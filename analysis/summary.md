# Analysis summary (rolling snapshot, cutoff 2026-09-18T03:38:54Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-18T03:38:54Z` (353,909 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (22 files, 2 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 353,909 |
| Unique source IPs | 3,178 |
| Sessions (`cowrie.session.connect`) | 54,850 |
| SSH events | 353,909 (100%) |
| Fake successful logins (`cowrie.login.success`) | 38,795 |
| Failed logins | 238 |
| Command-input events | 36,239 (+222 `command.failed`) |
| File-download events | 195 |
| File-upload events | 43 |
| Session duration median (n=54,646 matched close) | 2.4s; 41,104 < 10s; max ~18,022s |

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

`2026-09-17` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 17,508 |
| 2 | `admin` | 1,467 |
| 3 | `ubuntu` | 916 |
| 4 | `user` | 876 |
| 5 | `deploy` | 491 |
| 6 | `test` | 448 |
| 7 | `user1` | 239 |
| 8 | `claude` | 238 |
| 9 | `debian` | 227 |
| 10 | `avelychko` | 213 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 2,028 |
| 2 | `1234` | 1,024 |
| 3 | `123` | 940 |
| 4 | `admin` | 586 |
| 5 | `12345678` | 536 |
| 6 | `1` | 478 |
| 7 | `password` | 440 |
| 8 | `root` | 401 |
| 9 | `12345` | 395 |
| 10 | `123456789` | 323 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 28,654 |
| 2 | `hostname` | 1,185 |
| 3 | `/bin/./uname -s -v -n -r -m` | 856 |
| 4 | `uname -a` | 556 |
| 5 | `whoami` | 450 |
| 6 | `pwd` | 350 |
| 7 | `ls -la /` | 328 |
| 8 | `ps aux | head -10` | 297 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 18 |
| `discovery` | 33,940 |
| `downloader` | 6 |
| `empty` | 4 |
| `other` | 706 |
| `persistence-privilege` | 6 |
| `shell-exec` | 1,559 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `../dashboard/README.md`.
