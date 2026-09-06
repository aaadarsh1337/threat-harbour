# Deployment

## Prerequisites

- OCI account with Free Tier capacity
- SSH key pair (private key kept off the VM and out of this repo)
- Region: `ap-hyderabad-1`
- VM shape: `VM.Standard.E2.1.Micro`
- Cowrie version: `3.0.13` (venv at `/home/jack/honeypot/cowrie-env`)
- Monitor stack: Grafana `10.2.3`, Loki `2.9.4`, Promtail `2.9.4`
  (compose at `/home/jack/honeypot-monitor/docker-compose.yml`)
- A separate analysis workstation

## 1. Create the OCI network

Create:

- A VCN
- A public subnet
- An Internet Gateway
- A route table with a default route to the Internet Gateway
- A security list or NSG
- A public IPv4 address

Document the resulting values in a private deployment record. Publish only
the information necessary to reproduce the architecture. Do not publish the
sensor public IP, OCIDs, or keys.

## 2. Configure network rules

Allow only the intended honeypot ports from the Internet (SSH to Cowrie).
Administrative and analytical services must NOT be public:

- Cowrie SSH honeypot: public (observed SSH-only in this window; no Telnet
  events recorded)
- Admin SSH: restricted port/key only (not the honeypot port)
- Grafana (`3000`) and Loki (`3100`): localhost-bound, reached via SSH
  tunnel (e.g. `ssh -L 3000:localhost:3000`), never exposed publicly

Validate the effective rules from both OCI and the host firewall.

## 3. Install Cowrie (as deployed)

- Python venv + Cowrie `3.0.13` under `/home/jack/honeypot/`
- Config: `/home/jack/honeypot/etc/cowrie.cfg`; logs:
  `/home/jack/honeypot/var/log/cowrie/cowrie.json*` (rotated daily)
- Artifacts: `var/lib/cowrie/downloads/`, `var/lib/cowrie/tty/`
- Verify: `sudo wc -l /home/jack/honeypot/var/log/cowrie/cowrie.json*`
  shows growing daily files; a test login appears as
  `cowrie.session.connect` + `cowrie.login.*` (exclude test events from
  published metrics).

## 4. Install monitoring (as deployed)

- `docker-compose.yml` runs `loki`, `promtail` (read-only mount of the
  Cowrie log dir, `job="cowrie"`), and `grafana`
- Promtail config maps `/var/log/cowrie/cowrie.json*`
- Verify: Loki `http://localhost:3100/ready`, Grafana
  `http://localhost:3000` via tunnel; import `dashboard/grafana-dashboard.json`

## 5. Log rotation and retention

- Cowrie rotates `cowrie.json` daily (observed `cowrie.json.YYYY-MM-DD`).
- Keep raw logs on the sensor; publish aggregates only
  (`analysis/metrics.json`). Record hashes and per-day counts in
  `evidence/manifest.md` before any rebuild.
