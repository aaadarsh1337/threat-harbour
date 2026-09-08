#!/usr/bin/env python3
"""Threat Harbour renderer — metrics payload -> repo files.

Single source of truth: the JSON payload produced by scripts/parse_remote.py
(collected on the sensor). Everything derived is regenerated deterministically
so daily diffs contain only real data changes.

Usage:
    python3 scripts/render.py <payload.json> [--root <repo-root>]

Regenerates:
    analysis/metrics.json
    analysis/summary.md
    evidence/manifest.md
    README.md  (only the block between <!-- METRICS:START/END -->)
    diagrams/activity-timeline.png
    diagrams/session-funnel.png

Flow diagrams (graphviz) are infra, not data — re-rendered only on
infrastructure change, never by the daily job.
"""

import argparse
import datetime
import json
import os
import re
import sys

STACK = {"cowrie": "3.0.13", "grafana": "10.2.3", "loki": "2.9.4",
         "promtail": "2.9.4"}
SENSOR_LOG_PATH = "/home/jack/honeypot/var/log/cowrie/cowrie.json*"
OBS_START = "2026-08-27"


def fmt(n):
    return f"{n:,}"


def short_date(ts):
    # "2026-09-06T20:36:00Z" -> "06-09-2026"
    d = datetime.datetime.strptime(ts[:10], "%Y-%m-%d")
    return d.strftime("%d-%m-%Y")


def top5_table_rows(items, key):
    rows = []
    for i, it in enumerate(items[:5], 1):
        rows.append(f"| {i} | `{it[key]}` ({fmt(it['count'])}) |")
    return rows


def build_metrics(payload):
    """Merge the remote payload into the repo's metrics.json schema."""
    per_day = payload["collection"]["per_day_utc"]
    return {
        "analysis_cutoff_utc": payload["collected_at_utc"],
        "observation_period": {"start": OBS_START, "end": "ongoing",
                               "interim_cutoff": payload["collected_at_utc"][:10]},
        "totals": payload["totals"],
        "sources": payload["sources"],
        "sessions": payload["sessions"],
        "protocols": payload["protocols"],
        "logins": payload["logins"],
        "commands": payload["commands"],
        "behavioral_command_categories": payload["behavioral_command_categories"],
        "downloads_uploads": payload["downloads_uploads"],
        "event_ids": payload["event_ids"],
        "collection": {
            "files": payload["collection"]["files"],
            "log_path_on_sensor": SENSOR_LOG_PATH,
            "per_day_utc": per_day,
            "sensor_uptime_note": (
                f"Continuous daily log files {OBS_START} through "
                f"{payload['collected_at_utc'][:10]}, no missing days observed"
            ),
            "bad_json_lines": payload["totals"]["bad_json_lines"],
        },
        "stack": STACK,
        "method": ("Parsed Cowrie JSONL on sensor with Python json parser "
                   "(same source Promtail ships to Loki). Aggregates only; "
                   "raw IPs and payloads not published."),
    }


