# Threat Intelligence (analyst deep-dive, cutoff 2026-09-08 UTC)

> Sensor is still running. Observation: `2026-08-27` → `ongoing`.
> Figures below are a snapshot at `2026-09-08T19:08:28Z`. See `analysis/summary.md`
> and `analysis/metrics.json` for method.
>
> Live leaderboard: the README refreshes every 24 hours — this report is
> the analyst deep-dive behind the numbers.

## Scope

One Cowrie `3.0.13` sensor (SSH).
No external scanning was performed.

## Data sources

- Cowrie JSON logs (`/home/jack/honeypot/var/log/cowrie/cowrie.json*`)
- Session metadata + host log continuity (daily files, no gaps)
- Collector: Promtail → Loki (`job="cowrie"`); dashboard: Grafana `10.2.3`
- Enrichment: none (counts and /16 volume buckets only; no GeoIP claims)

## Metrics (cutoff)

- Total events: **174,927**
- Unique source IPs: **2,112**
- Sessions: **28,501** (`cowrie.session.connect`)
- Login attempts: **18,481** (18,343 fake-success + 138 failed)
- Commands: **16,931** input events (+109 failed)
- Download attempts: **101** (+12 uploads)
- Top targeted accounts: `root` (9,801), `admin` (761), `user` (446),
  `ubuntu` (415), `deploy` (248)
- Top passwords: `123456` (960), `1234` (470), `123` (465), `12345678`
  (271), `admin` (259)
- Top commands: `uname -s -v -n -r -m` (12,396), `hostname` (722),
  `uname -a` (356), `whoami` (315), `pwd` (259)
- Top command categories: discovery 15,679 · shell-exec 809 · other 424 ·
  destructive 8 · downloader 4 · persistence-privilege 3

## Behavioral categories observed

- Scanning / connect-only sessions: large share (28,501 connects vs 16,931
  command sessions; median session 2.3s, ~71% under 10s).
- Credential guessing: trivial username/password lists above.
- Interactive shell use + discovery: `uname/hostname/whoami/ls/ps/uptime`
  fingerprinting, plus recurring long recon one-liners probing
  arch/CPU/GPU/shell-filter behavior.
- Persistence attempts: repeated writes toward `authorized_keys`
  (see IoCs). No evidence of host compromise — these stayed inside Cowrie.
- Downloader behavior: minimal (4 `wget/curl`-class commands; most download
  events carry null URL — SFTP-style writes, not HTTP fetches).
- Miner indicators: none observed. Destructive: 8 events (no impact).

## Attribution language

Use: “observed from a source associated with this session” and
“consistent with automated scanning”. Never “attacker from `<COUNTRY>`”.

> Source volume bucketed to `<PREFIX>` (e.g. `109.160.0.0/16`); this does
> not establish the identity, physical location, or intent of the operator.

## Indicators (redacted, cutoff)

| Type | Value | First observed | Last observed | Confidence | Notes |
|---|---|---|---|---|---|
| Hash (SHA-256) | `a8460f44…f8f2` (full hash in `analysis/metrics.json`) | 2026-09-06 | 2026-09-08 | Moderate | Repeated `authorized_keys` write payload (89 events); content not published |
| Path pattern | `/root/.ssh/authorized_keys` via Cowrie file-write | 2026-09-06 | 2026-09-08 | High | Directly observed `destfile`; persistence-attempt behavior |
| Path variant | `/home/ubuntu/.ssh/authorized_keys` | 2026-09-08 | 2026-09-08 | High | Same campaign, non-root target |
| Credential pattern | `root / 123456`-class pairs | 2026-08-28 | 2026-09-08 | High | Top username+password across window |
| Recon pattern | `uname -s -v -n -r -m` + long recon one-liners | 2026-08-28 | 2026-09-08 | Moderate | Bot fingerprinting, consistent across sessions |

Raw IPs, URLs with null value, and payload bytes are withheld. Volume
context: `109.160.0.0/16` 62,784 events · `91.92.0.0/16` 36,956 ·
`139.59.0.0/16` 13,049 (per /16, not attribution).

## Confidence

- High: directly observed with multiple event fields (counts, destfile).
- Moderate: consistent behavioral repetition (recon one-liners, hash reuse).
- Low: anything requiring operator identity, location, or intent — not claimed.

## Findings

1. Unsolicited SSH volume is scanner-dominated: 2,112 sources produced
   28,501 sessions and ~59% reached command input; evidence:
   connects vs `command.input` counts + 2.3s median duration.
2. Credential guessing is commodity-list driven (`root` + numeric
   passwords); evidence: top-10 username/password tables in
   `analysis/metrics.json`.
3. Post-login behavior is discovery/persistence-probing, contained by
   Cowrie; evidence: 93% discovery commands + `authorized_keys` writes
   with no host-compromise indicators (see `docs/incident-response.md`).
   Limitation: single sensor with partial-day volume spikes — do not generalize.

## Limitations

Sensor-specific; reflects Cowrie emulation, single-region placement, IP
reputation, and the rolling window. No attacker attribution is made.
