# Analysis summary (rolling snapshot, cutoff 2026-09-25T03:53:21Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-25T03:53:21Z` (504,014 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (30 files, 3 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 504,014 |
| Unique source IPs | 3,826 |
| Sessions (`cowrie.session.connect`) | 76,101 |
| SSH events | 504,014 (100%) |
| Fake successful logins (`cowrie.login.success`) | 56,232 |
| Failed logins | 344 |
| Command-input events | 52,929 (+268 `command.failed`) |
| File-download events | 236 |
| File-upload events | 58 |
| Session duration median (n=75,886 matched close) | 2.4s; 58,410 < 10s; max ~18,022s |

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
| `2026-09-24` | 9,616 |
| `2026-09-25` | 437 |

`2026-09-25` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 25,586 |
| 2 | `admin` | 2,074 |
| 3 | `ubuntu` | 1,420 |
| 4 | `user` | 1,328 |
| 5 | `deploy` | 781 |
| 6 | `test` | 654 |
| 7 | `user1` | 387 |
| 8 | `claude` | 365 |
| 9 | `debian` | 328 |
| 10 | `postgres` | 274 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 2,987 |
| 2 | `1234` | 1,542 |
| 3 | `123` | 1,423 |
| 4 | `admin` | 823 |
| 5 | `12345678` | 788 |
| 6 | `1` | 719 |
| 7 | `password` | 634 |
| 8 | `root` | 591 |
| 9 | `12345` | 575 |
| 10 | `123456789` | 468 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 42,276 |
| 2 | `hostname` | 1,566 |
| 3 | `/bin/./uname -s -v -n -r -m` | 1,069 |
| 4 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 923 |
| 5 | `uname -a` | 844 |
| 6 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 7 | `whoami` | 687 |
| 8 | `pwd` | 539 |
| 9 | `ls -la /` | 511 |
| 10 | `ps aux \| head -10` | 464 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 1,887 |
| `discovery` | 49,848 |
| `downloader` | 26 |
| `empty` | 4 |
| `other` | 601 |
| `persistence-privilege` | 17 |
| `shell-exec` | 546 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
