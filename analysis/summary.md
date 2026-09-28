# Analysis summary (rolling snapshot, cutoff 2026-09-28T04:11:14Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-28T04:11:14Z` (604,540 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (33 files, 4 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 604,540 |
| Unique source IPs | 4,084 |
| Sessions (`cowrie.session.connect`) | 89,083 |
| SSH events | 604,540 (100%) |
| Fake successful logins (`cowrie.login.success`) | 68,693 |
| Failed logins | 409 |
| Command-input events | 64,776 (+341 `command.failed`) |
| File-download events | 308 |
| File-upload events | 66 |
| Session duration median (n=88,866 matched close) | 2.3s; 70,347 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-09-28` | 783 |

<details>
<summary>Older days (3 days, click to expand)</summary>

| Day (UTC) | Events |
|---|---|
| `2026-08-27` | 964 |
| `2026-08-28` | 15,483 |
| `2026-08-29` | 17,457 |

</details>

`2026-09-28` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 30,390 |
| 2 | `admin` | 2,523 |
| 3 | `ubuntu` | 1,820 |
| 4 | `user` | 1,650 |
| 5 | `deploy` | 1,012 |
| 6 | `test` | 820 |
| 7 | `user1` | 507 |
| 8 | `claude` | 467 |
| 9 | `debian` | 422 |
| 10 | `postgres` | 368 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 3,749 |
| 2 | `1234` | 1,919 |
| 3 | `123` | 1,799 |
| 4 | `12345678` | 994 |
| 5 | `admin` | 986 |
| 6 | `1` | 901 |
| 7 | `password` | 785 |
| 8 | `root` | 739 |
| 9 | `12345` | 715 |
| 10 | `123456789` | 579 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 53,222 |
| 2 | `hostname` | 1,613 |
| 3 | `/bin/./uname -s -v -n -r -m` | 1,267 |
| 4 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 1,116 |
| 5 | `uname -a` | 884 |
| 6 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 7 | `whoami` | 709 |
| 8 | `pwd` | 567 |
| 9 | `ls -la /` | 535 |
| 10 | `ps aux \| head -10` | 489 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 2,150 |
| `discovery` | 61,303 |
| `downloader` | 30 |
| `empty` | 7 |
| `other` | 688 |
| `persistence-privilege` | 20 |
| `shell-exec` | 578 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
