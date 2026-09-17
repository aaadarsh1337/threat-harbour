# Analysis summary (rolling snapshot, cutoff 2026-09-17T03:52:21Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-17T03:52:21Z` (328,523 events).

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
| Total events | 328,523 |
| Unique source IPs | 3,134 |
| Sessions (`cowrie.session.connect`) | 51,592 |
| SSH events | 328,523 (100%) |
| Fake successful logins (`cowrie.login.success`) | 35,652 |
| Failed logins | 224 |
| Command-input events | 33,204 (+214 `command.failed`) |
| File-download events | 186 |
| File-upload events | 43 |
| Session duration median (n=51,389 matched close) | 2.4s; 38,007 < 10s; max ~18,022s |

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
| `2026-09-17` | 856 |

`2026-09-17` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 16,294 |
| 2 | `admin` | 1,327 |
| 3 | `ubuntu` | 798 |
| 4 | `user` | 776 |
| 5 | `deploy` | 423 |
| 6 | `test` | 396 |
| 7 | `avelychko` | 213 |
| 8 | `user1` | 211 |
| 9 | `claude` | 208 |
| 10 | `vyos` | 203 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 1,817 |
| 2 | `1234` | 916 |
| 3 | `123` | 837 |
| 4 | `admin` | 535 |
| 5 | `12345678` | 479 |
| 6 | `1` | 423 |
| 7 | `password` | 393 |
| 8 | `root` | 362 |
| 9 | `12345` | 360 |
| 10 | `123456789` | 290 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 25,790 |
| 2 | `hostname` | 1,171 |
| 3 | `/bin/./uname -s -v -n -r -m` | 856 |
| 4 | `uname -a` | 544 |
| 5 | `whoami` | 443 |
| 6 | `pwd` | 348 |
| 7 | `ls -la /` | 325 |
| 8 | `netstat -tulpn | head -10` | 293 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 18 |
| `discovery` | 31,019 |
| `downloader` | 6 |
| `empty` | 4 |
| `other` | 691 |
| `persistence-privilege` | 6 |
| `shell-exec` | 1,460 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `../dashboard/README.md`.
