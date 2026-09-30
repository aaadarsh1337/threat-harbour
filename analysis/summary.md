# Analysis summary (rolling snapshot, cutoff 2026-09-30T04:27:47Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-30T04:27:47Z` (646,004 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (35 files, 5 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 646,004 |
| Unique source IPs | 4,292 |
| Sessions (`cowrie.session.connect`) | 94,744 |
| SSH events | 646,004 (100%) |
| Fake successful logins (`cowrie.login.success`) | 73,686 |
| Failed logins | 421 |
| Command-input events | 69,458 (+392 `command.failed`) |
| File-download events | 365 |
| File-upload events | 77 |
| Session duration median (n=94,527 matched close) | 2.3s; 75,347 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-09-28` | 30,603 |
| `2026-09-29` | 11,381 |
| `2026-09-30` | 263 |

<details>
<summary>Older days (5 days, click to expand)</summary>

| Day (UTC) | Events |
|---|---|
| `2026-08-27` | 964 |
| `2026-08-28` | 15,483 |
| `2026-08-29` | 17,457 |
| `2026-08-30` | 6,980 |
| `2026-08-31` | 6,317 |

</details>

`2026-09-30` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 32,345 |
| 2 | `admin` | 2,698 |
| 3 | `ubuntu` | 1,976 |
| 4 | `user` | 1,782 |
| 5 | `deploy` | 1,104 |
| 6 | `test` | 884 |
| 7 | `user1` | 554 |
| 8 | `claude` | 505 |
| 9 | `debian` | 454 |
| 10 | `postgres` | 405 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 4,046 |
| 2 | `1234` | 2,075 |
| 3 | `123` | 1,947 |
| 4 | `12345678` | 1,071 |
| 5 | `admin` | 1,047 |
| 6 | `1` | 973 |
| 7 | `password` | 841 |
| 8 | `root` | 796 |
| 9 | `12345` | 768 |
| 10 | `123456789` | 622 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 57,565 |
| 2 | `hostname` | 1,639 |
| 3 | `/bin/./uname -s -v -n -r -m` | 1,299 |
| 4 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 1,188 |
| 5 | `uname -a` | 899 |
| 6 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 7 | `whoami` | 721 |
| 8 | `pwd` | 574 |
| 9 | `ls -la /` | 550 |
| 10 | `ps aux \| head -10` | 499 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 2,276 |
| `discovery` | 65,791 |
| `downloader` | 32 |
| `empty` | 7 |
| `other` | 743 |
| `persistence-privilege` | 20 |
| `shell-exec` | 589 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
