# Analysis summary (rolling snapshot, cutoff 2026-11-04T05:16:44Z)

Sensor is **still running**: this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-11-04T05:16:44Z` (2,925,425 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (70 files, 32 malformed lines): the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 2,925,425 |
| Unique source IPs | 8,198 |
| Sessions (`cowrie.session.connect`) | 386,257 |
| SSH events | 2,925,425 (100%) |
| Fake successful logins (`cowrie.login.success`) | 347,440 |
| Failed logins | 1,180 |
| Command-input events | 276,519 (+6,702 `command.failed`) |
| File-download events | 2,278 |
| File-upload events | 1,202 |
| Session duration median (n=386,016 matched close) | 2.3s; 351,385 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
| `2026-10-06` | 48,627 |
| `2026-10-07` | 43,716 |
| `2026-10-08` | 64,154 |
| `2026-10-09` | 57,818 |
| `2026-10-10` | 28,596 |
| `2026-10-11` | 32,615 |
| `2026-10-12` | 36,781 |
| `2026-10-13` | 57,072 |
| `2026-10-14` | 98,898 |
| `2026-10-15` | 70,616 |
| `2026-10-16` | 111,562 |
| `2026-10-17` | 98,865 |
| `2026-10-18` | 100,972 |
| `2026-10-19` | 88,052 |
| `2026-10-20` | 82,218 |
| `2026-10-21` | 99,039 |
| `2026-10-22` | 85,522 |
| `2026-10-23` | 94,483 |
| `2026-10-24` | 93,187 |
| `2026-10-25` | 96,986 |
| `2026-10-26` | 75,317 |
| `2026-10-27` | 109,420 |
| `2026-10-28` | 89,074 |
| `2026-10-29` | 94,134 |
| `2026-10-30` | 56,113 |
| `2026-10-31` | 29,881 |
| `2026-11-01` | 39,637 |
| `2026-11-02` | 71,535 |
| `2026-11-03` | 67,936 |
| `2026-11-04` | 20,111 |

<details>
<summary>Older days (40 days, click to expand)</summary>

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

</details>

`2026-11-04` is partial at cutoff: do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 130,765 |
| 2 | `ubuntu` | 36,649 |
| 3 | `admin` | 19,560 |
| 4 | `user` | 14,166 |
| 5 | `y2unix` | 13,186 |
| 6 | `deploy` | 2,445 |
| 7 | `345gs5662d34` | 2,006 |
| 8 | `test` | 1,951 |
| 9 | `user1` | 1,281 |
| 10 | `claude` | 1,143 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 8,746 |
| 2 | `123` | 4,494 |
| 3 | `1234` | 4,433 |
| 4 | `12345678` | 2,452 |
| 5 | `admin` | 2,170 |
| 6 | `1` | 2,113 |
| 7 | `345gs5662d34` | 2,006 |
| 8 | `3245gs5662d34` | 1,987 |
| 9 | `password` | 1,862 |
| 10 | `root` | 1,848 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 176,238 |
| 2 | `echo -e "\x6F\x6B"` | 10,651 |
| 3 | `hostname` | 5,483 |
| 4 | `uname -a` | 3,952 |
| 5 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 3,672 |
| 6 | `whoami` | 3,115 |
| 7 | `echo xsec` | 2,717 |
| 8 | `/bin/./uname -s -v -n -r -m` | 2,649 |
| 9 | `pwd` | 2,587 |
| 10 | `ls -la /` | 2,237 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 6,656 |
| `discovery` | 206,836 |
| `downloader` | 88 |
| `empty` | 8 |
| `other` | 17,369 |
| `persistence-privilege` | 2,051 |
| `shell-exec` | 43,511 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
