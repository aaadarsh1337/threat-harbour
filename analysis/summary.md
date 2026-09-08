# Analysis summary (rolling snapshot, cutoff 2026-09-08T19:08:28Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-08T19:08:28Z` (174,927 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (13 files, 0 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 174,927 |
| Unique source IPs | 2,112 |
| Sessions (`cowrie.session.connect`) | 28,501 |
| SSH events | 174,927 (100%) |
| Fake successful logins (`cowrie.login.success`) | 18,343 |
| Failed logins | 138 |
| Command-input events | 16,931 (+109 `command.failed`) |
| File-download events | 101 |
| File-upload events | 12 |
| Session duration median (n=28,401 matched close) | 2.3s; 20,055 < 10s; max ~9,614s |

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
| `2026-09-08` | 42,402 |

`2026-09-08` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 9,801 |
| 2 | `admin` | 761 |
| 3 | `user` | 446 |
| 4 | `ubuntu` | 415 |
| 5 | `deploy` | 248 |
| 6 | `test` | 242 |
| 7 | `user1` | 139 |
| 8 | `debian` | 127 |
| 9 | `claude` | 124 |
| 10 | `support` | 108 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 960 |
| 2 | `1234` | 470 |
| 3 | `123` | 465 |
| 4 | `12345678` | 271 |
| 5 | `admin` | 259 |
| 6 | `password` | 223 |
| 7 | `root` | 206 |
| 8 | `1` | 204 |
| 9 | `12345` | 167 |
| 10 | `123456789` | 149 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 12,396 |
| 2 | `hostname` | 722 |
| 3 | `uname -a` | 356 |
| 4 | `/bin/./uname -s -v -n -r -m` | 336 |
| 5 | `whoami` | 315 |
| 6 | `pwd` | 259 |
| 7 | `ls -la /` | 220 |
| 8 | `history | tail -5` | 205 |
| 9 | `netstat -tulpn | head -10` | 201 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 8 |
| `discovery` | 15,679 |
| `downloader` | 4 |
| `empty` | 4 |
| `other` | 424 |
| `persistence-privilege` | 3 |
| `shell-exec` | 809 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `../dashboard/README.md`.
