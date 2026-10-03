# Analysis summary (rolling snapshot, cutoff 2026-10-03T04:14:14Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-03T04:14:14Z` (683,446 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (38 files, 5 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 683,446 |
| Unique source IPs | 4,684 |
| Sessions (`cowrie.session.connect`) | 100,541 |
| SSH events | 683,446 (100%) |
| Fake successful logins (`cowrie.login.success`) | 77,787 |
| Failed logins | 435 |
| Command-input events | 73,298 (+454 `command.failed`) |
| File-download events | 434 |
| File-upload events | 78 |
| Session duration median (n=100,322 matched close) | 2.4s; 79,176 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-03` | 12,938 |

<details>
<summary>Older days (8 days, click to expand)</summary>

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

</details>

`2026-10-03` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 32,941 |
| 2 | `admin` | 2,802 |
| 3 | `ubuntu` | 1,988 |
| 4 | `user` | 1,812 |
| 5 | `deploy` | 1,108 |
| 6 | `test` | 889 |
| 7 | `user1` | 559 |
| 8 | `claude` | 509 |
| 9 | `debian` | 456 |
| 10 | `postgres` | 407 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 4,074 |
| 2 | `1234` | 2,122 |
| 3 | `123` | 1,961 |
| 4 | `admin` | 1,117 |
| 5 | `12345678` | 1,082 |
| 6 | `1` | 982 |
| 7 | `password` | 855 |
| 8 | `root` | 807 |
| 9 | `12345` | 786 |
| 10 | `123456789` | 633 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 60,828 |
| 2 | `hostname` | 1,659 |
| 3 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 1,394 |
| 4 | `/bin/./uname -s -v -n -r -m` | 1,329 |
| 5 | `uname -a` | 917 |
| 6 | `whoami` | 727 |
| 7 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 8 | `pwd` | 582 |
| 9 | `ls -la /` | 563 |
| 10 | `ps aux \| head -10` | 514 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 2,545 |
| `discovery` | 69,266 |
| `downloader` | 32 |
| `empty` | 7 |
| `other` | 824 |
| `persistence-privilege` | 28 |
| `shell-exec` | 596 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
