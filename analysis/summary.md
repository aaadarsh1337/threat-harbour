# Analysis summary (rolling snapshot, cutoff 2026-10-14T03:56:33Z)

Sensor is **still running** — this file regenerates every 24 hours.
Observation: `2026-08-27` → `ongoing`. Numbers below are a snapshot at
`2026-10-14T03:56:33Z` (1,164,728 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (49 files, 10 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: `scripts/parse_remote.py` (stdlib only, deployed fresh each run);
  renderer: `scripts/render.py`. Aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 1,164,728 |
| Unique source IPs | 5,938 |
| Sessions (`cowrie.session.connect`) | 164,449 |
| SSH events | 1,164,728 (100%) |
| Fake successful logins (`cowrie.login.success`) | 136,478 |
| Failed logins | 658 |
| Command-input events | 116,039 (+921 `command.failed`) |
| File-download events | 881 |
| File-upload events | 120 |
| Session duration median (n=164,228 matched close) | 2.3s; 138,408 < 10s; max ~18,022s |

## Events per UTC day

| Day (UTC) | Events |
|---|---|
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
| `2026-10-05` | 24,281 |
| `2026-10-06` | 48,627 |
| `2026-10-07` | 43,716 |
| `2026-10-08` | 64,154 |
| `2026-10-09` | 57,818 |
| `2026-10-10` | 28,596 |
| `2026-10-11` | 32,615 |
| `2026-10-12` | 36,781 |
| `2026-10-13` | 57,072 |
| `2026-10-14` | 12,861 |

<details>
<summary>Older days (19 days, click to expand)</summary>

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

</details>

`2026-10-14` is partial at cutoff — do not annualize.

### Top usernames

| # | Value | Tries |
|---|---|---|
| 1 | `root` | 45,357 |
| 2 | `ubuntu` | 6,910 |
| 3 | `admin` | 5,056 |
| 4 | `user` | 2,776 |
| 5 | `deploy` | 1,253 |
| 6 | `test` | 1,059 |
| 7 | `345gs5662d34` | 731 |
| 8 | `user1` | 644 |
| 9 | `claude` | 577 |
| 10 | `debian` | 538 |

### Top passwords

| # | Value | Tries |
|---|---|---|
| 1 | `123456` | 4,625 |
| 2 | `1234` | 2,680 |
| 3 | `123` | 2,278 |
| 4 | `admin` | 1,616 |
| 5 | `12345678` | 1,290 |
| 6 | `1` | 1,132 |
| 7 | `password` | 1,022 |
| 8 | `12345` | 976 |
| 9 | `root` | 934 |
| 10 | `123456789` | 773 |

### Top commands

| # | Value | Tries |
|---|---|---|
| 1 | `uname -s -v -n -r -m` | 98,884 |
| 2 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 2,506 |
| 3 | `/bin/./uname -s -v -n -r -m` | 1,981 |
| 4 | `hostname` | 1,912 |
| 5 | `uname -a` | 1,128 |
| 6 | `whoami` | 912 |
| 7 | `cd ~; chattr -ia .ssh; lockr -ia .ssh` | 781 |
| 8 | `cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3Nza…` | 758 |
| 9 | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bi…` | 722 |
| 10 | `pwd` | 703 |

### Command categories

| Category | Events |
|---|---|
| `destructive` | 4,090 |
| `discovery` | 109,473 |
| `downloader` | 46 |
| `empty` | 7 |
| `other` | 1,356 |
| `persistence-privilege` | 56 |
| `shell-exec` | 1,011 |

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
