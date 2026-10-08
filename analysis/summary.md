# Analysis summary (rolling snapshot, cutoff 2026-10-08T04:59:26Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-08T04:59:26Z` (891,753 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (43 files, 7 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 891,753 |
| Unique source IPs | 5,338 |
| Sessions (`cowrie.session.connect`) | 128,151 |
| SSH events | 891,753 (100%) |
| Fake successful logins (`cowrie.login.success`) | 103,236 |
| Failed logins | 589 |
| Command-input events | 94,724 (+701 `command.failed`) |
| File-download events | 665 |
| File-upload events | 96 |
| Session duration median (n=127,932 matched close) | 2.3s; 104,675 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-08` | 16,922 |

<details>
<summary>Older days (13 days, click to expand)</summary>

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

</details>

`2026-10-08` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 37,702 |
| 2 | `ubuntu` | 3,290 |
| 3 | `admin` | 3,289 |
| 4 | `user` | 2,049 |
| 5 | `deploy` | 1,187 |
| 6 | `test` | 983 |
| 7 | `user1` | 603 |
| 8 | `claude` | 551 |
| 9 | `345gs5662d34` | 547 |
| 10 | `debian` | 499 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 4,377 |
| 2 | `1234` | 2,388 |
| 3 | `123` | 2,133 |
| 4 | `admin` | 1,329 |
| 5 | `12345678` | 1,188 |
| 6 | `1` | 1,062 |
| 7 | `password` | 958 |
| 8 | `root` | 884 |
| 9 | `12345` | 878 |
| 10 | `123456789` | 706 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 80,215 |
| 2 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 1,955 |
| 3 | `hostname` | 1,716 |
| 4 | `/bin/./uname -s -v -n -r -m` | 1,624 |
| 5 | `uname -a` | 957 |
| 6 | `whoami` | 783 |
| 7 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 8 | `pwd` | 616 |
| 9 | `ls -la /` | 584 |
| 10 | `cd ~; chattr -ia .ssh; lockr -ia .ssh` | 581 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 3,324 |
| `discovery` | 89,334 |
| `downloader` | 37 |
| `empty` | 7 |
| `other` | 1,062 |
| `persistence-privilege` | 38 |
| `shell-exec` | 922 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
