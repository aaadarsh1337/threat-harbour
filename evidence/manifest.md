# Evidence manifest (interim, cutoff 2026-09-08T18:57:53Z)

Raw Cowrie logs are **retained on the sensor only** and are not published.
This manifest lets a reviewer re-derive `analysis/metrics.json`.

## Dataset

- Host path: `/home/jack/honeypot/var/log/cowrie/cowrie.json*` (13 files)
- Total lines: 174,877 (0 malformed). Per-file:
  `cowrie.json` (42,352 lines)
  `cowrie.json.2026-08-27` (964 lines)
  `cowrie.json.2026-08-28` (15,483 lines)
  `cowrie.json.2026-08-29` (17,457 lines)
  `cowrie.json.2026-08-30` (6,980 lines)
  `cowrie.json.2026-08-31` (6,317 lines)
  `cowrie.json.2026-09-01` (3,941 lines)
  `cowrie.json.2026-09-02` (4,684 lines)
  `cowrie.json.2026-09-03` (4,969 lines)
  `cowrie.json.2026-09-04` (4,310 lines)
  `cowrie.json.2026-09-05` (3,592 lines)
  `cowrie.json.2026-09-06` (24,144 lines)
  `cowrie.json.2026-09-07` (39,684 lines)
- Cowrie: `3.0.13`
- Collector: Promtail `2.9.4` → Loki `2.9.4` (`job="cowrie"`), Grafana `10.2.3`

## What is / is not in this repo

- IN REPO: aggregates (`analysis/`), redacted hashes/destfile patterns,
  /16 volume buckets, top username/password/command strings (these are
  attacker guesses, not sensitive).
- NOT IN REPO: raw `cowrie.json*`, raw source IPs, payload contents,
  host keys, SSH private keys, OCI identifiers, sensor public IP.

## Re-derivation

```bash
# automated daily: .github/workflows/daily-metrics.yml
# manual equivalent (read-only on sensor):
python3 scripts/render.py <(ssh metrics@<SENSOR> "sudo /usr/bin/python3 ..." )
```

## Health / continuity

- Per-day counts in `analysis/metrics.json`; any missing day is flagged by
  the renderer as a collection gap. Uptime percentage is not claimed.
