# Analysis summary (rolling snapshot, cutoff 2026-09-19T03:36:26Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-19T03:36:26Z` (357,922 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (24 files, 3 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 357,922 |
| Unique source IPs | 3,302 |
| Sessions (`cowrie.session.connect`) | 55,973 |
| SSH events | 357,922 (100%) |
| Fake successful logins (`cowrie.login.success`) | 38,938 |
| Failed logins | 240 |
| Command-input events | 36,360 (+222 `command.failed`) |
| File-download events | 195 |
| File-upload events | 44 |
| Session duration median (n=55,757 matched close) | 2.4s; 41,259 < 10s; max ~18,022s |

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
| `2026-09-19` | 734 |

`2026-09-19` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 17,586 |
| 2 | `admin` | 1,482 |
| 3 | `ubuntu` | 916 |
| 4 | `user` | 883 |
| 5 | `deploy` | 492 |
| 6 | `test` | 451 |
| 7 | `user1` | 240 |
| 8 | `claude` | 238 |
| 9 | `debian` | 227 |
| 10 | `avelychko` | 213 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 2,037 |
| 2 | `1234` | 1,032 |
| 3 | `123` | 944 |
| 4 | `admin` | 591 |
| 5 | `12345678` | 538 |
| 6 | `1` | 482 |
| 7 | `password` | 441 |
| 8 | `root` | 401 |
| 9 | `12345` | 398 |
| 10 | `123456789` | 325 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 28,737 |
| 2 | `hostname` | 1,185 |
| 3 | `/bin/./uname -s -v -n -r -m` | 856 |
| 4 | `uname -a` | 559 |
| 5 | `whoami` | 452 |
| 6 | `pwd` | 350 |
| 7 | `ls -la /` | 328 |
| 8 | `ps aux | head -10` | 298 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 18 |
| `discovery` | 34,031 |
| `downloader` | 6 |
| `empty` | 4 |
| `other` | 708 |
| `persistence-privilege` | 6 |
| `shell-exec` | 1,587 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `../dashboard/README.md`.
