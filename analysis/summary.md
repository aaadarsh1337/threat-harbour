# Analysis summary (rolling snapshot, cutoff 2026-09-16T13:24:18Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-16T13:24:18Z` (278,837 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (21 files, 1 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 278,837 |
| Unique source IPs | 3,068 |
| Sessions (`cowrie.session.connect`) | 45,221 |
| SSH events | 278,837 (100%) |
| Fake successful logins (`cowrie.login.success`) | 29,503 |
| Failed logins | 201 |
| Command-input events | 27,220 (+196 `command.failed`) |
| File-download events | 168 |
| File-upload events | 34 |
| Session duration median (n=45,019 matched close) | 2.4s; 32,026 < 10s; max ~18,022s |

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
| `2026-09-16` | 13,852 |

`2026-09-16` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 13,976 |
| 2 | `admin` | 1,110 |
| 3 | `user` | 595 |
| 4 | `ubuntu` | 558 |
| 5 | `deploy` | 288 |
| 6 | `test` | 288 |
| 7 | `avelychko` | 213 |
| 8 | `hongb` | 199 |
| 9 | `vyos` | 194 |
| 10 | `dell` | 187 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 1,406 |
| 2 | `1234` | 731 |
| 3 | `123` | 640 |
| 4 | `admin` | 453 |
| 5 | `12345678` | 375 |
| 6 | `1` | 315 |
| 7 | `password` | 306 |
| 8 | `12345` | 300 |
| 9 | `root` | 284 |
| 10 | `123456789` | 230 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 20,073 |
| 2 | `hostname` | 1,156 |
| 3 | `/bin/./uname -s -v -n -r -m` | 772 |
| 4 | `uname -a` | 527 |
| 5 | `whoami` | 433 |
| 6 | `pwd` | 343 |
| 7 | `ls -la /` | 318 |
| 8 | `netstat -tulpn | head -10` | 287 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 18 |
| `discovery` | 25,133 |
| `downloader` | 6 |
| `empty` | 4 |
| `other` | 652 |
| `persistence-privilege` | 4 |
| `shell-exec` | 1,403 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `../dashboard/README.md`.
