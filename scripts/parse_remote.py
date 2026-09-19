#!/usr/bin/env python3
"""Threat Harbour remote parser — runs ON the sensor via passwordless sudo.

Deployed fresh each run (scp to /tmp/th-parse-<ts>.py, executed, deleted),
so the sensor carries no agent and there is no version drift.

Reads Cowrie JSONL, prints ONE JSON object (the metrics payload) to stdout.
Only aggregates leave the sensor: no raw IPs, payloads, keys, or identifiers.

Usage on the sensor:
    sudo /usr/bin/python3 /tmp/th-parse-<ts>.py
Requires stdlib only.
"""

import collections
import datetime
import glob
import gzip
import json
import os
import re
import sys

LOG_GLOB = "/home/jack/honeypot/var/log/cowrie/cowrie.json*"

# Split chained shell commands so `echo hi; rm -rf /` is still seen as
# destructive, not just shell-exec. Covers ; && || | & newlines.
_CHAIN_SPLIT = re.compile(r"&&|\|\||[;|&\n]+")
# Miner indicators matched on word boundaries so `exminer` etc. don't match.
_MINER_RE = re.compile(
    r"\b(xmrig|minerd|mining|cryptonight|stratum\+tcp|\bminer\b)")
_DOWNLOADER_BINS = {"wget", "curl", "tftp", "ftp", "scp", "aria2c"}
_PERSIST_BINS = {"chmod", "chpasswd", "passwd", "useradd", "adduser",
                 "usermod", "crontab", "systemctl", "service", "iptables"}
_DESTRUCTIVE_BINS = {"rm", "dd", "mkfs", "shutdown", "reboot", "kill",
                     "pkill"}
_DISCOVERY_BINS = {"uname", "hostname", "whoami", "id", "pwd", "arch",
                   "ls", "cat", "ps", "netstat", "ss", "ifconfig", "ip",
                   "mount", "df", "uptime", "history"}
_SHELL_BINS = {"sh", "bash", "python", "python3", "perl", "busybox",
               "export", "echo", "ssh"}


def _tokens(cmd):
    """Yield normalized binary names for every command in a chain."""
    c = (cmd or "").strip().lower()
    if not c:
        return
    for chunk in _CHAIN_SPLIT.split(c):
        chunk = chunk.strip()
        if not chunk:
            continue
        # strip sudo/nohup/env prefixes: `sudo rm -rf /` -> rm
        parts = chunk.split()
        while parts and parts[0] in ("sudo", "nohup", "env", "nice"):
            parts = parts[1:]
        if not parts:
            continue
        # `sh -c 'rm ...'` -> look at the rest too, not just `sh`
        first = parts[0].split("/")[-1]
        yield first
        # also surface binaries later in the chunk (e.g. `sh -c rm`)
        for p in parts[1:]:
            yield p.split("/")[-1].strip("'\"")


def cmd_category(cmd):
    c = (cmd or "").strip().lower()
    if not c:
        return "empty"
    toks = set(_tokens(cmd))
    if not toks:
        return "empty"
    # Highest severity wins so chained attacks aren't masked by `echo`/`sh`.
    if toks & _DESTRUCTIVE_BINS:
        return "destructive"
    if toks & _PERSIST_BINS:
        return "persistence-privilege"
    if toks & _DOWNLOADER_BINS:
        return "downloader"
    if _MINER_RE.search(c):
        return "miner-indicator"
    if toks & _DISCOVERY_BINS:
        return "discovery"
    if toks & _SHELL_BINS:
        return "shell-exec"
    return "other"


def _median(sorted_vals):
    n = len(sorted_vals)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 1:
        return sorted_vals[mid]
    return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2


def _open_log(path):
    if path.endswith(".gz"):
        return gzip.open(path, "rt", encoding="utf-8", errors="replace")
    return open(path, "r", encoding="utf-8", errors="replace")


