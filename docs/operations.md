# Operations

Sensor is live. Grafana/Loki are localhost-bound; use an SSH tunnel.

## Daily checks (read-only, from workstation)

```bash
ssh -p <ADMIN_PORT> -i <PRIVATE_KEY> -L 3000:localhost:3000 <ADMIN_USER>@<REDACTED_HOST> \
  'sudo docker ps --format "table {{.Names}}\t{{.Status}}"; \
   sudo ls -lh /home/jack/honeypot/var/log/cowrie/ | tail -n 5; \
   sudo wc -l /home/jack/honeypot/var/log/cowrie/cowrie.json* | tail -n 3'
```

Then open `http://localhost:3000/d/b3f714e8-54fc-420f-b0ea-1aabea9d4858/cowrie`
and confirm fresh `cowrie.session.connect` events.

(The legacy `./scripts/health-check.sh` / `./scripts/disk-usage.sh` names
are retired; no `scripts/` dir ships in this repo. The commands above are
the current procedure.)

## What to watch

- All three monitor containers up: `grafana`, `loki`, `promtail`
- Cowrie daily log file growing; per-day counts logged to
  `analysis/metrics.json` at each interim cutoff
- Disk: `50M` of Cowrie JSON at 2026-09-06 cutoff — plan rotation before
  Free Tier disk pressure; never delete without recording hashes/counts
- Resource limits in `honeypot-monitor/docker-compose.yml`
  (loki 280M, grafana 220M, promtail 80M)

## Change control

Record Cowrie version (`3.0.13`), config rev, and compose rev in
`CHANGELOG.md` at each interim analysis. Raw logs stay on sensor;
publish aggregates only.
