# Analysis summary (rolling snapshot, cutoff 2026-09-20T03:52:34Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-20T03:52:34Z` (394,916 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (25 files, 3 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 394,916 |
| Unique source IPs | 3,423 |
| Sessions (`cowrie.session.connect`) | 60,801 |
| SSH events | 394,916 (100%) |
| Fake successful logins (`cowrie.login.success`) | 43,476 |
| Failed logins | 267 |
| Command-input events | 40,711 (+263 `command.failed`) |
| File-download events | 224 |
| File-upload events | 48 |
| Session duration median (n=60,593 matched close) | 2.4s; 45,584 < 10s; max ~18,022s |

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
| `2026-09-20` | 10,069 |

`2026-09-20` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 19,562 |
| 2 | `admin` | 1,635 |
| 3 | `ubuntu` | 1,063 |
| 4 | `user` | 1,027 |
| 5 | `deploy` | 572 |
| 6 | `test` | 509 |
| 7 | `user1` | 278 |
| 8 | `claude` | 274 |
| 9 | `debian` | 255 |
| 10 | `avelychko` | 213 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 2,299 |
| 2 | `1234` | 1,191 |
| 3 | `123` | 1,075 |
| 4 | `admin` | 672 |
| 5 | `12345678` | 604 |
| 6 | `1` | 549 |
| 7 | `password` | 493 |
| 8 | `root` | 453 |
| 9 | `12345` | 445 |
| 10 | `123456789` | 364 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 32,361 |
| 2 | `hostname` | 1,263 |
| 3 | `/bin/./uname -s -v -n -r -m` | 945 |
| 4 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 5 | `uname -a` | 617 |
| 6 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 601 |
| 7 | `whoami` | 490 |
| 8 | `pwd` | 387 |
| 9 | `ls -la /` | 375 |
| 10 | `ps aux \| head -10` | 333 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 1,557 |
| `discovery` | 38,183 |
| `downloader` | 24 |
| `empty` | 4 |
| `other` | 507 |
| `persistence-privilege` | 17 |
| `shell-exec` | 419 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
