# Analysis summary (rolling snapshot, cutoff 2026-09-11T18:20:09Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-11T18:20:09Z` (247,715 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (16 files, 0 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 247,715 |
| Unique source IPs | 2,476 |
| Sessions (`cowrie.session.connect`) | 38,622 |
| SSH events | 247,715 (100%) |
| Fake successful logins (`cowrie.login.success`) | 27,090 |
| Failed logins | 173 |
| Command-input events | 25,072 (+184 `command.failed`) |
| File-download events | 156 |
| File-upload events | 33 |
| Session duration median (n=38,522 matched close) | 2.3s; 28,890 < 10s; max ~9,614s |

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
| `2026-09-11` | 2,537 |

`2026-09-11` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 12,712 |
| 2 | `admin` | 1,013 |
| 3 | `user` | 529 |
| 4 | `ubuntu` | 490 |
| 5 | `test` | 259 |
| 6 | `deploy` | 254 |
| 7 | `avelychko` | 213 |
| 8 | `hongb` | 199 |
| 9 | `vyos` | 191 |
| 10 | `dell` | 187 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 1,289 |
| 2 | `1234` | 654 |
| 3 | `123` | 578 |
| 4 | `admin` | 404 |
| 5 | `12345678` | 341 |
| 6 | `1` | 286 |
| 7 | `password` | 282 |
| 8 | `12345` | 277 |
| 9 | `root` | 258 |
| 10 | `123456789` | 210 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 18,641 |
| 2 | `hostname` | 1,075 |
| 3 | `/bin/./uname -s -v -n -r -m` | 646 |
| 4 | `uname -a` | 468 |
| 5 | `whoami` | 402 |
| 6 | `pwd` | 314 |
| 7 | `ls -la /` | 280 |
| 8 | `history | tail -5` | 260 |
| 9 | `netstat -tulpn | head -10` | 257 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 18 |
| `discovery` | 23,188 |
| `downloader` | 6 |
| `empty` | 4 |
| `other` | 605 |
| `persistence-privilege` | 4 |
| `shell-exec` | 1,247 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `../dashboard/README.md`.
