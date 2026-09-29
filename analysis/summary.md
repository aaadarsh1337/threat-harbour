# Analysis summary (rolling snapshot, cutoff 2026-09-29T04:44:38Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-09-29T04:44:38Z` (635,657 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (34 files, 5 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 635,657 |
| Unique source IPs | 4,204 |
| Sessions (`cowrie.session.connect`) | 93,187 |
| SSH events | 635,657 (100%) |
| Fake successful logins (`cowrie.login.success`) | 72,547 |
| Failed logins | 419 |
| Command-input events | 68,389 (+389 `command.failed`) |
| File-download events | 362 |
| File-upload events | 69 |
| Session duration median (n=92,970 matched close) | 2.3s; 74,180 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-09-28` | 30,603 |
| `2026-09-29` | 1,297 |

<details>
<summary>Older days (4 days, click to expand)</summary>

| Day (UTC) | Events |
|---|---|
| `2026-08-27` | 964 |
| `2026-08-28` | 15,483 |
| `2026-08-29` | 17,457 |
| `2026-08-30` | 6,980 |

</details>

`2026-09-29` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 31,865 |
| 2 | `admin` | 2,664 |
| 3 | `ubuntu` | 1,941 |
| 4 | `user` | 1,756 |
| 5 | `deploy` | 1,084 |
| 6 | `test` | 870 |
| 7 | `user1` | 543 |
| 8 | `claude` | 496 |
| 9 | `debian` | 447 |
| 10 | `postgres` | 397 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 3,982 |
| 2 | `1234` | 2,045 |
| 3 | `123` | 1,915 |
| 4 | `12345678` | 1,055 |
| 5 | `admin` | 1,037 |
| 6 | `1` | 955 |
| 7 | `password` | 827 |
| 8 | `root` | 784 |
| 9 | `12345` | 755 |
| 10 | `123456789` | 612 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 56,561 |
| 2 | `hostname` | 1,629 |
| 3 | `/bin/./uname -s -v -n -r -m` | 1,299 |
| 4 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 1,173 |
| 5 | `uname -a` | 894 |
| 6 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 7 | `whoami` | 718 |
| 8 | `pwd` | 572 |
| 9 | `ls -la /` | 544 |
| 10 | `ps aux \| head -10` | 497 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 2,258 |
| `discovery` | 64,749 |
| `downloader` | 32 |
| `empty` | 7 |
| `other` | 735 |
| `persistence-privilege` | 20 |
| `shell-exec` | 588 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
