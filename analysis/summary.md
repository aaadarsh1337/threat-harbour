# Analysis summary (rolling snapshot, cutoff 2026-09-23T03:45:14Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-23T03:45:14Z` (463,643 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (28 files, 3 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 463,643 |
| Unique source IPs | 3,713 |
| Sessions (`cowrie.session.connect`) | 70,583 |
| SSH events | 463,643 (100%) |
| Fake successful logins (`cowrie.login.success`) | 51,405 |
| Failed logins | 294 |
| Command-input events | 48,362 (+263 `command.failed`) |
| File-download events | 230 |
| File-upload events | 56 |
| Session duration median (n=70,373 matched close) | 2.4s; 53,660 < 10s; max ~18,022s |

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
| `2026-09-23` | 450 |

`2026-09-23` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 23,005 |
| 2 | `admin` | 1,883 |
| 3 | `ubuntu` | 1,305 |
| 4 | `user` | 1,224 |
| 5 | `deploy` | 710 |
| 6 | `test` | 606 |
| 7 | `user1` | 350 |
| 8 | `claude` | 334 |
| 9 | `debian` | 303 |
| 10 | `postgres` | 247 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 2,757 |
| 2 | `1234` | 1,418 |
| 3 | `123` | 1,304 |
| 4 | `admin` | 762 |
| 5 | `12345678` | 727 |
| 6 | `1` | 660 |
| 7 | `password` | 585 |
| 8 | `root` | 543 |
| 9 | `12345` | 533 |
| 10 | `123456789` | 432 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 38,937 |
| 2 | `hostname` | 1,396 |
| 3 | `/bin/./uname -s -v -n -r -m` | 1,069 |
| 4 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 752 |
| 5 | `uname -a` | 724 |
| 6 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 7 | `whoami` | 578 |
| 8 | `pwd` | 456 |
| 9 | `ls -la /` | 429 |
| 10 | `netstat -tulpn \| head -10` | 389 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 1,711 |
| `discovery` | 45,583 |
| `downloader` | 24 |
| `empty` | 4 |
| `other` | 542 |
| `persistence-privilege` | 17 |
| `shell-exec` | 481 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
