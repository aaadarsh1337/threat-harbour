# Analysis summary (rolling snapshot, cutoff 2026-10-06T05:21:44Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-06T05:21:44Z` (796,007 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (41 files, 6 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 796,007 |
| Unique source IPs | 5,054 |
| Sessions (`cowrie.session.connect`) | 115,406 |
| SSH events | 796,007 (100%) |
| Fake successful logins (`cowrie.login.success`) | 91,613 |
| Failed logins | 496 |
| Command-input events | 86,027 (+619 `command.failed`) |
| File-download events | 577 |
| File-upload events | 95 |
| Session duration median (n=115,186 matched close) | 2.4s; 92,709 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-09-20` | 13,791 |
| `2026-09-21` | 40,240 |
| `2026-09-22` | 24,315 |
| `2026-09-23` | 30,768 |
| `2026-09-24` | 9,616 |
| `2026-09-25` | 20,230 |
| `2026-09-26` | 42,051 |
| `2026-09-27` | 37,899 |
| `2026-09-28` | 30,603 |
| `2026-09-29` | 11,381 |
| `2026-09-30` | 3,990 |
| `2026-10-01` | 2,353 |
| `2026-10-02` | 18,424 |
| `2026-10-03` | 41,555 |
| `2026-10-04` | 46,144 |
| `2026-10-05` | 24,281 |
| `2026-10-06` | 13,519 |

<details>
<summary>Older days (11 days, click to expand)</summary>

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

</details>

`2026-10-06` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 34,899 |
| 2 | `admin` | 3,048 |
| 3 | `ubuntu` | 2,058 |
| 4 | `user` | 1,928 |
| 5 | `deploy` | 1,140 |
| 6 | `test` | 931 |
| 7 | `user1` | 576 |
| 8 | `claude` | 526 |
| 9 | `debian` | 474 |
| 10 | `345gs5662d34` | 472 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 4,188 |
| 2 | `1234` | 2,251 |
| 3 | `123` | 2,029 |
| 4 | `admin` | 1,239 |
| 5 | `12345678` | 1,125 |
| 6 | `1` | 1,017 |
| 7 | `password` | 895 |
| 8 | `root` | 839 |
| 9 | `12345` | 826 |
| 10 | `123456789` | 667 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 72,424 |
| 2 | `hostname` | 1,690 |
| 3 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 1,664 |
| 4 | `/bin/./uname -s -v -n -r -m` | 1,366 |
| 5 | `uname -a` | 945 |
| 6 | `whoami` | 751 |
| 7 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 8 | `pwd` | 605 |
| 9 | `ls -la /` | 574 |
| 10 | `ps aux \| head -10` | 531 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 2,950 |
| `discovery` | 81,137 |
| `downloader` | 37 |
| `empty` | 7 |
| `other` | 970 |
| `persistence-privilege` | 35 |
| `shell-exec` | 891 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
