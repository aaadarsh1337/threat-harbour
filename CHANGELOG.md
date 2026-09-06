# Changelog

## 06-09-2026 (interim analysis, sensor still running)

- Froze interim metrics at `2026-09-06T20:36:00Z`: 87,059 events, 1,876
  source IPs, 17,102 SSH sessions, 7,404 fake logins, 6,521 commands,
  66 downloads (+5 uploads). SSH-only sensor.
- Added `analysis/metrics.json`, `analysis/summary.md`,
  `evidence/manifest.md`
- Filled `docs/threat-intelligence.md` (interim findings, redacted IoCs)
- Completed `docs/deployment.md`, rewrote `docs/operations.md`,
  added incident disposition (no host compromise), finished
  `dashboard/README.md` (tables-only scope)
- Added `diagrams/architecture.png` + `architecture.mmd`; fixed broken
  `dashboards/` link; removed `SECURITY.md` link; clarified no-license
  portfolio status
- Stack pinned: Cowrie `3.0.13`, Grafana `10.2.3`, Loki/Promtail `2.9.4`

## 27-08-2026

- Created the repository
- Deployed the initial Cowrie honeypot
- Added architecture and deployment documentation