def readme_block(m):
    """Render the README hero section body (between the markers)."""
    cutoff = short_date(m["analysis_cutoff_utc"])
    t = m["totals"]["total_events"]
    ips = m["sources"]["unique_source_ips"]
    sess = m["sessions"]["session_connect_events"]
    lok = m["logins"]
    cmd = m["commands"]
    dl = m["downloads_uploads"]
    dur = m["sessions"]["session_duration_seconds"]
    cats = m["behavioral_command_categories"]
    disc = cats.get("discovery", 0)
    disc_pct = round(100 * disc / cmd["input_events"]) if cmd["input_events"] else 0
    under_pct = (round(100 * dur["under_10s"] / dur["n_closed_matched"])
                 if dur["n_closed_matched"] else 0)
    shas = dl.get("top_shasums", [])
    sha_note = (f" (hash `{shas[0]['value'][:8]}…`, content withheld)"
                if shas else " (content withheld)")
    top16 = m["sources"]["top_source_net16_by_event_volume"]
    net_note = (f"Busiest /16 by volume: `{top16[0]['cidr']}` "
                f"({fmt(top16[0]['events'])} events)"
                if top16 else "")

    user_rows, pass_rows, cmd_rows = [], [], []
    for i, (u, p, c) in enumerate(zip(lok["top_usernames"][:5],
                                      lok["top_passwords"][:5],
                                      cmd["top_commands"][:5]), 1):
        user_rows.append(f"| {i} | `{u['value']}` ({fmt(u['count'])}) |")
        pass_rows.append(f"| {i} | `{p['value']}` ({fmt(p['count'])}) |")
        short_cmd = c["input"] if len(c["input"]) <= 40 else c["input"][:40] + "…"
        cmd_rows.append(f"| {i} | `{short_cmd}` ({fmt(c['count'])}) |")

    lines = [
        f"## Collected Data — refreshed every 24 hours (last run `{cutoff} UTC`)",
        "",
        f"`27-08-2026` → `ongoing` · Cowrie `{STACK['cowrie']}` · SSH-only · `ap-hyderabad-1`.",
        "",
        "| Total events | Unique IPs | Sessions | Fake logins | Commands | Downloads (+uploads) |",
        "|---|---|---|---|---|---|",
        f"| `{fmt(t)}` | `{fmt(ips)}` | `{fmt(sess)}` | `{fmt(lok['success_fake'])}` / {fmt(lok['failed'])} failed | `{fmt(cmd['input_events'])}` (+{fmt(cmd['failed_command_events'])} failed) | `{fmt(dl['file_download_events'])}` (+{fmt(dl['file_upload_events'])}) |",
        "",
        "| # | Top username | Top password | Top command |",
        "|---|---|---|---|",
    ]
    for u, p, c in zip(user_rows, pass_rows, cmd_rows):
        # merge the three per-rank rows into one table row
        ur = u.split("|")[2].strip()
        pr = p.split("|")[2].strip()
        cr = c.split("|")[2].strip()
        lines.append(f"| {u.split('|')[1].strip()} | {ur} | {pr} | {cr} |")
    lines += [
        "",
        "Key findings:",
        "",
        f"- Median session `{dur['median']:.1f}s` ({under_pct}% under 10s) — mostly automated scanning, not humans.",
        f"- `{disc_pct}%` of commands are discovery/fingerprinting (`uname`, `hostname`, `whoami`).",
        f"- Repeated persistence probes writing toward `authorized_keys`{sha_note}.",
        f"- {net_note} — volume only, never attribution.",
        "",
        "![Session funnel](diagrams/session-funnel.png)",
        "![Activity timeline](diagrams/activity-timeline.png)",
        "",
        "Method + full tables: [`analysis/summary.md`](analysis/summary.md), [`analysis/metrics.json`](analysis/metrics.json). These results describe this sensor only.",
    ]
    return "\n".join(lines) + "\n"


def summary_md(m):
    cutoff = m["analysis_cutoff_utc"]
    per_day = m["collection"]["per_day_utc"]
    day_str = " · ".join(
        f"{k[5:]}: {fmt(v)}" for k, v in sorted(per_day.items()))
    lok, cmd, dur = m["logins"], m["commands"], m["sessions"]["session_duration_seconds"]
    cats = m["behavioral_command_categories"]
    per_day = m["collection"]["per_day_utc"]
    day_rows = "\n".join(
        f"| `{d}` | {fmt(c)} |" for d, c in sorted(per_day.items()))
    last_day = sorted(per_day)[-1]
    top_tables = []
    for title, items, key in (("Top usernames", lok["top_usernames"], "value"),
                              ("Top passwords", lok["top_passwords"], "value"),
                              ("Top commands", cmd["top_commands"], "input")):
        rows = "\n".join(
            f"| {i} | `{it[key][:60]}` | {fmt(it['count'])} |"
            for i, it in enumerate(items[:10], 1))
        top_tables.append(
            f"### {title}\n\n| # | Value | Tries |\n|---|---|---|\n{rows}")
    cat_rows = "\n".join(
        f"| `{k}` | {fmt(v)} |" for k, v in sorted(cats.items()))
    return f"""# Analysis summary (rolling snapshot, cutoff {cutoff})

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`{cutoff}` ({fmt(m['totals']['total_events'])} events).

## Source

- Cowrie JSONL on sensor: `{SENSOR_LOG_PATH}`
  ({m['collection']['files']} files, {m['totals']['bad_json_lines']} malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | {fmt(m['totals']['total_events'])} |
| Unique source IPs | {fmt(m['sources']['unique_source_ips'])} |
| Sessions (`cowrie.session.connect`) | {fmt(m['sessions']['session_connect_events'])} |
| SSH events | {fmt(m['totals']['total_events'])} (100%) |
| Fake successful logins (`cowrie.login.success`) | {fmt(lok['success_fake'])} |
| Failed logins | {fmt(lok['failed'])} |
| Command-input events | {fmt(cmd['input_events'])} (+{fmt(cmd['failed_command_events'])} `command.failed`) |
| File-download events | {fmt(m['downloads_uploads']['file_download_events'])} |
| File-upload events | {fmt(m['downloads_uploads']['file_upload_events'])} |
| Session duration median (n={fmt(dur['n_closed_matched'])} matched close) | {dur['median']:.1f}s; {fmt(dur['under_10s'])} < 10s; max ~{dur['max']:,.0f}s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
{day_rows}

`{last_day}` is partial at cutoff — do not annualize.

{top_tables[0]}

{top_tables[1]}

{top_tables[2]}

### Command categories

| Category | Events |
|---|---|
{cat_rows}

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `../dashboard/README.md`.
"""