def main():
    files = sorted(glob.glob(LOG_GLOB))
    # Cowrie rotates to .gz eventually; read those too instead of
    # miscounting them as bad lines. Ignore unrelated suffixes.
    files = [p for p in files
             if os.path.basename(p).startswith("cowrie.json")]
    if not files:
        print(json.dumps({"error": "no log files matched " + LOG_GLOB}))
        return 1

    total = 0
    bad = 0
    eventids = collections.Counter()
    srcips = set()
    sessions = set()
    protocols = collections.Counter()
    usernames = collections.Counter()
    passwords = collections.Counter()
    commands = collections.Counter()
    cmdcat = collections.Counter()
    login_success = 0
    login_failed = 0
    cmd_events = 0
    cmd_failed = 0
    downloads = 0
    downloads_failed = 0
    uploads = 0
    destfiles = collections.Counter()
    shasums = collections.Counter()
    connects = 0
    unmatched_closes = 0
    ipv6_events = 0
    per_day = collections.Counter()
    net16 = collections.Counter()
    starts = {}
    durations = []
    file_lines = {}
    file_open_errors = {}

    for path in files:
        n = 0
        try:
            fh = _open_log(path)
        except OSError as exc:
            file_open_errors[os.path.basename(path)] = str(exc)
            continue
        with fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    e = json.loads(line)
                except json.JSONDecodeError:
                    bad += 1
                    continue
                n += 1
                total += 1
                eid = e.get("eventid", "?")
                eventids[eid] += 1
                ts = e.get("timestamp", "")
                if len(ts) >= 10:
                    per_day[ts[:10]] += 1
                ip = e.get("src_ip")
                if ip:
                    if ":" in ip:
                        # IPv6: counted, not bucketed into /16.
                        ipv6_events += 1
                        srcips.add(ip)
                    else:
                        srcips.add(ip)
                        parts = ip.split(".")
                        if len(parts) == 4:
                            net16[parts[0] + "." + parts[1] + ".0.0/16"] += 1
                if e.get("session"):
                    sessions.add(e["session"])
                if e.get("protocol"):
                    protocols[e["protocol"]] += 1
                if eid == "cowrie.session.connect":
                    connects += 1
                    # First start wins: duplicate session IDs must not
                    # overwrite the original connect timestamp.
                    if e.get("session") and e["session"] not in starts:
                        starts[e["session"]] = ts
                elif eid == "cowrie.session.closed":
                    if e.get("session") in starts:
                        try:
                            t0 = datetime.datetime.fromisoformat(
                                starts[e["session"]].replace("Z", "+00:00"))
                            t1 = datetime.datetime.fromisoformat(
                                ts.replace("Z", "+00:00"))
                            delta = (t1 - t0).total_seconds()
                            # Negative deltas come from clock skew or the
                            # force-reboot truncating an in-flight line.
                            if delta >= 0:
                                durations.append(delta)
                        except (ValueError, KeyError):
                            pass
                        finally:
                            # Bound memory: drop the start once matched.
                            del starts[e["session"]]
                    else:
                        unmatched_closes += 1
                elif eid == "cowrie.login.success":
                    login_success += 1
                    usernames[e.get("username", "?")] += 1
                    passwords[e.get("password", "?")] += 1
                elif eid == "cowrie.login.failed":
                    login_failed += 1
                    usernames[e.get("username", "?")] += 1
                    passwords[e.get("password", "?")] += 1
                elif eid == "cowrie.command.input":
                    cmd_events += 1
                    commands[e.get("input", "?")] += 1
                    cmdcat[cmd_category(e.get("input", ""))] += 1
                elif eid == "cowrie.command.failed":
                    cmd_failed += 1
                elif eid == "cowrie.session.file_download":
                    downloads += 1
                    if e.get("destfile"):
                        destfiles[e["destfile"]] += 1
                    if e.get("shasum"):
                        shasums[e["shasum"]] += 1
                elif eid == "cowrie.session.file_download.failed":
                    downloads_failed += 1
                elif eid == "cowrie.session.file_upload":
                    uploads += 1
        # file_lines = valid JSON lines per file; sum(file_lines) == total.
        # Malformed lines are counted globally in bad_json_lines.
        file_lines[os.path.basename(path)] = n

    durations_sorted = sorted(durations)
    dur_stats = {
        "n_closed_matched": len(durations),
        "median": _median(durations_sorted),
        "max": max(durations) if durations else 0,
        "under_10s": sum(1 for d in durations if d < 10),
        "unmatched_closes": unmatched_closes,
    }

    payload = {
        "collected_at_utc": datetime.datetime.now(
            datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "totals": {"total_events": total, "bad_json_lines": bad},
        "sources": {
            "unique_source_ips": len(srcips),
            "ipv6_events": ipv6_events,
            "top_source_net16_by_event_volume": [
                {"cidr": k, "events": v}
                for k, v in net16.most_common(8)
            ],
        },
        "sessions": {
            "unique_session_ids": len(sessions),
            "session_connect_events": connects,
            "session_duration_seconds": dur_stats,
        },
        "protocols": dict(protocols),
        "logins": {
            "success_fake": login_success,
            "failed": login_failed,
            "top_usernames": [{"value": k, "count": v}
                              for k, v in usernames.most_common(10)],
            "top_passwords": [{"value": k, "count": v}
                              for k, v in passwords.most_common(10)],
        },
        "commands": {
            "input_events": cmd_events,
            "failed_command_events": cmd_failed,
            # No length filter here: truncation is a render concern so
            # counts in metrics.json always reconcile with input_events.
            "top_commands": [{"input": k, "count": v}
                             for k, v in commands.most_common(10)],
        },
        "behavioral_command_categories": dict(cmdcat),
        "downloads_uploads": {
            "file_download_events": downloads,
            "file_download_failed_events": downloads_failed,
            "file_upload_events": uploads,
            "top_destfiles": [{"value": k, "count": v}
                              for k, v in destfiles.most_common(5)],
            "top_shasums": [{"value": k, "count": v}
                            for k, v in shasums.most_common(3)],
        },
        "event_ids": dict(eventids),
        "collection": {
            "files": len(files),
            "file_lines": file_lines,
            "file_open_errors": file_open_errors,
            "per_day_utc": dict(sorted(per_day.items())),
        },
    }
    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())
