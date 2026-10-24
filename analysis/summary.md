# Analysis summary (rolling snapshot, cutoff 2026-10-24T03:42:42Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-24T03:42:42Z` (2,109,168 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (59 files, 18 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 2,109,168 |
| Unique source IPs | 6,932 |
| Sessions (`cowrie.session.connect`) | 288,106 |
| SSH events | 2,109,168 (100%) |
| Fake successful logins (`cowrie.login.success`) | 251,798 |
| Failed logins | 898 |
| Command-input events | 164,969 (+1,402 `command.failed`) |
| File-download events | 1,312 |
| File-upload events | 169 |
| Session duration median (n=287,875 matched close) | 2.3s; 257,051 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-20` | 82,218 |
| `2026-10-21` | 99,039 |
| `2026-10-22` | 85,522 |
| `2026-10-23` | 94,483 |
| `2026-10-24` | 27,074 |

<details>
<summary>Older days (29 days, click to expand)</summary>

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

</details>

`2026-10-24` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 84,584 |
| 2 | `ubuntu` | 27,231 |
| 3 | `admin` | 17,918 |
| 4 | `user` | 13,251 |
| 5 | `y2unix` | 2,478 |
| 6 | `deploy` | 1,645 |
| 7 | `test` | 1,350 |
| 8 | `345gs5662d34` | 1,119 |
| 9 | `user1` | 857 |
| 10 | `claude` | 764 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 5,982 |
| 2 | `1234` | 3,308 |
| 3 | `123` | 3,026 |
| 4 | `admin` | 1,840 |
| 5 | `12345678` | 1,694 |
| 6 | `1` | 1,470 |
| 7 | `password` | 1,316 |
| 8 | `12345` | 1,288 |
| 9 | `root` | 1,242 |
| 10 | `345gs5662d34` | 1,119 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 134,988 |
| 2 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 3,598 |
| 3 | `hostname` | 3,251 |
| 4 | `echo xsec` | 2,717 |
| 5 | `uname -a` | 2,167 |
| 6 | `/bin/./uname -s -v -n -r -m` | 2,132 |
| 7 | `whoami` | 1,730 |
| 8 | `pwd` | 1,400 |
| 9 | `ls -la /` | 1,246 |
| 10 | `cd ~; chattr -ia .ssh; lockr -ia .ssh` | 1,215 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 5,622 |
| `discovery` | 152,860 |
| `downloader` | 70 |
| `empty` | 7 |
| `other` | 2,307 |
| `persistence-privilege` | 73 |
| `shell-exec` | 4,030 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
