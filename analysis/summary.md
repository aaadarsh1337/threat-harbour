# Analysis summary (rolling snapshot, cutoff 2026-11-05T05:37:35Z)

Sensor is **still running**: this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-11-05T05:37:35Z` (2,958,422 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (71 files, 32 malformed lines): the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 2,958,422 |
| Unique source IPs | 8,294 |
| Sessions (`cowrie.session.connect`) | 390,138 |
| SSH events | 2,958,422 (100%) |
| Fake successful logins (`cowrie.login.success`) | 351,079 |
| Failed logins | 1,190 |
| Command-input events | 281,967 (+7,080 `command.failed`) |
| File-download events | 2,312 |
| File-upload events | 1,255 |
| Session duration median (n=389,896 matched close) | 2.3s; 355,085 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-11-04` | 46,309 |
| `2026-11-05` | 6,799 |

<details>
<summary>Older days (41 days, click to expand)</summary>

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

</details>

`2026-11-05` is partial at cutoff: do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 132,845 |
| 2 | `ubuntu` | 36,706 |
| 3 | `admin` | 19,672 |
| 4 | `user` | 14,199 |
| 5 | `y2unix` | 13,209 |
| 6 | `deploy` | 2,471 |
| 7 | `345gs5662d34` | 2,011 |
| 8 | `test` | 1,972 |
| 9 | `user1` | 1,294 |
| 10 | `claude` | 1,156 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 8,854 |
| 2 | `123` | 4,549 |
| 3 | `1234` | 4,482 |
| 4 | `12345678` | 2,495 |
| 5 | `admin` | 2,192 |
| 6 | `1` | 2,136 |
| 7 | `345gs5662d34` | 2,011 |
| 8 | `3245gs5662d34` | 1,993 |
| 9 | `password` | 1,892 |
| 10 | `root` | 1,870 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 177,602 |
| 2 | `echo -e "\x6F\x6B"` | 10,651 |
| 3 | `hostname` | 5,489 |
| 4 | `uname -a` | 3,955 |
| 5 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 3,672 |
| 6 | `whoami` | 3,138 |
| 7 | `/bin/./uname -s -v -n -r -m` | 2,898 |
| 8 | `echo xsec` | 2,717 |
| 9 | `pwd` | 2,589 |
| 10 | `ls -la /` | 2,239 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 6,690 |
| `discovery` | 208,498 |
| `downloader` | 88 |
| `empty` | 9 |
| `other` | 18,701 |
| `persistence-privilege` | 2,144 |
| `shell-exec` | 45,837 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
