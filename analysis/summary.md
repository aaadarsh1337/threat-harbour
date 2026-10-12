# Analysis summary (rolling snapshot, cutoff 2026-10-12T04:48:40Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-12T04:48:40Z` (1,063,036 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (47 files, 10 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 1,063,036 |
| Unique source IPs | 5,724 |
| Sessions (`cowrie.session.connect`) | 150,752 |
| SSH events | 1,063,036 (100%) |
| Fake successful logins (`cowrie.login.success`) | 124,176 |
| Failed logins | 637 |
| Command-input events | 108,270 (+847 `command.failed`) |
| File-download events | 813 |
| File-upload events | 113 |
| Session duration median (n=150,529 matched close) | 2.3s; 125,540 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-12` | 5,022 |

<details>
<summary>Older days (17 days, click to expand)</summary>

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

</details>

`2026-10-12` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 43,103 |
| 2 | `ubuntu` | 6,212 |
| 3 | `admin` | 3,747 |
| 4 | `user` | 2,320 |
| 5 | `deploy` | 1,243 |
| 6 | `test` | 1,038 |
| 7 | `345gs5662d34` | 675 |
| 8 | `user1` | 633 |
| 9 | `claude` | 575 |
| 10 | `debian` | 523 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 4,589 |
| 2 | `1234` | 2,599 |
| 3 | `123` | 2,255 |
| 4 | `admin` | 1,507 |
| 5 | `12345678` | 1,262 |
| 6 | `1` | 1,118 |
| 7 | `password` | 1,003 |
| 8 | `12345` | 942 |
| 9 | `root` | 920 |
| 10 | `123456789` | 756 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 92,391 |
| 2 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 2,288 |
| 3 | `/bin/./uname -s -v -n -r -m` | 1,886 |
| 4 | `hostname` | 1,783 |
| 5 | `uname -a` | 1,038 |
| 6 | `whoami` | 829 |
| 7 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 8 | `cd ~; chattr -ia .ssh; lockr -ia .ssh` | 719 |
| 9 | `cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3Nza…` | 697 |
| 10 | `pwd` | 651 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 3,802 |
| `discovery` | 102,183 |
| `downloader` | 41 |
| `empty` | 7 |
| `other` | 1,238 |
| `persistence-privilege` | 51 |
| `shell-exec` | 948 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
