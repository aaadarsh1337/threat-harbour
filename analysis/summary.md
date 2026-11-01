# Analysis summary (rolling snapshot, cutoff 2026-11-01T04:54:31Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-11-01T04:54:31Z` (2,737,314 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (67 files, 29 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 2,737,314 |
| Unique source IPs | 7,958 |
| Sessions (`cowrie.session.connect`) | 363,912 |
| SSH events | 2,737,314 (100%) |
| Fake successful logins (`cowrie.login.success`) | 325,720 |
| Failed logins | 1,105 |
| Command-input events | 245,417 (+5,261 `command.failed`) |
| File-download events | 2,136 |
| File-upload events | 882 |
| Session duration median (n=363,676 matched close) | 2.3s; 330,527 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-27` | 109,420 |
| `2026-10-28` | 89,074 |
| `2026-10-29` | 94,134 |
| `2026-10-30` | 56,113 |
| `2026-10-31` | 29,881 |
| `2026-11-01` | 11,108 |

<details>
<summary>Older days (37 days, click to expand)</summary>

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
| `2026-09-28` | 30,603 |
| `2026-09-29` | 11,381 |
| `2026-09-30` | 3,990 |
| `2026-10-01` | 2,353 |
| `2026-10-02` | 18,424 |

</details>

`2026-11-01` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 121,785 |
| 2 | `ubuntu` | 36,054 |
| 3 | `admin` | 18,997 |
| 4 | `user` | 13,806 |
| 5 | `y2unix` | 12,353 |
| 6 | `deploy` | 2,122 |
| 7 | `345gs5662d34` | 1,907 |
| 8 | `test` | 1,717 |
| 9 | `user1` | 1,103 |
| 10 | `claude` | 987 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 7,664 |
| 2 | `1234` | 3,984 |
| 3 | `123` | 3,909 |
| 4 | `12345678` | 2,156 |
| 5 | `admin` | 2,064 |
| 6 | `345gs5662d34` | 1,907 |
| 7 | `3245gs5662d34` | 1,887 |
| 8 | `1` | 1,853 |
| 9 | `password` | 1,647 |
| 10 | `12345` | 1,620 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 159,504 |
| 2 | `echo -e "\x6F\x6B"` | 10,574 |
| 3 | `hostname` | 5,326 |
| 4 | `uname -a` | 3,835 |
| 5 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 3,672 |
| 6 | `whoami` | 3,019 |
| 7 | `echo xsec` | 2,717 |
| 8 | `/bin/./uname -s -v -n -r -m` | 2,509 |
| 9 | `pwd` | 2,501 |
| 10 | `ls -la /` | 2,176 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 6,514 |
| `discovery` | 189,127 |
| `downloader` | 88 |
| `empty` | 8 |
| `other` | 13,243 |
| `persistence-privilege` | 1,453 |
| `shell-exec` | 34,984 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
