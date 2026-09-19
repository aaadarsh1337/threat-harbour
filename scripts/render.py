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
import tempfile

STACK = {"cowrie": "3.0.13", "grafana": "10.2.3", "loki": "2.9.4",
         "promtail": "2.9.4"}
SENSOR_LOG_PATH = "/home/jack/honeypot/var/log/cowrie/cowrie.json*"
OBS_START = "2026-08-27"

# Timeline is fully daily up to this many days. Beyond it, the chart turns
# hybrid (see RECENT_DAILY_DAYS): recent detail stays daily, only older
# history is compressed — so day 46 looks like day 45 plus a small
# aggregated tail instead of a jarring granularity switch.
TIMELINE_DAILY_LIMIT = 45
# In hybrid mode, the last N days always render as daily bars.
RECENT_DAILY_DAYS = 30
# Older history spans at most this many days before it buckets monthly
# instead of weekly, keeping total bars bounded even after a year.
WEEKLY_SPAN_LIMIT = 84
# Days shown inline in summary.md before older days collapse into <details>.
SUMMARY_INLINE_DAYS = 30
# Absolute-count highlight cutoff (currently unused for colour; kept so
# archived payloads/metrics carrying it still validate conceptually).
# Tokyo Night (matches aaadarsh1337.github.io/intel + css/tokens.css).
# Site chart reference: base bars #7aa2f7 @0.75, peak #f7768e, latest #7dcfff,
# grid #292e42, values #a9b1d6, axis labels #7d86b0, Mono for numbers.
T_BG = "#1a1b26"      # --bg-elev (.panel background)
T_FIG_EDGE = "#16161e"  # --bg (figure edge / bar outlines)
T_GRID = "#292e42"    # --line
T_INK = "#c0caf5"     # --ink (titles, values)
T_MUTED = "#a9b1d6"   # --muted (subtitles, bar labels)
T_FAINT = "#7d86b0"   # --faint (axis ticks, footers)
T_BLUE = "#7aa2f7"    # --accent-2 (base bars)
T_CYAN = "#7dcfff"    # --accent (latest / partial bucket)
T_PINK = "#f7768e"    # --danger (peak)
T_PURPLE = "#bb9af7"  # kpi-3 accent (funnel stage 3)
T_MONO = "monospace"
T_SANS = "sans-serif"


def fmt(n):
    return f"{n:,}"


def short_date(ts):
    # "2026-09-06T20:36:00Z" -> "2026-09-06" (ISO, unambiguous).
    d = datetime.datetime.strptime(ts[:10], "%Y-%m-%d")
    return d.strftime("%Y-%m-%d")


def obs_start_display():
    return datetime.datetime.strptime(OBS_START, "%Y-%m-%d").strftime(
        "%Y-%m-%d")


def md_cell(value, max_len=60):
    """Escape attacker-controlled strings for markdown tables."""
    s = str(value).replace("`", "'").replace("|", "\\|")
    s = re.sub(r"[\x00-\x08\x0b-\x1f\x7f]", "", s).replace("\n", " ")
    s = " ".join(s.split())
    if len(s) > max_len:
        s = s[:max_len] + "…"
    return s or "?"


def atomic_write(path, text):
    d = os.path.dirname(os.path.abspath(path))
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".tmp-")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _require(payload, *keys):
    missing = [k for k in keys if k not in payload]
    if missing:
        raise ValueError(f"payload missing keys: {', '.join(missing)}")


def validate_payload(payload):
    """Fail fast with a clear message instead of a raw KeyError."""
    if not isinstance(payload, dict):
        raise ValueError("payload must be a JSON object")
    _require(payload, "collected_at_utc", "totals", "sources", "sessions",
             "protocols", "logins", "commands", "behavioral_command_categories",
             "downloads_uploads", "event_ids", "collection")
    _require(payload["totals"], "total_events", "bad_json_lines")
    _require(payload["logins"], "success_fake", "failed",
             "top_usernames", "top_passwords")
    _require(payload["commands"], "input_events", "failed_command_events",
             "top_commands")
    _require(payload["collection"], "files", "file_lines", "per_day_utc")
    datetime.datetime.strptime(payload["collected_at_utc"][:10], "%Y-%m-%d")


