# Sensor configs (redacted examples)

Rebuild reference for the single-node sensor described in
`docs/architecture.md` + `docs/deployment.md`. Values match the live sensor;
secrets are replaced with `<PLACEHOLDERS>` — copy, fill in, never commit real
keys, IPs, or OCIDs.

| File | Live path | Purpose |
|---|---|---|
| `cowrie.cfg.example` | `/home/jack/honeypot/etc/cowrie.cfg` | Cowrie `3.0.13` SSH-only honeypot |
| `docker-compose.yml.example` | `/home/jack/honeypot-monitor/docker-compose.yml` | Loki `2.9.4` + Promtail `2.9.4` + Grafana `10.2.3`, localhost-only |
| `promtail-config.yml.example` | (mounted into Promtail container) | Ships `cowrie.json*` as `job="cowrie"` |
| `sudoers.d-metrics-read.example` | `/etc/sudoers.d/metrics-read` | Restricted `metrics` user for the daily job |
| `nsg-rules.md` | OCI console → VCN → Security List / NSG | Public surface: Cowrie SSH only |

Stack versions are pinned in `scripts/render.py` `STACK`; update configs +
docs + `STACK` together on any upgrade and record it in `CHANGELOG.md`.
