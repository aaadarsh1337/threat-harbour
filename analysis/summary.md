# Analysis summary (rolling snapshot, cutoff 2026-10-27T04:06:41Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-27T04:06:41Z` (2,363,924 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (62 files, 21 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 2,363,924 |
| Unique source IPs | 7,355 |
| Sessions (`cowrie.session.connect`) | 319,245 |
| SSH events | 2,363,924 (100%) |
| Fake successful logins (`cowrie.login.success`) | 282,028 |
| Failed logins | 934 |
| Command-input events | 192,174 (+2,684 `command.failed`) |
| File-download events | 1,613 |
| File-upload events | 399 |
| Session duration median (n=319,013 matched close) | 2.3s; 287,228 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-26` | 75,317 |
| `2026-10-27` | 16,340 |

<details>
<summary>Older days (32 days, click to expand)</summary>

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

</details>

`2026-10-27` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 96,630 |
| 2 | `ubuntu` | 33,296 |
| 3 | `admin` | 18,300 |
| 4 | `user` | 13,447 |
| 5 | `y2unix` | 8,404 |
| 6 | `deploy` | 1,809 |
| 7 | `test` | 1,482 |
| 8 | `345gs5662d34` | 1,404 |
| 9 | `user1` | 942 |
| 10 | `claude` | 842 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 6,541 |
| 2 | `1234` | 3,540 |
| 3 | `123` | 3,326 |
| 4 | `admin` | 1,912 |
| 5 | `12345678` | 1,854 |
| 6 | `1` | 1,606 |
| 7 | `password` | 1,429 |
| 8 | `345gs5662d34` | 1,404 |
| 9 | `12345` | 1,404 |
| 10 | `3245gs5662d34` | 1,381 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 143,507 |
| 2 | `hostname` | 4,511 |
| 3 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 3,672 |
| 4 | `uname -a` | 3,204 |
| 5 | `echo xsec` | 2,717 |
| 6 | `whoami` | 2,509 |
| 7 | `/bin/./uname -s -v -n -r -m` | 2,300 |
| 8 | `pwd` | 2,096 |
| 9 | `ls -la /` | 1,833 |
| 10 | `ps aux \| head -10` | 1,761 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 5,993 |
| `discovery` | 168,543 |
| `downloader` | 70 |
| `empty` | 8 |
| `other` | 6,106 |
| `persistence-privilege` | 520 |
| `shell-exec` | 10,934 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
