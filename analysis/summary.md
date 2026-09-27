# Analysis summary (rolling snapshot, cutoff 2026-09-27T04:09:58Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-27T04:09:58Z` (582,100 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (32 files, 3 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 582,100 |
| Unique source IPs | 3,949 |
| Sessions (`cowrie.session.connect`) | 86,122 |
| SSH events | 582,100 (100%) |
| Fake successful logins (`cowrie.login.success`) | 65,927 |
| Failed logins | 398 |
| Command-input events | 62,293 (+274 `command.failed`) |
| File-download events | 240 |
| File-upload events | 63 |
| Session duration median (n=85,905 matched close) | 2.4s; 67,472 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-09-27` | 16,242 |

<details>
<summary>Older days (2 days, click to expand)</summary>

| Day (UTC) | Events |
|---|---|
| `2026-08-27` | 964 |
| `2026-08-28` | 15,483 |

</details>

`2026-09-27` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 29,315 |
| 2 | `admin` | 2,400 |
| 3 | `ubuntu` | 1,740 |
| 4 | `user` | 1,569 |
| 5 | `deploy` | 966 |
| 6 | `test` | 785 |
| 7 | `user1` | 483 |
| 8 | `claude` | 446 |
| 9 | `debian` | 401 |
| 10 | `postgres` | 346 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 3,593 |
| 2 | `1234` | 1,830 |
| 3 | `123` | 1,727 |
| 4 | `12345678` | 953 |
| 5 | `admin` | 926 |
| 6 | `1` | 865 |
| 7 | `password` | 751 |
| 8 | `root` | 707 |
| 9 | `12345` | 686 |
| 10 | `123456789` | 556 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 51,016 |
| 2 | `hostname` | 1,598 |
| 3 | `/bin/./uname -s -v -n -r -m` | 1,267 |
| 4 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 1,094 |
| 5 | `uname -a` | 871 |
| 6 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 7 | `whoami` | 701 |
| 8 | `pwd` | 560 |
| 9 | `ls -la /` | 529 |
| 10 | `ps aux \| head -10` | 481 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 2,062 |
| `discovery` | 58,995 |
| `downloader` | 28 |
| `empty` | 4 |
| `other` | 619 |
| `persistence-privilege` | 17 |
| `shell-exec` | 568 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
