# Analysis summary (rolling snapshot, cutoff 2026-09-09T03:31:39Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-09T03:31:39Z` (181,361 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (14 files, 0 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 181,361 |
| Unique source IPs | 2,155 |
| Sessions (`cowrie.session.connect`) | 29,401 |
| SSH events | 181,361 (100%) |
| Fake successful logins (`cowrie.login.success`) | 19,124 |
| Failed logins | 147 |
| Command-input events | 17,627 (+112 `command.failed`) |
| File-download events | 102 |
| File-upload events | 16 |
| Session duration median (n=29,301 matched close) | 2.3s; 20,940 < 10s; max ~9,614s |

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
| `2026-09-09` | 4,293 |

`2026-09-09` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 10,223 |
| 2 | `admin` | 811 |
| 3 | `user` | 463 |
| 4 | `ubuntu` | 429 |
| 5 | `deploy` | 251 |
| 6 | `test` | 248 |
| 7 | `user1` | 141 |
| 8 | `debian` | 127 |
| 9 | `claude` | 125 |
| 10 | `support` | 108 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 1,013 |
| 2 | `1234` | 484 |
| 3 | `123` | 476 |
| 4 | `admin` | 278 |
| 5 | `12345678` | 273 |
| 6 | `password` | 236 |
| 7 | `root` | 209 |
| 8 | `1` | 208 |
| 9 | `12345` | 170 |
| 10 | `123456789` | 150 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 12,641 |
| 2 | `hostname` | 836 |
| 3 | `/bin/./uname -s -v -n -r -m` | 432 |
| 4 | `uname -a` | 383 |
| 5 | `whoami` | 331 |
| 6 | `pwd` | 273 |
| 7 | `ls -la /` | 238 |
| 8 | `history | tail -5` | 220 |
| 9 | `netstat -tulpn | head -10` | 213 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 8 |
| `discovery` | 16,286 |
| `downloader` | 6 |
| `empty` | 4 |
| `other` | 437 |
| `persistence-privilege` | 3 |
| `shell-exec` | 883 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `../dashboard/README.md`.
