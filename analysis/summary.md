# Analysis summary (rolling snapshot, cutoff 2026-11-13T05:34:59Z)

Sensor is **still running**: this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-11-13T05:34:59Z` (3,784,967 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (79 files, 40 malformed lines): the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 3,784,967 |
| Unique source IPs | 8,943 |
| Sessions (`cowrie.session.connect`) | 491,905 |
| SSH events | 3,784,967 (100%) |
| Fake successful logins (`cowrie.login.success`) | 445,053 |
| Failed logins | 1,456 |
| Command-input events | 373,853 (+12,703 `command.failed`) |
| File-download events | 2,634 |
| File-upload events | 1,844 |
| Session duration median (n=491,649 matched close) | 2.3s; 448,261 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-11-04` | 46,309 |
| `2026-11-05` | 43,784 |
| `2026-11-06` | 39,883 |
| `2026-11-07` | 84,179 |
| `2026-11-08` | 150,290 |
| `2026-11-09` | 137,366 |
| `2026-11-10` | 144,307 |
| `2026-11-11` | 113,159 |
| `2026-11-12` | 82,265 |
| `2026-11-13` | 38,111 |

<details>
<summary>Older days (49 days, click to expand)</summary>

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
| `2026-10-06` | 48,627 |
| `2026-10-07` | 43,716 |
| `2026-10-08` | 64,154 |
| `2026-10-09` | 57,818 |
| `2026-10-10` | 28,596 |
| `2026-10-11` | 32,615 |
| `2026-10-12` | 36,781 |
| `2026-10-13` | 57,072 |
| `2026-10-14` | 98,898 |

</details>

`2026-11-13` is partial at cutoff: do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 173,414 |
| 2 | `ubuntu` | 50,234 |
| 3 | `admin` | 32,108 |
| 4 | `user` | 17,453 |
| 5 | `y2unix` | 13,216 |
| 6 | `deploy` | 3,159 |
| 7 | `test` | 2,509 |
| 8 | `345gs5662d34` | 2,075 |
| 9 | `user1` | 1,671 |
| 10 | `claude` | 1,468 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 11,134 |
| 2 | `123` | 5,766 |
| 3 | `1234` | 5,438 |
| 4 | `12345678` | 3,116 |
| 5 | `1` | 2,674 |
| 6 | `admin` | 2,469 |
| 7 | `root` | 2,393 |
| 8 | `password` | 2,344 |
| 9 | `12345` | 2,342 |
| 10 | `345gs5662d34` | 2,075 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 213,954 |
| 2 | `echo -e "\x6F\x6B"` | 11,273 |
| 3 | `hostname` | 5,552 |
| 4 | `echo xsec` | 4,398 |
| 5 | `uname -a` | 4,016 |
| 6 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 3,672 |
| 7 | `whoami` | 3,194 |
| 8 | `/bin/./uname -s -v -n -r -m` | 2,970 |
| 9 | `pwd` | 2,629 |
| 10 | `cd ~; chattr -ia .ssh; lockr -ia .ssh` | 2,571 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 7,012 |
| `discovery` | 245,399 |
| `downloader` | 88 |
| `empty` | 9 |
| `other` | 35,597 |
| `persistence-privilege` | 3,256 |
| `shell-exec` | 82,492 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
