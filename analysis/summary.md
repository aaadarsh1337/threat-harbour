# Analysis summary (rolling snapshot, cutoff 2026-09-21T03:48:34Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-21T03:48:34Z` (399,041 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (26 files, 3 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 399,041 |
| Unique source IPs | 3,546 |
| Sessions (`cowrie.session.connect`) | 61,851 |
| SSH events | 399,041 (100%) |
| Fake successful logins (`cowrie.login.success`) | 43,667 |
| Failed logins | 271 |
| Command-input events | 40,852 (+263 `command.failed`) |
| File-download events | 228 |
| File-upload events | 55 |
| Session duration median (n=61,642 matched close) | 2.4s; 45,974 < 10s; max ~18,022s |

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
| `2026-09-21` | 403 |

`2026-09-21` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 19,720 |
| 2 | `admin` | 1,653 |
| 3 | `ubuntu` | 1,063 |
| 4 | `user` | 1,040 |
| 5 | `deploy` | 572 |
| 6 | `test` | 510 |
| 7 | `user1` | 278 |
| 8 | `claude` | 274 |
| 9 | `debian` | 255 |
| 10 | `avelychko` | 213 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 2,303 |
| 2 | `1234` | 1,202 |
| 3 | `123` | 1,077 |
| 4 | `admin` | 689 |
| 5 | `12345678` | 606 |
| 6 | `1` | 550 |
| 7 | `password` | 496 |
| 8 | `root` | 454 |
| 9 | `12345` | 451 |
| 10 | `123456789` | 365 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 32,361 |
| 2 | `hostname` | 1,284 |
| 3 | `/bin/./uname -s -v -n -r -m` | 945 |
| 4 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 5 | `uname -a` | 631 |
| 6 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 614 |
| 7 | `whoami` | 497 |
| 8 | `pwd` | 393 |
| 9 | `ls -la /` | 382 |
| 10 | `netstat -tulpn \| head -10` | 342 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 1,572 |
| `discovery` | 38,280 |
| `downloader` | 24 |
| `empty` | 4 |
| `other` | 511 |
| `persistence-privilege` | 17 |
| `shell-exec` | 444 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
