# Analysis summary (interim, cutoff 2026-09-06 UTC)

Sensor is **still running**. This is an interim analysis, not a closed study.
Observation: `2026-08-27` → `ongoing`. Numbers below are frozen at
`2026-09-06T20:36:00Z` (87,059 events).

## Source

- Cowrie JSONL on sensor: `/home/jack/honeypot/var/log/cowrie/cowrie.json*`
  (11 files, 0 malformed lines) — the same files Promtail ships to Loki
  (`job="cowrie"`).
- Parser: Python `json` per-line; aggregates only. Raw logs stay on the
  sensor. No raw source IPs, payloads, or keys are published.
- Reproduce: parse all `cowrie.json*`, group by `eventid`, count distinct
  `src_ip` / `session`, bucket `timestamp` by UTC day.

## Headline metrics

| Metric | Value |
|---|---|
| Total events | 87,059 |
| Unique source IPs | 1,876 |
| Sessions (`cowrie.session.connect`) | 17,102 |
| SSH events | 87,059 (100%) |
| Fake successful logins (`cowrie.login.success`) | 7,404 |
| Failed logins | 81 |
| Command-input events | 6,521 (+67 `command.failed`) |
| File-download events | 66 |
| File-upload events | 5 |
| Session duration median (n=17,003 matched close) | 8.4s; 8,853 < 10s; max ~9,614s |

Per-day UTC: 08-27: 964 · 08-28: 15,483 · 08-29: 17,457 · 08-30: 6,980 ·
08-31: 6,317 · 09-01: 3,941 · 09-02: 4,684 · 09-03: 4,970 · 09-04: 4,309 ·
09-05: 3,592 · 09-06: 18,362 (partial day at cutoff, single-day spike).

## What actors did

- **Credential guessing:** `root` (3,311) dominates usernames, then
  `admin`/`user`/`ubuntu`/`test`/`deploy`. Passwords are trivial numeric
  sequences (`123456`, `1234`, `123`, `12345678`) plus `admin`/`password`.
  Cowrie permits the fake login, so `login.success` ≫ `login.failed`.
- **Discovery-heavy shell use:** 5,946/6,521 commands classify as discovery
  (`uname`, `hostname`, `whoami`, `ls`, `ps`, `uptime`, `history`). Top
  command `uname -s -v -n -r -m` (4,692) is bot fingerprinting, not human
  typing. Two long `export PATH=...` reconnaissance one-liners (180 + 72
  occurrences) probe CPU/arch/GPU/shell-filter behavior.
- **Persistence attempts:** repeated `file_download` events writing to
  `/root/.ssh/authorized_keys` (and one `/home/vishnu/...` variant) with a
  repeated SHA-256 (`a8460f44…`). URL field is null in these events —
  Cowrie recorded an SFTP-style write, not an HTTP fetch. Content is not
  published.
- **Concentration:** top /16 by event volume (`91.92.0.0/16`: 36,956 events)
  shows a small number of scanners produce most volume. Published only as
  /16 aggregates — a source IP does not establish identity, location, or
  intent.

## Limitations that shape these numbers

- One SSH-only sensor, one region.
- Cowrie emulation + Free Tier resource limits bias what is recorded.
- 2026-09-06 is a partial-day spike; do not annualize it.
- Geo/attribution claims are out of scope (see `docs/limitations.md`).

Full tables: `metrics.json`. Loki equivalents in `dashboard/README.md`.
