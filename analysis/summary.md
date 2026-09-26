# Analysis summary (rolling snapshot, cutoff 2026-09-26T03:58:50Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-26T03:58:50Z` (533,302 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (31 files, 3 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 533,302 |
| Unique source IPs | 3,875 |
| Sessions (`cowrie.session.connect`) | 79,869 |
| SSH events | 533,302 (100%) |
| Fake successful logins (`cowrie.login.success`) | 59,872 |
| Failed logins | 375 |
| Command-input events | 56,451 (+269 `command.failed`) |
| File-download events | 236 |
| File-upload events | 59 |
| Session duration median (n=79,653 matched close) | 2.3s; 62,061 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-09-26` | 9,495 |

<details>
<summary>Older days (1 days, click to expand)</summary>

| Day (UTC) | Events |
|---|---|
| `2026-08-27` | 964 |

</details>

`2026-09-26` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 27,039 |
| 2 | `admin` | 2,197 |
| 3 | `ubuntu` | 1,535 |
| 4 | `user` | 1,419 |
| 5 | `deploy` | 851 |
| 6 | `test` | 702 |
| 7 | `user1` | 423 |
| 8 | `claude` | 395 |
| 9 | `debian` | 356 |
| 10 | `postgres` | 301 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 3,214 |
| 2 | `1234` | 1,651 |
| 3 | `123` | 1,534 |
| 4 | `admin` | 860 |
| 5 | `12345678` | 847 |
| 6 | `1` | 774 |
| 7 | `password` | 677 |
| 8 | `root` | 635 |
| 9 | `12345` | 616 |
| 10 | `123456789` | 501 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 45,562 |
| 2 | `hostname` | 1,588 |
| 3 | `/bin/./uname -s -v -n -r -m` | 1,104 |
| 4 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 993 |
| 5 | `uname -a` | 859 |
| 6 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 7 | `whoami` | 694 |
| 8 | `pwd` | 550 |
| 9 | `ls -la /` | 522 |
| 10 | `ps aux \| head -10` | 470 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 1,957 |
| `discovery` | 53,284 |
| `downloader` | 26 |
| `empty` | 4 |
| `other` | 609 |
| `persistence-privilege` | 17 |
| `shell-exec` | 554 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
