# Analysis summary (interim, cutoff 2026-09-08T18:57:53Z)

Sensor is **still running**. This is an interim analysis, not a closed study.
Observation: `2026-08-27` → `ongoing`. Numbers below are frozen at
`2026-09-08T18:57:53Z` (174,877 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (13 files, 0 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 174,877 |
| Unique source IPs | 2,112 |
| Sessions (`cowrie.session.connect`) | 28,494 |
| SSH events | 174,877 (100%) |
| Fake successful logins (`cowrie.login.success`) | 18,337 |
| Failed logins | 138 |
| Command-input events | 16,926 (+109 `command.failed`) |
| File-download events | 101 |
| File-upload events | 12 |
| Session duration median (n=28,393 matched close) | 2.3s; 20,047 < 10s; max ~9614s |

Per-day UTC: 08-27: 964 · 08-28: 15,483 · 08-29: 17,457 · 08-30: 6,980 · 08-31: 6,317 · 09-01: 3,941 · 09-02: 4,684 · 09-03: 4,970 · 09-04: 4,309 · 09-05: 3,592 · 09-06: 24,144 · 09-07: 39,684 · 09-08: 42,352 (last day partial at cutoff — do not annualize).

Top usernames: `root` (9,795), `admin` (761), `user` (446), `ubuntu` (415), `deploy` (248).
Top passwords: `123456` (960), `1234` (470), `123` (465), `12345678` (271), `admin` (259).
Top commands: `uname -s -v -n -r -m` (12,396), `hostname` (721), `uname -a` (356), `/bin/./uname -s -v -n -r -m` (336), `whoami` (315).
Command categories: destructive 8, discovery 15675, downloader 4, empty 4, other 423, persistence-privilege 3, shell-exec 809.

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
