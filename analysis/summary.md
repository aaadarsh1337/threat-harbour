# Analysis summary (rolling snapshot, cutoff 2026-10-04T04:46:05Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-04T04:46:05Z` (721,245 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (39 files, 6 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 721,245 |
| Unique source IPs | 4,800 |
| Sessions (`cowrie.session.connect`) | 105,497 |
| SSH events | 721,245 (100%) |
| Fake successful logins (`cowrie.login.success`) | 82,471 |
| Failed logins | 451 |
| Command-input events | 77,723 (+492 `command.failed`) |
| File-download events | 472 |
| File-upload events | 90 |
| Session duration median (n=105,278 matched close) | 2.4s; 83,553 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-03` | 41,555 |
| `2026-10-04` | 9,182 |

<details>
<summary>Older days (9 days, click to expand)</summary>

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

</details>

`2026-10-04` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 33,703 |
| 2 | `admin` | 2,888 |
| 3 | `ubuntu` | 2,029 |
| 4 | `user` | 1,865 |
| 5 | `deploy` | 1,133 |
| 6 | `test` | 913 |
| 7 | `user1` | 572 |
| 8 | `claude` | 521 |
| 9 | `debian` | 466 |
| 10 | `postgres` | 417 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 4,166 |
| 2 | `1234` | 2,187 |
| 3 | `123` | 2,009 |
| 4 | `admin` | 1,168 |
| 5 | `12345678` | 1,112 |
| 6 | `1` | 1,005 |
| 7 | `password` | 878 |
| 8 | `root` | 830 |
| 9 | `12345` | 810 |
| 10 | `123456789` | 651 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 64,924 |
| 2 | `hostname` | 1,668 |
| 3 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 1,511 |
| 4 | `/bin/./uname -s -v -n -r -m` | 1,364 |
| 5 | `uname -a` | 924 |
| 6 | `whoami` | 738 |
| 7 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 8 | `pwd` | 591 |
| 9 | `ls -la /` | 568 |
| 10 | `ps aux \| head -10` | 522 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 2,700 |
| `discovery` | 73,480 |
| `downloader` | 34 |
| `empty` | 7 |
| `other` | 862 |
| `persistence-privilege` | 29 |
| `shell-exec` | 611 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
