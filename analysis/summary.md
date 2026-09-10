# Analysis summary (rolling snapshot, cutoff 2026-09-10T03:29:38Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-10T03:29:38Z` (205,285 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (15 files, 0 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 205,285 |
| Unique source IPs | 2,272 |
| Sessions (`cowrie.session.connect`) | 32,605 |
| SSH events | 205,285 (100%) |
| Fake successful logins (`cowrie.login.success`) | 22,077 |
| Failed logins | 162 |
| Command-input events | 20,314 (+144 `command.failed`) |
| File-download events | 128 |
| File-upload events | 27 |
| Session duration median (n=32,505 matched close) | 2.3s; 23,997 < 10s; max ~9,614s |

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
| `2026-09-10` | 4,808 |

`2026-09-10` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 10,998 |
| 2 | `admin` | 918 |
| 3 | `user` | 498 |
| 4 | `ubuntu` | 444 |
| 5 | `test` | 252 |
| 6 | `deploy` | 251 |
| 7 | `avelychko` | 213 |
| 8 | `dell` | 187 |
| 9 | `user1` | 141 |
| 10 | `debian` | 138 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 1,129 |
| 2 | `1234` | 587 |
| 3 | `123` | 535 |
| 4 | `admin` | 355 |
| 5 | `12345678` | 307 |
| 6 | `password` | 256 |
| 7 | `1` | 252 |
| 8 | `12345` | 243 |
| 9 | `root` | 238 |
| 10 | `123456789` | 184 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 14,592 |
| 2 | `hostname` | 992 |
| 3 | `uname -a` | 438 |
| 4 | `/bin/./uname -s -v -n -r -m` | 434 |
| 5 | `whoami` | 375 |
| 6 | `pwd` | 293 |
| 7 | `ls -la /` | 258 |
| 8 | `history | tail -5` | 248 |
| 9 | `netstat -tulpn | head -10` | 235 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 12 |
| `discovery` | 18,658 |
| `downloader` | 6 |
| `empty` | 4 |
| `other` | 520 |
| `persistence-privilege` | 4 |
| `shell-exec` | 1,110 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `../dashboard/README.md`.