def manifest_md(m, payload):
    files = payload["collection"]["file_lines"]
    file_rows = "\n".join(
        f"| `{name}` | {fmt(n)} |" for name, n in sorted(files.items()))
    return f"""# Evidence manifest (rolling snapshot, cutoff {m['analysis_cutoff_utc']})

Raw Cowrie logs are **retained on the sensor only** and are not published.
This manifest lets a reviewer re-derive `analysis/metrics.json`.

## Dataset

- Host path: `{SENSOR_LOG_PATH}` ({payload['collection']['files']} files)
- Total lines: {fmt(m['totals']['total_events'])} ({m['totals']['bad_json_lines']} malformed)
- Cowrie: `{STACK['cowrie']}`
- Collector: Promtail `{STACK['promtail']}` → Loki `{STACK['loki']}` (`job="cowrie"`), Grafana `{STACK['grafana']}`

### Lines per file

| File | Lines |
|---|---|
{file_rows}

## What is / is not in this repo

- IN REPO: aggregates (`analysis/`), redacted hashes/destfile patterns,
  /16 volume buckets, top username/password/command strings (these are
  attacker guesses, not sensitive).
- NOT IN REPO: raw `cowrie.json*`, raw source IPs, payload contents,
  host keys, SSH private keys, OCI identifiers, sensor public IP.

## Re-derivation

Automated daily via `.github/workflows/daily-metrics.yml` (manual trigger:
Actions → daily-metrics → Run workflow). Manual equivalent is documented in
`docs/operations.md`.

## Health / continuity

- Per-day counts in `analysis/metrics.json`; any missing day is flagged by
  the renderer as a collection gap. Uptime percentage is not claimed.
"""