def missing_days(per_day, cutoff_day):
    """Days in OBS_START..cutoff with no events (true collection gaps)."""
    try:
        start = datetime.datetime.strptime(OBS_START, "%Y-%m-%d").date()
        end = datetime.datetime.strptime(cutoff_day, "%Y-%m-%d").date()
    except ValueError:
        return []
    if end < start:
        return []
    missing = []
    d = start
    while d <= end:
        if per_day.get(d.isoformat(), 0) == 0:
            missing.append(d.isoformat())
        d += datetime.timedelta(days=1)
    return missing


def build_metrics(payload):
    """Merge the remote payload into the repo's metrics.json schema."""
    validate_payload(payload)
    per_day = payload["collection"]["per_day_utc"]
    cutoff_day = payload["collected_at_utc"][:10]
    gaps = missing_days(per_day, cutoff_day)
    if gaps:
        uptime_note = (
            f"Daily log files {OBS_START} through {cutoff_day}; "
            f"{len(gaps)} day(s) with zero events "
            f"({', '.join(gaps[:5])}"
            f"{'…' if len(gaps) > 5 else ''}) — see per-day table"
        )
    else:
        uptime_note = (
            f"Continuous daily log files {OBS_START} through {cutoff_day}, "
            "no missing days observed"
        )
    return {
        "analysis_cutoff_utc": payload["collected_at_utc"],
        "observation_period": {"start": OBS_START, "end": "ongoing",
                               "interim_cutoff": cutoff_day},
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
            "sensor_uptime_note": uptime_note,
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
    sha_note = (f" (hash `{md_cell(shas[0]['value'], 8)}…`, content withheld)"
                if shas else " (content withheld)")
    top16 = m["sources"]["top_source_net16_by_event_volume"]
    net_note = (f"Busiest /16 by volume: `{top16[0]['cidr']}` "
                f"({fmt(top16[0]['events'])} events)"
                if top16 else "")

    # Pad the shortest list so unequal top-N lengths never drop rows.
    users = lok["top_usernames"][:5]
    passes = lok["top_passwords"][:5]
    cmds = cmd["top_commands"][:5]
    nrows = max(len(users), len(passes), len(cmds), 1)
    rows = []
    for i in range(nrows):
        u = (f"`{md_cell(users[i]['value'])}` ({fmt(users[i]['count'])})"
             if i < len(users) else "—")
        p = (f"`{md_cell(passes[i]['value'])}` ({fmt(passes[i]['count'])})"
             if i < len(passes) else "—")
        if i < len(cmds):
            short_cmd = md_cell(cmds[i]["input"], 40)
            c = f"`{short_cmd}` ({fmt(cmds[i]['count'])})"
        else:
            c = "—"
        rows.append(f"| {i + 1} | {u} | {p} | {c} |")

    dl_failed = dl.get("file_download_failed_events", 0)
    dl_label = (f"`{fmt(dl['file_download_events'])}` "
                f"(+{fmt(dl['file_upload_events'])} uploads"
                f"{f', +{fmt(dl_failed)} dl-failed' if dl_failed else ''})")
    lines = [
        f"## Collected Data — refreshed every 24 hours (last run `{cutoff} UTC`)",
        "",
        f"`{obs_start_display()}` → `ongoing` · Cowrie `{STACK['cowrie']}` · SSH-only · `ap-hyderabad-1`.",
        "",
        "| Total events | Unique IPs | Sessions | Fake logins | Commands | Downloads (+uploads) |",
        "|---|---|---|---|---|---|",
        f"| `{fmt(t)}` | `{fmt(ips)}` | `{fmt(sess)}` | `{fmt(lok['success_fake'])}` / {fmt(lok['failed'])} failed | `{fmt(cmd['input_events'])}` (+{fmt(cmd['failed_command_events'])} failed) | {dl_label} |",
        "",
        "| # | Top username | Top password | Top command |",
        "|---|---|---|---|",
        *rows,
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


def _per_day_table(per_day):
    days = sorted(per_day.items())
    if len(days) <= SUMMARY_INLINE_DAYS:
        return "\n".join(f"| `{d}` | {fmt(c)} |" for d, c in days)
    recent = days[-SUMMARY_INLINE_DAYS:]
    older = days[:-SUMMARY_INLINE_DAYS]
    recent_rows = "\n".join(f"| `{d}` | {fmt(c)} |" for d, c in recent)
    older_rows = "\n".join(f"| `{d}` | {fmt(c)} |" for d, c in older)
    return (recent_rows + "\n\n<details>\n<summary>Older days "
            f"({len(older)} days, click to expand)</summary>\n\n"
            "| Day (UTC) | Events |\n|---|---|\n" + older_rows + "\n\n</details>")


def summary_md(m):
    cutoff = m["analysis_cutoff_utc"]
    per_day = m["collection"]["per_day_utc"]
    lok, cmd, dur = m["logins"], m["commands"], m["sessions"]["session_duration_seconds"]
    cats = m["behavioral_command_categories"]
    day_table = _per_day_table(per_day) if per_day else "_No per-day data._"
    last_day = sorted(per_day)[-1] if per_day else "?"
    top_tables = []
    for title, items, key in (("Top usernames", lok["top_usernames"], "value"),
                              ("Top passwords", lok["top_passwords"], "value"),
                              ("Top commands", cmd["top_commands"], "input")):
        rows = "\n".join(
            f"| {i} | `{md_cell(it[key])}` | {fmt(it['count'])} |"
            for i, it in enumerate(items[:10], 1)) or "_none_"
        top_tables.append(
            f"### {title}\n\n| # | Value | Tries |\n|---|---|---|\n{rows}")
    cat_rows = "\n".join(
        f"| `{k}` | {fmt(v)} |" for k, v in sorted(cats.items())) or "_none_"
    dl_failed = m["downloads_uploads"].get("file_download_failed_events", 0)
    dl_extra = (f"\n| File-download failures | {fmt(dl_failed)} |"
                if dl_failed else "")
    return f"""# Analysis summary (rolling snapshot, cutoff {cutoff})

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `{OBS_START}` → `ongoing`. Numbers below are a snapshot at
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
| File-download events | {fmt(m['downloads_uploads']['file_download_events'])} |{dl_extra}
| File-upload events | {fmt(m['downloads_uploads']['file_upload_events'])} |
| Session duration median (n={fmt(dur['n_closed_matched'])} matched close) | {dur['median']:.1f}s; {fmt(dur['under_10s'])} < 10s; max ~{dur['max']:,.0f}s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
{day_table}

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

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
"""


def manifest_md(m, payload):
    files = payload["collection"]["file_lines"]
    file_rows = "\n".join(
        f"| `{md_cell(name, 80)}` | {fmt(n)} |" for name, n in sorted(files.items()))
    open_errs = payload["collection"].get("file_open_errors", {})
    err_section = ""
    if open_errs:
        err_rows = "\n".join(
            f"| `{md_cell(k, 80)}` | `{md_cell(v, 120)}` |"
            for k, v in sorted(open_errs.items()))
        err_section = ("\n### File open errors\n\n| File | Error |\n"
                       "|---|---|\n" + err_rows + "\n")
    return f"""# Evidence manifest (rolling snapshot, cutoff {m['analysis_cutoff_utc']})

Raw Cowrie logs are **retained on the sensor only** and are not published.
This manifest lets a reviewer re-derive `analysis/metrics.json`.

## Dataset

- Host path: `{SENSOR_LOG_PATH}` ({payload['collection']['files']} files)
- Total lines: {fmt(m['totals']['total_events'])} ({m['totals']['bad_json_lines']} malformed)
- Cowrie: `{STACK['cowrie']}`
- Collector: Promtail `{STACK['promtail']}` → Loki `{STACK['loki']}` (`job="cowrie"`), Grafana `{STACK['grafana']}`

### Lines per file (valid JSON lines; sum equals total events)

| File | Lines |
|---|---|
{file_rows}
{err_section}
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


def _bucket_weekly(per_day):
    weeks = {}
    for day, count in per_day.items():
        d = datetime.datetime.strptime(day, "%Y-%m-%d").date()
        start = d - datetime.timedelta(days=d.weekday())  # Monday
        weeks[start] = weeks.get(start, 0) + count
    return sorted(weeks.items())


def _bucket_monthly(per_day):
    months = {}
    for day, count in per_day.items():
        d = datetime.datetime.strptime(day, "%Y-%m-%d").date()
        start = d.replace(day=1)
        months[start] = months.get(start, 0) + count
    return sorted(months.items())


def draw_timeline(m, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    BG, INK, MUTED, FAINT, GRID = T_BG, T_INK, T_MUTED, T_FAINT, T_GRID
    plt.rcParams.update({"font.family": T_SANS})
    per_day = m["collection"]["per_day_utc"]

    def _empty(msg):
        fig, ax = plt.subplots(figsize=(13, 4))
        fig.patch.set_facecolor(BG)
        ax.set_facecolor(BG)
        ax.set_title("Threat Harbour — Events per UTC day (SSH-only)",
                     fontsize=14, weight="bold", color=INK, loc="left",
                     fontfamily=T_SANS)
        ax.text(0.5, 0.5, msg, ha="center", va="center", color=MUTED)
        ax.axis("off")
        fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=BG)
        plt.close(fig)

    if not per_day:
        _empty("No per-day data at this cutoff.")
        return
    days = sorted(per_day)
    section_split = None  # index where the aggregated history ends
    if len(days) <= TIMELINE_DAILY_LIMIT:
        labels = [d[5:] for d in days]
        counts = [per_day[d] for d in days]
        xlabel = None
    else:
        # Hybrid: the last RECENT_DAILY_DAYS stay daily; only older days
        # compress (weekly, or monthly once the older span is long). Each
        # new day shifts one bar from daily into the aggregated tail, so
        # the chart evolves smoothly instead of switching granularity
        # overnight at the threshold.
        recent = days[-RECENT_DAILY_DAYS:]
        older = days[:-RECENT_DAILY_DAYS]
        d0 = datetime.datetime.strptime(older[0], "%Y-%m-%d").date()
        d1 = datetime.datetime.strptime(older[-1], "%Y-%m-%d").date()
        sub = {d: per_day[d] for d in older}
        if (d1 - d0).days + 1 <= WEEKLY_SPAN_LIMIT:
            buckets = _bucket_weekly(sub)
            agg_labels = [s.strftime("%b %d") for s, _ in buckets]
            agg_kind = "weekly"
        else:
            buckets = _bucket_monthly(sub)
            agg_labels = [s.strftime("%b '%y") for s, _ in buckets]
            agg_kind = "monthly"
        agg_counts = [c for _, c in buckets]
        labels = agg_labels + [d[5:] for d in recent]
        counts = agg_counts + [per_day[d] for d in recent]
        section_split = len(agg_labels)
        xlabel = (f"Dim bars: older history in {agg_kind} buckets · "
                  f"bright bars: last {RECENT_DAILY_DAYS} days daily · "
                  "full series in analysis/summary.md")
    title = "Threat Harbour — Events per UTC day (SSH-only)"
    peak = max(counts)
    width = max(13, min(20, 6 + len(counts) * 0.35))
    fig, ax = plt.subplots(figsize=(width, 5.8))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_title(title, fontsize=14, weight="bold", color=INK, loc="left",
                 pad=12, fontfamily=T_SANS)
    # Site semantics: peak = pink, latest/partial = cyan, rest = blue.
    # Aggregated-history bars are dimmed so the two sections read apart;
    # highlights always render full-strength wherever they fall.
    # HIGH_VOLUME_THRESHOLD no longer drives colour (kept for compat).
    from matplotlib.colors import to_rgba
    last_idx = len(counts) - 1
    colors = []
    for i, c in enumerate(counts):
        in_agg = section_split is not None and i < section_split
        if c == peak:
            colors.append(to_rgba(T_PINK, 0.92))
        elif i == last_idx:
            colors.append(to_rgba(T_CYAN, 0.92))
        else:
            colors.append(to_rgba(T_BLUE, 0.55 if in_agg else 0.92))
    bars = ax.bar(labels, counts, color=colors, edgecolor=T_FIG_EDGE,
                  linewidth=1.0, zorder=3)
    if section_split:
        ax.axvline(x=section_split - 0.5, color=GRID,
                   linestyle=(0, (4, 4)), linewidth=1, zorder=2)
    ax.yaxis.grid(True, color=GRID, linestyle=(0, (4, 4)), linewidth=1,
                   alpha=1.0, zorder=0)
    ax.set_axisbelow(True)
    # Label every bar only when readable; otherwise label just the peak.
    if len(counts) <= 30:
        ax.bar_label(bars, labels=[f"{c:,}" for c in counts], fontsize=8.5,
                     color=MUTED, padding=3, fontfamily=T_MONO)
    else:
        idx = counts.index(peak)
        ax.bar_label(bars,
                     labels=[f"{peak:,}" if i == idx else ""
                             for i in range(len(counts))],
                     fontsize=9, color=MUTED, padding=3,
                     fontfamily=T_MONO)
    ax.set_ylabel("events", color=FAINT)
    if xlabel:
        ax.set_xlabel(xlabel, color=FAINT, fontsize=9, style="italic")
    ax.tick_params(colors=FAINT, labelsize=9)
    for lbl in ax.get_xticklabels():
        lbl.set_fontfamily(T_MONO)
    for lbl in ax.get_yticklabels():
        lbl.set_fontfamily(T_MONO)
    if len(counts) > 12:
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(GRID)
    day_range = f"{days[0]} → {days[-1]}"
    if section_split:
        footer = (f"{day_range} ({sum(counts):,} events): older history in "
                  f"buckets, last {RECENT_DAILY_DAYS} days daily. "
                  f"* {days[-1]} is partial at cutoff "
                  f"({counts[-1]:,}) — do not annualize.")
    else:
        footer = (f"* {days[-1]} is a partial day at cutoff "
                  f"({counts[-1]:,}) — do not annualize. "
                  f"{day_range}, total {sum(counts):,}.")
    ax.text(0.01, -0.24, footer, transform=ax.transAxes, fontsize=9,
            color=FAINT, style="italic")
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


def draw_funnel(m, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    BG, INK, MUTED, FAINT, GRID = T_BG, T_INK, T_MUTED, T_FAINT, T_GRID
    plt.rcParams.update({"font.family": T_SANS})
    cutoff = m["analysis_cutoff_utc"][:10]
    sess = m["sessions"]["session_connect_events"]
    lok, cmd = m["logins"]["success_fake"], m["commands"]["input_events"]
    dl = m["downloads_uploads"]["file_download_events"]
    dur = m["sessions"]["session_duration_seconds"]
    under_pct = round(100 * dur["under_10s"] / dur["n_closed_matched"]) if dur["n_closed_matched"] else 0
    shas = m["downloads_uploads"].get("top_shasums", [])
    sha = md_cell(shas[0]["value"], 8) + "…" if shas else "…"
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_title(f"Threat Harbour — SSH Session Funnel (rolling {cutoff} UTC)",
                 fontsize=15, weight="bold", color=INK, loc="left", pad=38,
                 fontfamily=T_SANS)
    ax.text(0.01, 1.06,
            f"{sess:,} connects → {lok:,} fake logins → {cmd:,} command sessions → {dl:,} download events"
            f"  ·  median session {dur['median']:.1f}s, {under_pct}% < 10s",
            transform=ax.transAxes, fontsize=10, color=MUTED, va="bottom",
            fontfamily=T_SANS)
    stages = ["Session\nconnect", "Fake login\nsuccess", "Command\ninput", "File\n-download"]
    vals = [sess, lok, cmd, dl]
    # Log scale can't render 0; floor at 0.5 for the bar but label the truth.
    plot_vals = [max(v, 0.5) for v in vals]
    bars = ax.bar(stages, plot_vals,
                  color=[T_BLUE, T_CYAN, T_PURPLE, T_PINK],
                  edgecolor=T_FIG_EDGE, linewidth=1.5, width=0.55,
                  alpha=0.92, zorder=3)
    ax.set_yscale("log")
    ax.set_ylim(bottom=0.5)
    ax.yaxis.grid(True, color=GRID, linestyle=(0, (4, 4)), linewidth=1,
                   alpha=1.0, zorder=0, which="major")
    for b, v, pv in zip(bars, vals, plot_vals):
        y = pv * (1.3 if v > 0 else 2.2)
        ax.text(b.get_x() + b.get_width() / 2, y, f"{v:,}",
                ha="center", va="bottom", fontsize=12, weight="bold",
                color=INK, fontfamily=T_MONO)
    ax.set_ylabel("events (log scale)", color=FAINT)
    ax.tick_params(colors=FAINT)
    for lbl in ax.get_xticklabels():
        lbl.set_fontfamily(T_SANS)
    for lbl in ax.get_yticklabels():
        lbl.set_fontfamily(T_MONO)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(GRID)
    cats = m["behavioral_command_categories"]
    disc_pct = round(100 * cats.get("discovery", 0) / cmd) if cmd else 0
    fig.text(0.5, 0.02,
             f"Plus: {m['logins']['failed']:,} failed logins · {m['commands']['failed_command_events']:,} failed commands · "
             f"{m['downloads_uploads']['file_upload_events']:,} uploads · discovery = {disc_pct}% of commands · "
             f"persistence probes → authorized_keys (hash {sha})",
             ha="center", fontsize=8.5, color=FAINT, style="italic")
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


def replace_readme_block(root, block):
    path = os.path.join(root, "README.md")
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    pattern = re.compile(r"<!-- METRICS:START -->\n.*?\n<!-- METRICS:END -->",
                         re.DOTALL)
    if not pattern.search(text):
        print("ERROR: METRICS markers not found in README.md", file=sys.stderr)
        return False
    text = pattern.sub("<!-- METRICS:START -->\n" + block + "<!-- METRICS:END -->", text)
    atomic_write(path, text)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("payload", help="JSON payload from parse_remote.py")
    ap.add_argument("--root", default=".", help="repo root")
    args = ap.parse_args()

    with open(args.payload, encoding="utf-8") as fh:
        payload = json.load(fh)
    if "error" in payload:
        print(f"ERROR from sensor: {payload['error']}", file=sys.stderr)
        return 1
    try:
        validate_payload(payload)
    except ValueError as exc:
        print(f"ERROR: invalid payload: {exc}", file=sys.stderr)
        return 1

    m = build_metrics(payload)

    atomic_write(os.path.join(args.root, "analysis/metrics.json"),
                 json.dumps(m, indent=1) + "\n")
    atomic_write(os.path.join(args.root, "analysis/summary.md"), summary_md(m))
    atomic_write(os.path.join(args.root, "evidence/manifest.md"),
                 manifest_md(m, payload))
    if not replace_readme_block(args.root, readme_block(m)):
        return 1
    draw_timeline(m, os.path.join(args.root, "diagrams/activity-timeline.png"))
    draw_funnel(m, os.path.join(args.root, "diagrams/session-funnel.png"))

    per_day = m["collection"]["per_day_utc"]
    zero_days = sorted(d for d, c in per_day.items() if c == 0)
    gaps = missing_days(per_day, m["analysis_cutoff_utc"][:10])
    print(f"cutoff={m['analysis_cutoff_utc']} total={m['totals']['total_events']:,} "
          f"sessions={m['sessions']['session_connect_events']:,} "
          f"ips={m['sources']['unique_source_ips']:,}")
    if gaps:
        print(f"WARNING: missing/zero-event days (possible gap): {gaps}")
    elif zero_days:
        print(f"WARNING: zero-event days (possible gap): {zero_days}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
