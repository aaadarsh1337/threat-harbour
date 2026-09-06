# Evidence manifest (interim, cutoff 2026-09-06)

Raw Cowrie logs are **retained on the sensor only** and are not published.
This manifest lets a reviewer re-derive `analysis/metrics.json`.

## Dataset

- Host path: `/home/jack/honeypot/var/log/cowrie/cowrie.json*` (11 files)
- Total lines: 87,059 (`cowrie.json` 18,362 + 10 rotated dailies; see
  `analysis/metrics.json` per-day counts). Zero malformed JSON lines at
  cutoff.
- Files present at cutoff:
  `cowrie.json`, `cowrie.json.2026-08-27` … `cowrie.json.2026-09-05`
- Cowrie: `3.0.13` (venv `/home/jack/honeypot/cowrie-env`)
- Collector: Promtail `2.9.4` → Loki `2.9.4` (`job="cowrie"`), Grafana `10.2.3`

## What is / is not in this repo

- IN REPO: aggregates (`analysis/`), redacted hashes/destfile patterns,
  /16 volume buckets, top username/password/command strings (these are
  attacker guesses, not sensitive).
- NOT IN REPO: raw `cowrie.json*`, raw source IPs, payload contents,
  host keys, SSH private keys, OCI identifiers, sensor public IP.

## Re-derivation

```bash
# on sensor (read-only)
sudo wc -l /home/jack/honeypot/var/log/cowrie/cowrie.json*
# parse with Python json per line, group by eventid / src_ip / session,
# bucket timestamp by UTC day -> compare to analysis/metrics.json
```

## Health / continuity

- Daily files exist for every day 2026-08-27 → 2026-09-06 (no missing days).
- Uptime percentage is not claimed; continuity statement above is the
  evidence. Formalize with host health records before any final close-out.
