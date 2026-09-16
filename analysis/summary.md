# Analysis summary (rolling snapshot, cutoff 2026-09-15T19:41:52Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-15T19:41:52Z` (263,759 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (20 files, 1 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 263,759 |
| Unique source IPs | 2,943 |
| Sessions (`cowrie.session.connect`) | 42,973 |
| SSH events | 263,759 (100%) |
| Fake successful logins (`cowrie.login.success`) | 27,787 |
| Failed logins | 191 |
| Command-input events | 25,633 (+190 `command.failed`) |
| File-download events | 163 |
| File-upload events | 33 |
| Session duration median (n=42,720 matched close) | 2.4s; 30,075 < 10s; max ~18,022s |

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
| `2026-09-15` | 1,553 |

`2026-09-15` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 13,293 |
| 2 | `admin` | 1,043 |
| 3 | `user` | 541 |
| 4 | `ubuntu` | 495 |
| 5 | `test` | 260 |
| 6 | `deploy` | 254 |
| 7 | `avelychko` | 213 |
| 8 | `hongb` | 199 |
| 9 | `vyos` | 191 |
| 10 | `dell` | 187 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 1,300 |
| 2 | `1234` | 675 |
| 3 | `123` | 588 |
| 4 | `admin` | 423 |
| 5 | `12345678` | 349 |
| 6 | `1` | 288 |
| 7 | `12345` | 286 |
| 8 | `password` | 285 |
| 9 | `root` | 260 |
| 10 | `123456789` | 216 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 18,641 |
| 2 | `hostname` | 1,140 |
| 3 | `/bin/./uname -s -v -n -r -m` | 715 |
| 4 | `uname -a` | 516 |
| 5 | `whoami` | 426 |
| 6 | `pwd` | 337 |
| 7 | `ls -la /` | 312 |
| 8 | `history | tail -5` | 282 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 18 |
| `discovery` | 23,569 |
| `downloader` | 6 |
| `empty` | 4 |
| `other` | 638 |
| `persistence-privilege` | 4 |
| `shell-exec` | 1,394 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `../dashboard/README.md`.
