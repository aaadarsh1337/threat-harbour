# Analysis summary (rolling snapshot, cutoff 2026-10-20T03:52:25Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-20T03:52:25Z` (1,736,341 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (55 files, 15 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 1,736,341 |
| Unique source IPs | 6,528 |
| Sessions (`cowrie.session.connect`) | 239,342 |
| SSH events | 1,736,341 (100%) |
| Fake successful logins (`cowrie.login.success`) | 206,219 |
| Failed logins | 810 |
| Command-input events | 144,524 (+1,233 `command.failed`) |
| File-download events | 1,143 |
| File-upload events | 159 |
| Session duration median (n=239,115 matched close) | 2.3s; 209,612 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-17` | 98,865 |
| `2026-10-18` | 100,972 |
| `2026-10-19` | 88,052 |
| `2026-10-20` | 15,509 |

<details>
<summary>Older days (25 days, click to expand)</summary>

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

</details>

`2026-10-20` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 69,507 |
| 2 | `ubuntu` | 15,457 |
| 3 | `admin` | 14,914 |
| 4 | `user` | 9,366 |
| 5 | `deploy` | 1,350 |
| 6 | `test` | 1,137 |
| 7 | `345gs5662d34` | 964 |
| 8 | `user1` | 702 |
| 9 | `claude` | 622 |
| 10 | `debian` | 579 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 4,999 |
| 2 | `1234` | 2,885 |
| 3 | `123` | 2,477 |
| 4 | `admin` | 1,730 |
| 5 | `12345678` | 1,421 |
| 6 | `1` | 1,232 |
| 7 | `password` | 1,113 |
| 8 | `12345` | 1,088 |
| 9 | `root` | 1,010 |
| 10 | `345gs5662d34` | 964 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 119,639 |
| 2 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 3,134 |
| 3 | `echo xsec` | 2,717 |
| 4 | `hostname` | 2,535 |
| 5 | `/bin/./uname -s -v -n -r -m` | 2,128 |
| 6 | `uname -a` | 1,622 |
| 7 | `whoami` | 1,309 |
| 8 | `cd ~; chattr -ia .ssh; lockr -ia .ssh` | 1,049 |
| 9 | `pwd` | 1,028 |
| 10 | `cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3Nza…` | 1,008 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 4,994 |
| `discovery` | 133,757 |
| `downloader` | 68 |
| `empty` | 7 |
| `other` | 1,887 |
| `persistence-privilege` | 64 |
| `shell-exec` | 3,747 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
