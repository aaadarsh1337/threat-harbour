# Analysis summary (rolling snapshot, cutoff 2026-10-09T05:02:24Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-09T05:02:24Z` (945,371 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (44 files, 8 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 945,371 |
| Unique source IPs | 5,424 |
| Sessions (`cowrie.session.connect`) | 135,062 |
| SSH events | 945,371 (100%) |
| Fake successful logins (`cowrie.login.success`) | 109,874 |
| Failed logins | 603 |
| Command-input events | 97,914 (+731 `command.failed`) |
| File-download events | 695 |
| File-upload events | 107 |
| Session duration median (n=134,843 matched close) | 2.3s; 111,469 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-09` | 6,386 |

<details>
<summary>Older days (14 days, click to expand)</summary>

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

</details>

`2026-10-09` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 39,623 |
| 2 | `ubuntu` | 4,788 |
| 3 | `admin` | 3,369 |
| 4 | `user` | 2,098 |
| 5 | `deploy` | 1,188 |
| 6 | `test` | 986 |
| 7 | `user1` | 606 |
| 8 | `345gs5662d34` | 574 |
| 9 | `claude` | 553 |
| 10 | `debian` | 500 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 4,384 |
| 2 | `1234` | 2,423 |
| 3 | `123` | 2,138 |
| 4 | `admin` | 1,371 |
| 5 | `12345678` | 1,192 |
| 6 | `1` | 1,067 |
| 7 | `password` | 961 |
| 8 | `root` | 887 |
| 9 | `12345` | 885 |
| 10 | `123456789` | 710 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 83,215 |
| 2 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 1,989 |
| 3 | `hostname` | 1,726 |
| 4 | `/bin/./uname -s -v -n -r -m` | 1,626 |
| 5 | `uname -a` | 975 |
| 6 | `whoami` | 791 |
| 7 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 8 | `pwd` | 622 |
| 9 | `cd ~; chattr -ia .ssh; lockr -ia .ssh` | 611 |
| 10 | `cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3Nza…` | 591 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 3,388 |
| `discovery` | 92,413 |
| `downloader` | 37 |
| `empty` | 7 |
| `other` | 1,101 |
| `persistence-privilege` | 42 |
| `shell-exec` | 926 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
