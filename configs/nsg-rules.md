# NSG / Security List rules (redacted — OCI console → VCN → Security List / NSG)

Public surface is Cowrie SSH only. Grafana (`3000`) and Loki (`3100`) are
localhost-bound (see `docker-compose.yml.example`) and never get an ingress rule.

| Direction | Source | Port | Allow | Notes |
|---|---|---|---|---|
| Ingress | `0.0.0.0/0` | `22/tcp` | yes | Cowrie SSH honeypot (public) |
| Ingress | `0.0.0.0/0` | `<ADMIN_PORT>/tcp` | yes | Host admin SSH, key-only, restricted `metrics` user. Required reachable from GitHub runners for the daily job — tradeoff in `docs/operations.md`. Harden: restrict to runner IPs / bastion / Tailscale if available. |
| Ingress | `0.0.0.0/0` | `3000/tcp`, `3100/tcp` | **no** | Never public; via `ssh -L 3000:localhost:3000` tunnel only |
| Egress | `0.0.0.0/0` | all | yes | Updates, Docker pulls, OCI API |

Validate from both OCI console and host firewall (`ss -tlnp` should show
`3000`/`3100` on `127.0.0.1` only). Do not publish the sensor public IP or OCIDs.
