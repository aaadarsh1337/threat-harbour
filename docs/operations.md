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
are retired; `scripts/` now holds the automation below. The commands above
are the current manual health procedure.)

## Automated daily metrics (GitHub Actions)

`.github/workflows/daily-metrics.yml` runs at `00:00 UTC` daily (plus manual
`workflow_dispatch`): SSH to the sensor as the restricted `metrics` user,
`scp` + execute `scripts/parse_remote.py` read-only, render
`scripts/render.py` output (README block, `analysis/`, `evidence/`, charts),
then auto-commit + push when numbers changed.

- Sensor side: `metrics` user, key-only auth (`~/.ssh/threat-harbour-metrics`
  pubkey in `authorized_keys`), passwordless sudo limited to
  `/usr/bin/python3 /tmp/th-parse-*.py` (`/etc/sudoers.d/metrics-read`).
  It cannot run anything else as root — verified (`sudo whoami` denied).
- Secrets (repo Settings → Secrets → Actions): `SSH_HOST`, `SSH_PORT`,
  `SSH_USER`, `SSH_PRIVATE_KEY`, `SSH_KNOWN_HOSTS`.
- Workflow needs Settings → Actions → General → Workflow permissions →
  "Read and write permissions".
- The admin SSH port must be reachable from GitHub-hosted runners, so the
  OCI security list allows it from `0.0.0.0/0`. Accepted tradeoff: port is
  key-only, and the automation account is restricted to log parsing.
- Failures fail loud and push nothing — a stale README beats a wrong one.
  Manual equivalent of one run is documented in `evidence/manifest.md`.

Key rotation: `ssh-keygen -t ed25519`, replace the pubkey in
`/home/metrics/.ssh/authorized_keys`, update the `SSH_PRIVATE_KEY` secret.

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
