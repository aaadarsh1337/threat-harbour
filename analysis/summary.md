# Analysis summary (rolling snapshot, cutoff 2026-10-26T03:42:32Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-26T03:42:32Z` (2,284,707 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (61 files, 20 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 2,284,707 |
| Unique source IPs | 7,212 |
| Sessions (`cowrie.session.connect`) | 309,611 |
| SSH events | 2,284,707 (100%) |
| Fake successful logins (`cowrie.login.success`) | 272,664 |
| Failed logins | 923 |
| Command-input events | 183,792 (+2,258 `command.failed`) |
| File-download events | 1,521 |
| File-upload events | 321 |
| Session duration median (n=309,379 matched close) | 2.3s; 277,796 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-20` | 82,218 |
| `2026-10-21` | 99,039 |
| `2026-10-22` | 85,522 |
| `2026-10-23` | 94,483 |
| `2026-10-24` | 93,187 |
| `2026-10-25` | 96,986 |
| `2026-10-26` | 12,440 |

<details>
<summary>Older days (31 days, click to expand)</summary>

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

</details>

`2026-10-26` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 92,674 |
| 2 | `ubuntu` | 31,536 |
| 3 | `admin` | 18,156 |
| 4 | `user` | 13,361 |
| 5 | `y2unix` | 7,333 |
| 6 | `deploy` | 1,740 |
| 7 | `test` | 1,423 |
| 8 | `345gs5662d34` | 1,315 |
| 9 | `user1` | 906 |
| 10 | `claude` | 809 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 6,310 |
| 2 | `1234` | 3,448 |
| 3 | `123` | 3,201 |
| 4 | `admin` | 1,890 |
| 5 | `12345678` | 1,788 |
| 6 | `1` | 1,550 |
| 7 | `password` | 1,382 |
| 8 | `12345` | 1,359 |
| 9 | `root` | 1,316 |
| 10 | `345gs5662d34` | 1,315 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 139,922 |
| 2 | `hostname` | 4,343 |
| 3 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 3,672 |
| 4 | `uname -a` | 3,053 |
| 5 | `echo xsec` | 2,717 |
| 6 | `whoami` | 2,399 |
| 7 | `/bin/./uname -s -v -n -r -m` | 2,180 |
| 8 | `pwd` | 1,984 |
| 9 | `ls -la /` | 1,757 |
| 10 | `ps aux \| head -10` | 1,674 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 5,901 |
| `discovery` | 163,839 |
| `downloader` | 70 |
| `empty` | 8 |
| `other` | 4,904 |
| `persistence-privilege` | 364 |
| `shell-exec` | 8,706 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