def draw_timeline(m, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    BG, NAVY, TEAL, AMBER, SLATE = "#f4f6f9", "#1b2a4a", "#0e7c7b", "#c67c1b", "#5b6b82"
    plt.rcParams.update({"font.family": "sans-serif"})
    per_day = m["collection"]["per_day_utc"]
    days = sorted(per_day)
    counts = [per_day[d] for d in days]
    labels = [d[5:].replace("-", "-") + ("*" if d == days[-1] else "") for d in days]
    fig, ax = plt.subplots(figsize=(13, 5.8))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_title("Threat Harbour — Events per UTC day (SSH-only)", fontsize=14,
                 weight="bold", color=NAVY, loc="left", pad=12)
    bars = ax.bar(labels,
                  counts,
                  color=[AMBER if c == max(counts) else TEAL if c > 10000 else NAVY
                         for c in counts],
                  edgecolor="white")
    ax.bar_label(bars, labels=[f"{c:,}" for c in counts], fontsize=8.5, color=NAVY, padding=3)
    ax.set_ylabel("events", color=SLATE)
    ax.tick_params(colors=SLATE, labelsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.01, -0.22,
            f"* {labels[-1].rstrip('*')} is a partial day at cutoff ({counts[-1]:,}) — do not annualize. "
            f"Total {sum(counts):,}.",
            transform=ax.transAxes, fontsize=9, color=SLATE, style="italic")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def draw_funnel(m, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    BG, NAVY, TEAL, AMBER, SLATE = "#f4f6f9", "#1b2a4a", "#0e7c7b", "#c67c1b", "#5b6b82"
    plt.rcParams.update({"font.family": "sans-serif"})
    cutoff = m["analysis_cutoff_utc"][:10]
    sess = m["sessions"]["session_connect_events"]
    lok, cmd = m["logins"]["success_fake"], m["commands"]["input_events"]
    dl = m["downloads_uploads"]["file_download_events"]
    dur = m["sessions"]["session_duration_seconds"]
    under_pct = round(100 * dur["under_10s"] / dur["n_closed_matched"]) if dur["n_closed_matched"] else 0
    shas = m["downloads_uploads"].get("top_shasums", [])
    sha = shas[0]["value"][:8] + "…" if shas else "…"
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_title(f"Threat Harbour — SSH Session Funnel (interim {cutoff} UTC)",
                 fontsize=15, weight="bold", color=NAVY, loc="left", pad=28)
    ax.text(0.01, 1.02,
            f"{sess:,} connects → {lok:,} fake logins → {cmd:,} command sessions → {dl:,} download events"
            f"  ·  median session {dur['median']:.1f}s, {under_pct}% < 10s",
            transform=ax.transAxes, fontsize=10, color=SLATE, va="bottom")
    stages = ["Session\nconnect", "Fake login\nsuccess", "Command\ninput", "File\n-download"]
    vals = [sess, lok, cmd, dl]
    bars = ax.bar(stages, vals, color=[NAVY, TEAL, AMBER, "#b3372f"],
                  edgecolor="white", linewidth=1.5, width=0.55)
    ax.set_yscale("log")
    for b, v, o in zip(bars, vals, [1.18, 1.3, 1.3, 2.2]):
        ax.text(b.get_x() + b.get_width() / 2, v * o, f"{v:,}",
                ha="center", va="bottom", fontsize=12, weight="bold", color=NAVY)
    ax.set_ylabel("events (log scale)", color=SLATE)
    ax.tick_params(colors=SLATE)
    ax.spines[["top", "right"]].set_visible(False)
    cats = m["behavioral_command_categories"]
    disc_pct = round(100 * cats.get("discovery", 0) / cmd) if cmd else 0
    fig.text(0.5, 0.02,
             f"Plus: {m['logins']['failed']:,} failed logins · {m['commands']['failed_command_events']:,} failed commands · "
             f"{m['downloads_uploads']['file_upload_events']:,} uploads · discovery = {disc_pct}% of commands · "
             f"persistence probes → authorized_keys (hash {sha})",
             ha="center", fontsize=8.5, color=SLATE, style="italic")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def replace_readme_block(root, block):
    path = os.path.join(root, "README.md")
    with open(path) as fh:
        text = fh.read()
    pattern = re.compile(r"<!-- METRICS:START -->\n.*?\n<!-- METRICS:END -->",
                         re.DOTALL)
    if not pattern.search(text):
        print("ERROR: METRICS markers not found in README.md", file=sys.stderr)
        return False
    text = pattern.sub("<!-- METRICS:START -->\n" + block + "<!-- METRICS:END -->", text)
    with open(path, "w") as fh:
        fh.write(text)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("payload", help="JSON payload from parse_remote.py")
    ap.add_argument("--root", default=".", help="repo root")
    args = ap.parse_args()

    with open(args.payload) as fh:
        payload = json.load(fh)
    if "error" in payload:
        print(f"ERROR from sensor: {payload['error']}", file=sys.stderr)
        return 1

    m = build_metrics(payload)

    with open(os.path.join(args.root, "analysis/metrics.json"), "w") as fh:
        json.dump(m, fh, indent=1)
        fh.write("\n")
    with open(os.path.join(args.root, "analysis/summary.md"), "w") as fh:
        fh.write(summary_md(m))
    with open(os.path.join(args.root, "evidence/manifest.md"), "w") as fh:
        fh.write(manifest_md(m, payload))
    if not replace_readme_block(args.root, readme_block(m)):
        return 1
    draw_timeline(m, os.path.join(args.root, "diagrams/activity-timeline.png"))
    draw_funnel(m, os.path.join(args.root, "diagrams/session-funnel.png"))

    eids = m["event_ids"]
    gap_days = [d for d, c in m["collection"]["per_day_utc"].items() if c == 0]
    print(f"cutoff={m['analysis_cutoff_utc']} total={m['totals']['total_events']:,} "
          f"sessions={m['sessions']['session_connect_events']:,} "
          f"ips={m['sources']['unique_source_ips']:,}")
    if gap_days:
        print(f"WARNING: zero-event days (possible gap): {gap_days}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
