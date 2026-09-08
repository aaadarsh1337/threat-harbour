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
import json
import os
import sys

LOG_GLOB = "/home/jack/honeypot/var/log/cowrie/cowrie.json*"
COWRIE_VERSION_FILE = "/home/jack/honeypot/cowrie-env/lib/python3.12/site-packages/cowrie/__init__.py"


def cmd_category(cmd):
    c = (cmd or "").strip().lower()
    if not c:
        return "empty"
    first = c.split()[0].split("/")[-1].split(";")[0]
    if first in ("uname", "hostname", "whoami", "id", "pwd", "arch"):
        return "discovery"
    if first in ("ls", "cat", "ps", "netstat", "ss", "ifconfig", "ip",
                 "mount", "df", "uptime", "history"):
        return "discovery"
    if first in ("wget", "curl", "tftp", "ftp", "scp", "aria2c"):
        return "downloader"
    if first in ("chmod", "chpasswd", "passwd", "useradd", "adduser",
                 "usermod", "crontab", "systemctl", "service", "iptables"):
        return "persistence-privilege"
    if first in ("rm", "dd", "mkfs", "shutdown", "reboot", "kill", "pkill"):
        return "destructive"
    if "xmrig" in c or "miner" in c:
        return "miner-indicator"
    if first in ("sh", "bash", "python", "python3", "perl", "busybox",
                 "export", "echo", "ssh"):
        return "shell-exec"
    return "other"


def main():
    files = sorted(glob.glob(LOG_GLOB))
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
    uploads = 0
    destfiles = collections.Counter()
    shasums = collections.Counter()
    connects = 0
    per_day = collections.Counter()
    net16 = collections.Counter()
    starts = {}
    durations = []
    file_lines = {}

    for path in files:
        n = 0
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
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
                    if e.get("session"):
                        starts[e["session"]] = ts
                elif eid == "cowrie.session.closed" and e.get("session") in starts:
                    try:
                        t0 = datetime.datetime.fromisoformat(
                            starts[e["session"]].replace("Z", "+00:00"))
                        t1 = datetime.datetime.fromisoformat(
                            ts.replace("Z", "+00:00"))
                        durations.append((t1 - t0).total_seconds())
                    except (ValueError, KeyError):
                        pass
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
                elif eid in ("cowrie.session.file_download",
                             "cowrie.session.file_download.failed"):
                    downloads += 1
                    if e.get("destfile"):
                        destfiles[e["destfile"]] += 1
                    if e.get("shasum"):
                        shasums[e["shasum"]] += 1
                elif eid == "cowrie.session.file_upload":
                    uploads += 1
        file_lines[os.path.basename(path)] = n

    durations_sorted = sorted(durations)
    dur_stats = {
        "n_closed_matched": len(durations),
        "median": (durations_sorted[len(durations_sorted) // 2]
                   if durations_sorted else 0),
        "max": max(durations) if durations else 0,
        "under_10s": sum(1 for d in durations if d < 10),
    }

    payload = {
        "collected_at_utc": datetime.datetime.now(
            datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "totals": {"total_events": total, "bad_json_lines": bad},
        "sources": {
            "unique_source_ips": len(srcips),
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
            "top_commands": [{"input": k, "count": v}
                             for k, v in commands.most_common(10)
                             if len(k) < 120],
        },
        "behavioral_command_categories": dict(cmdcat),
        "downloads_uploads": {
            "file_download_events": downloads,
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
            "per_day_utc": dict(sorted(per_day.items())),
        },
    }
    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())
