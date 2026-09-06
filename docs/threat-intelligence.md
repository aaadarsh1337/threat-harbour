# Threat Intelligence (interim, cutoff 2026-09-06 UTC)

> Sensor is still running. Observation: `2026-08-27` → `ongoing`.
> Figures below frozen at `2026-09-06T20:36:00Z`. See `analysis/summary.md`
> and `analysis/metrics.json` for method.

## Scope

One Cowrie `3.0.13` sensor (SSH).
No external scanning was performed.

## Data sources

- Cowrie JSON logs (`/home/jack/honeypot/var/log/cowrie/cowrie.json*`)
- Session metadata + host log continuity (daily files, no gaps)
- Collector: Promtail → Loki (`job="cowrie"`); dashboard: Grafana `10.2.3`
- Enrichment: none (counts and /16 volume buckets only; no GeoIP claims)

## Metrics (cutoff)

- Total events: **87,059**
- Unique source IPs: **1,876**
- Sessions: **17,102** (`cowrie.session.connect`)
- Login attempts: **7,485** (7,404 fake-success + 81 failed)
- Commands: **6,521** input events (+67 failed)
- Download attempts: **66** (+5 uploads)
- Top targeted accounts: `root` (3,311), `admin` (342), `user` (230),
  `ubuntu` (191), `test` (138)
- Top passwords: `123456` (461), `1234` (234), `123` (230), `12345678`
  (130), `admin` (117)
- Top commands: `uname -s -v -n -r -m` (4,692), `hostname` (249),
  `uname -a` (151), `whoami` (122), `pwd` (101)
- Top command categories: discovery 5,946 · shell-exec 352 · other 213 ·
  destructive 5 · persistence-privilege 3 · downloader 2

## Behavioral categories observed

- Scanning / connect-only sessions: majority (17,102 connects vs 6,521
  command sessions; median session 8.4s, ~52% under 10s).
- Credential guessing: trivial username/password lists above.
- Interactive shell use + discovery: `uname/hostname/whoami/ls/ps/uptime`
  fingerprinting; two long recon one-liners (180 + 72 hits) probing
  arch/CPU/GPU/shell-filter behavior.
- Persistence attempts: repeated writes toward `authorized_keys`
  (see IoCs). No evidence of host compromise — these stayed inside Cowrie.
- Downloader behavior: minimal (2 `wget/curl`-class commands; download
  events carry null URL — SFTP-style writes, not HTTP fetches).
- Miner indicators: none observed. Destructive: 5 events (no impact).

## Attribution language

Use: “observed from a source associated with this session” and
“consistent with automated scanning”. Never “attacker from `<COUNTRY>`”.

> Source volume bucketed to `<PREFIX>` (e.g. `91.92.0.0/16`); this does
> not establish the identity, physical location, or intent of the operator.

## Indicators (redacted, cutoff)

| Type | Value | First observed | Last observed | Confidence | Notes |
|---|---|---|---|---|---|
| Hash (SHA-256) | `a8460f44…f8f2` (full hash in `analysis/metrics.json`) | 2026-09-06 | 2026-09-06 | Moderate | Repeated `authorized_keys` write payload; content not published |
| Path pattern | `/root/.ssh/authorized_keys` via Cowrie file-write | 2026-09-06 | 2026-09-06 | High | Directly observed `destfile`; persistence-attempt behavior |
| Path variant | `/home/vishnu/.ssh/authorized_keys` | 2026-09-06 | 2026-09-06 | High | Same hash, non-root target |
| Credential pattern | `root / 123456`-class pairs | 2026-08-28 | 2026-09-06 | High | Top username+password across window |
| Recon pattern | `uname -s -v -n -r -m` + long `export PATH=…` one-liners | 2026-08-28 | 2026-09-06 | Moderate | Bot fingerprinting, consistent across sessions |

Raw IPs, URLs with null value, and payload bytes are withheld. Volume
context: `91.92.0.0/16` 36,956 events · `139.59.0.0/16` 9,577 ·
`138.68.0.0/16` 6,205 (per /16, not attribution).

## Confidence

- High: directly observed with multiple event fields (counts, destfile).
- Moderate: consistent behavioral repetition (recon one-liners, hash reuse).
- Low: anything requiring operator identity, location, or intent — not claimed.

## Findings

1. Unsolicited SSH volume is scanner-dominated: 1,876 sources produced
   17,102 sessions but only ~38% reached command input; evidence:
   connects vs `command.input` counts + 8.4s median duration.
2. Credential guessing is commodity-list driven (`root` + numeric
   passwords); evidence: top-10 username/password tables in
   `analysis/metrics.json`.
3. Post-login behavior is discovery/persistence-probing, contained by
   Cowrie; evidence: 91% discovery commands + `authorized_keys` writes
   with no host-compromise indicators (see `docs/incident-response.md`).
   Limitation: SSH-only, single sensor, interim cutoff with a 09-06
   partial-day spike — do not generalize.

## Limitations

Sensor-specific; reflects Cowrie emulation, single-region placement, IP
reputation, and the interim window. No attacker attribution is made.
