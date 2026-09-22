# Analysis summary (rolling snapshot, cutoff 2026-09-22T03:46:07Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-22T03:46:07Z` (449,613 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (27 files, 3 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 449,613 |
| Unique source IPs | 3,625 |
| Sessions (`cowrie.session.connect`) | 68,372 |
| SSH events | 449,613 (100%) |
| Fake successful logins (`cowrie.login.success`) | 49,943 |
| Failed logins | 290 |
| Command-input events | 46,951 (+263 `command.failed`) |
| File-download events | 230 |
| File-upload events | 56 |
| Session duration median (n=68,163 matched close) | 2.4s; 52,129 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
| `2026-08-27` | 964 |
| `2026-08-28` | 15,483 |
| `2026-08-29` | 17,457 |
| `2026-08-30` | 6,980 |
| `2026-08-31` | 6,317 |
| `2026-09-01` | 3,941 |
| `2026-09-02` | 4,684 |
| `2026-09-03` | 4,970 |
| `2026-09-04` | 4,309 |
| `2026-09-05` | 3,592 |
| `2026-09-06` | 24,144 |
| `2026-09-07` | 39,684 |
| `2026-09-08` | 44,543 |
| `2026-09-09` | 23,409 |
| `2026-09-10` | 44,701 |
| `2026-09-11` | 3,711 |
| `2026-09-12` | 3,333 |
| `2026-09-13` | 6,459 |
| `2026-09-14` | 3,525 |
| `2026-09-15` | 2,779 |
| `2026-09-16` | 62,682 |
| `2026-09-17` | 26,242 |
| `2026-09-18` | 3,279 |
| `2026-09-19` | 27,659 |
| `2026-09-20` | 13,791 |
| `2026-09-21` | 40,240 |
| `2026-09-22` | 10,735 |

`2026-09-22` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 22,265 |
| 2 | `admin` | 1,846 |
| 3 | `ubuntu` | 1,267 |
| 4 | `user` | 1,192 |
| 5 | `deploy` | 687 |
| 6 | `test` | 590 |
| 7 | `user1` | 338 |
| 8 | `claude` | 324 |
| 9 | `debian` | 295 |
| 10 | `postgres` | 238 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 2,683 |
| 2 | `1234` | 1,380 |
| 3 | `123` | 1,266 |
| 4 | `admin` | 747 |
| 5 | `12345678` | 708 |
| 6 | `1` | 641 |
| 7 | `password` | 570 |
| 8 | `root` | 528 |
| 9 | `12345` | 519 |
| 10 | `123456789` | 421 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 37,841 |
| 2 | `hostname` | 1,335 |
| 3 | `/bin/./uname -s -v -n -r -m` | 1,069 |
| 4 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 743 |
| 5 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 6 | `uname -a` | 680 |
| 7 | `whoami` | 543 |
| 8 | `pwd` | 432 |
| 9 | `ls -la /` | 411 |
| 10 | `netstat -tulpn \| head -10` | 371 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 1,702 |
| `discovery` | 44,214 |
| `downloader` | 24 |
| `empty` | 4 |
| `other` | 525 |
| `persistence-privilege` | 17 |
| `shell-exec` | 465 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
