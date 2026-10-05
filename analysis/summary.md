# Analysis summary (rolling snapshot, cutoff 2026-10-05T04:34:05Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-05T04:34:05Z` (760,104 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (40 files, 6 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 760,104 |
| Unique source IPs | 4,923 |
| Sessions (`cowrie.session.connect`) | 110,627 |
| SSH events | 760,104 (100%) |
| Fake successful logins (`cowrie.login.success`) | 87,226 |
| Failed logins | 463 |
| Command-input events | 82,084 (+558 `command.failed`) |
| File-download events | 517 |
| File-upload events | 93 |
| Session duration median (n=110,408 matched close) | 2.4s; 88,317 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-05` | 1,897 |

<details>
<summary>Older days (10 days, click to expand)</summary>

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

</details>

`2026-10-05` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 34,259 |
| 2 | `admin` | 2,971 |
| 3 | `ubuntu` | 2,032 |
| 4 | `user` | 1,895 |
| 5 | `deploy` | 1,138 |
| 6 | `test` | 918 |
| 7 | `user1` | 574 |
| 8 | `claude` | 524 |
| 9 | `debian` | 468 |
| 10 | `postgres` | 420 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 4,176 |
| 2 | `1234` | 2,221 |
| 3 | `123` | 2,018 |
| 4 | `admin` | 1,203 |
| 5 | `12345678` | 1,121 |
| 6 | `1` | 1,011 |
| 7 | `password` | 886 |
| 8 | `root` | 836 |
| 9 | `12345` | 817 |
| 10 | `123456789` | 660 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 68,924 |
| 2 | `hostname` | 1,680 |
| 3 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 1,627 |
| 4 | `/bin/./uname -s -v -n -r -m` | 1,366 |
| 5 | `uname -a` | 935 |
| 6 | `whoami` | 743 |
| 7 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 8 | `pwd` | 598 |
| 9 | `ls -la /` | 568 |
| 10 | `ps aux \| head -10` | 525 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 2,853 |
| `discovery` | 77,552 |
| `downloader` | 35 |
| `empty` | 7 |
| `other` | 899 |
| `persistence-privilege` | 30 |
| `shell-exec` | 708 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
