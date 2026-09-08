# Cowrie Dashboard

Grafana dashboard for visualizing SSH honeypot activity collected from Cowrie and stored in Loki.

This is a subcomponent of the main project. Refer to the repository root `README.md` for overall setup, deployment, configuration, and security information.

## Overview (tables-only, matching `grafana-dashboard.json`)

| Panel | Loki query |
|---|---|
| Login Attempts | `{job="cowrie"} \|= "cowrie.login.success"` |
| Commands Executed | `{job="cowrie"} \|= "cowrie.command.input" \| json \| label_format Source="{{.src_ip}}", Command="{{.input}}"` |
| Top Attacking IPs | `topk(10, sum by (src_ip) (count_over_time({job="cowrie"} \| json \| src_ip!="" [$__range])))` |
| Top Commands | `topk(10, sum by (input) (count_over_time({job="cowrie"} \| json \| input!="" [$__range])))` |
| Top Usernames | `topk(10, sum by (username) (count_over_time({job="cowrie"} \| json \| username!="" [$__range])))` |
| Top Passwords | `topk(10, sum by (password) (count_over_time({job="cowrie"} \| json \| password!="" [$__range])))` |

Deliberately out of scope for this version: time-series graphs,
per-service splits, download/session-duration panels, and GeoIP maps.
Those remain future work; the README no longer promises them.

## Stack

- [Grafana](https://grafana.com/) `10.2.3`
- [Loki](https://grafana.com/oss/loki/) `2.9.4`
- Cowrie `3.0.13` JSON logs via Promtail (`job="cowrie"`)

## Access

Services are localhost-bound on the sensor. From your workstation:

```bash
ssh -p <ADMIN_PORT> -i <PRIVATE_KEY> -L 3000:localhost:3000 <ADMIN_USER>@<REDACTED_HOST>
# open http://localhost:3000/d/b3f714e8-54fc-420f-b0ea-1aabea9d4858/cowrie?orgId=1
```

Grafana default in `honeypot-monitor/docker-compose.yml` is
`admin / admin` — change it on first login and do not commit the new
password. Never expose port 3000/3100 publicly.

## Dashboard location

```text
grafana-dashboard.json
```

Import via Grafana → Dashboards → Import. Screenshot: `dashboard.png`
(refresh when panels change, not on data updates).
Current dashboard UID: `b3f714e8-54fc-420f-b0ea-1aabea9d4858`.
