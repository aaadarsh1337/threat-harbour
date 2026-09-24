# Analysis summary (rolling snapshot, cutoff 2026-09-24T03:36:28Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-24T03:36:28Z` (496,133 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (29 files, 3 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 496,133 |
| Unique source IPs | 3,772 |
| Sessions (`cowrie.session.connect`) | 74,794 |
| SSH events | 496,133 (100%) |
| Fake successful logins (`cowrie.login.success`) | 55,450 |
| Failed logins | 329 |
| Command-input events | 52,225 (+263 `command.failed`) |
| File-download events | 234 |
| File-upload events | 56 |
| Session duration median (n=74,583 matched close) | 2.4s; 57,739 < 10s; max ~18,022s |

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
| `2026-09-22` | 24,315 |
| `2026-09-23` | 30,768 |
| `2026-09-24` | 2,172 |

`2026-09-24` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 24,874 |
| 2 | `admin` | 2,033 |
| 3 | `ubuntu` | 1,419 |
| 4 | `user` | 1,318 |
| 5 | `deploy` | 779 |
| 6 | `test` | 654 |
| 7 | `user1` | 386 |
| 8 | `claude` | 364 |
| 9 | `debian` | 327 |
| 10 | `postgres` | 274 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 2,981 |
| 2 | `1234` | 1,531 |
| 3 | `123` | 1,417 |
| 4 | `admin` | 806 |
| 5 | `12345678` | 785 |
| 6 | `1` | 717 |
| 7 | `password` | 630 |
| 8 | `root` | 586 |
| 9 | `12345` | 573 |
| 10 | `123456789` | 466 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 42,225 |
| 2 | `hostname` | 1,478 |
| 3 | `/bin/./uname -s -v -n -r -m` | 1,069 |
| 4 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 826 |
| 5 | `uname -a` | 783 |
| 6 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 7 | `whoami` | 621 |
| 8 | `pwd` | 501 |
| 9 | `ls -la /` | 471 |
| 10 | `netstat -tulpn \| head -10` | 427 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 1,787 |
| `discovery` | 49,319 |
| `downloader` | 24 |
| `empty` | 4 |
| `other` | 569 |
| `persistence-privilege` | 17 |
| `shell-exec` | 505 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
