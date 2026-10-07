# Analysis summary (rolling snapshot, cutoff 2026-10-07T04:48:59Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-07T04:48:59Z` (832,181 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (42 files, 7 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 832,181 |
| Unique source IPs | 5,196 |
| Sessions (`cowrie.session.connect`) | 120,267 |
| SSH events | 832,181 (100%) |
| Fake successful logins (`cowrie.login.success`) | 95,979 |
| Failed logins | 544 |
| Command-input events | 89,781 (+666 `command.failed`) |
| File-download events | 625 |
| File-upload events | 96 |
| Session duration median (n=120,048 matched close) | 2.3s; 97,084 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-06` | 48,627 |
| `2026-10-07` | 1,066 |

<details>
<summary>Older days (12 days, click to expand)</summary>

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

</details>

`2026-10-07` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 35,871 |
| 2 | `admin` | 3,185 |
| 3 | `ubuntu` | 2,281 |
| 4 | `user` | 1,992 |
| 5 | `deploy` | 1,164 |
| 6 | `test` | 965 |
| 7 | `user1` | 588 |
| 8 | `claude` | 536 |
| 9 | `345gs5662d34` | 514 |
| 10 | `debian` | 489 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 4,277 |
| 2 | `1234` | 2,321 |
| 3 | `123` | 2,081 |
| 4 | `admin` | 1,280 |
| 5 | `12345678` | 1,151 |
| 6 | `1` | 1,038 |
| 7 | `password` | 920 |
| 8 | `root` | 860 |
| 9 | `12345` | 850 |
| 10 | `123456789` | 687 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 75,760 |
| 2 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 1,870 |
| 3 | `hostname` | 1,705 |
| 4 | `/bin/./uname -s -v -n -r -m` | 1,366 |
| 5 | `uname -a` | 952 |
| 6 | `whoami` | 767 |
| 7 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 8 | `pwd` | 609 |
| 9 | `ls -la /` | 578 |
| 10 | `cd ~; chattr -ia .ssh; lockr -ia .ssh` | 546 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 3,202 |
| `discovery` | 84,553 |
| `downloader` | 37 |
| `empty` | 7 |
| `other` | 1,026 |
| `persistence-privilege` | 38 |
| `shell-exec` | 918 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
