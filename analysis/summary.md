# Analysis summary (rolling snapshot, cutoff 2026-10-17T03:25:48Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-17T03:25:48Z` (1,454,626 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (52 files, 13 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 1,454,626 |
| Unique source IPs | 6,238 |
| Sessions (`cowrie.session.connect`) | 202,329 |
| SSH events | 1,454,626 (100%) |
| Fake successful logins (`cowrie.login.success`) | 171,929 |
| Failed logins | 685 |
| Command-input events | 130,758 (+1,090 `command.failed`) |
| File-download events | 1,026 |
| File-upload events | 137 |
| Session duration median (n=202,102 matched close) | 2.3s; 174,557 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-15` | 70,616 |
| `2026-10-16` | 111,562 |
| `2026-10-17` | 21,683 |

<details>
<summary>Older days (22 days, click to expand)</summary>

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

</details>

`2026-10-17` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 56,979 |
| 2 | `admin` | 10,927 |
| 3 | `ubuntu` | 10,517 |
| 4 | `user` | 6,016 |
| 5 | `deploy` | 1,301 |
| 6 | `test` | 1,096 |
| 7 | `345gs5662d34` | 858 |
| 8 | `user1` | 676 |
| 9 | `claude` | 598 |
| 10 | `debian` | 561 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 4,814 |
| 2 | `1234` | 2,780 |
| 3 | `123` | 2,380 |
| 4 | `admin` | 1,677 |
| 5 | `12345678` | 1,353 |
| 6 | `1` | 1,182 |
| 7 | `password` | 1,067 |
| 8 | `12345` | 1,020 |
| 9 | `root` | 969 |
| 10 | `345gs5662d34` | 858 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 109,410 |
| 2 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 2,787 |
| 3 | `echo xsec` | 2,717 |
| 4 | `/bin/./uname -s -v -n -r -m` | 2,068 |
| 5 | `hostname` | 2,065 |
| 6 | `uname -a` | 1,270 |
| 7 | `whoami` | 1,020 |
| 8 | `cd ~; chattr -ia .ssh; lockr -ia .ssh` | 930 |
| 9 | `cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3Nza…` | 895 |
| 10 | `pwd` | 781 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 4,521 |
| `discovery` | 120,989 |
| `downloader` | 54 |
| `empty` | 7 |
| `other` | 1,579 |
| `persistence-privilege` | 58 |
| `shell-exec` | 3,550 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
