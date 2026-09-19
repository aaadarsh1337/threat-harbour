# Evidence manifest (rolling snapshot, cutoff 2026-09-19T03:36:26Z)

Raw Cowrie logs are **retained on the sensor only** and are not published.
This manifest lets a reviewer re-derive `analysis/metrics.json`.

## Dataset

- Host path: `/home/jack/honeypot/var/log/cowrie/cowrie.json*` (24 files)
- Total lines: 357,922 (3 malformed)
- Cowrie: `3.0.13`
- Collector: Promtail `2.9.4` → Loki `2.9.4` (`job="cowrie"`), Grafana `10.2.3`

### Lines per file

| File | Lines |
|---|---|
| `cowrie.json` | 734 |
| `cowrie.json.2026-08-27` | 964 |
| `cowrie.json.2026-08-28` | 15,483 |
| `cowrie.json.2026-08-29` | 17,457 |
| `cowrie.json.2026-08-30` | 6,980 |
| `cowrie.json.2026-08-31` | 6,317 |
| `cowrie.json.2026-09-01` | 3,941 |
| `cowrie.json.2026-09-02` | 4,684 |
| `cowrie.json.2026-09-03` | 4,969 |
| `cowrie.json.2026-09-04` | 4,310 |
| `cowrie.json.2026-09-05` | 3,592 |
| `cowrie.json.2026-09-06` | 24,144 |
| `cowrie.json.2026-09-07` | 39,684 |
| `cowrie.json.2026-09-08` | 44,543 |
| `cowrie.json.2026-09-09` | 23,409 |
| `cowrie.json.2026-09-10` | 44,701 |
| `cowrie.json.2026-09-11` | 3,711 |
| `cowrie.json.2026-09-12` | 3,333 |
| `cowrie.json.2026-09-13` | 6,459 |
| `cowrie.json.2026-09-14` | 3,525 |
| `cowrie.json.2026-09-15` | 2,779 |
| `cowrie.json.2026-09-16` | 62,682 |
| `cowrie.json.2026-09-17` | 26,242 |
| `cowrie.json.2026-09-18` | 3,279 |

## What is / is not in this repo

- IN REPO: aggregates (`analysis/`), redacted hashes/destfile patterns,
  /16 volume buckets, top username/password/command strings (these are
  attacker guesses, not sensitive).
- NOT IN REPO: raw `cowrie.json*`, raw source IPs, payload contents,
  host keys, SSH private keys, OCI identifiers, sensor public IP.

## Re-derivation

Automated daily via `.github/workflows/daily-metrics.yml` (manual trigger:
Actions → daily-metrics → Run workflow). Manual equivalent is documented in
`docs/operations.md`.

## Health / continuity

- Per-day counts in `analysis/metrics.json`; any missing day is flagged by
  the renderer as a collection gap. Uptime percentage is not claimed.
