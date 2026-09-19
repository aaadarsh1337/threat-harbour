# Architecture

> Live output of this setup: **[aaadarsh1337.github.io/intel](https://aaadarsh1337.github.io/intel)** (public stats site, refreshed daily). What follows is how it is built.

## Overview

One OCI Free Tier VM (`VM.Standard.E2.1.Micro`, Ubuntu 24.04, `ap-hyderabad-1`)
as a lightweight public honeypot sensor — single-node by design, one port,
tight scope, rebuildable (see `configs/` for redacted source configs).

The VM runs:

- Cowrie `3.0.13` SSH-only (venv at `/home/jack/honeypot/cowrie-env`,
  config `etc/cowrie.cfg`, logs `var/log/cowrie/cowrie.json*` rotated daily,
  artifacts `var/lib/cowrie/downloads/` + `tty/`)
- Monitor stack over Docker, all localhost-bound: Promtail `2.9.4`
  (`job="cowrie"`, read-only mount of the Cowrie log dir) → Loki `2.9.4`
  (`:3100`) → Grafana `10.2.3` (`:3000`, reached via SSH tunnel only)
- No agent on the sensor: `scripts/parse_remote.py` is scp'd fresh each daily
  run, executed via restricted sudo, then deleted (see `docs/operations.md`)

Source of truth for the diagram: `diagrams/architecture.mmd` /
`diagrams/architecture.dot` → `diagrams/architecture.png`.

## Network Flow

```text
Internet (unsolicited SSH scanners/bots)
   |
OCI Edge: Internet Gateway + VCN + public subnet
   |
NSG / SecList — allow: Cowrie SSH; deny: 3000/3100, admin SSH from Internet
   |  (exception: admin SSH key-only port reachable from GitHub runners
   |   for the daily job — tradeoff documented in docs/operations.md)
   |
Sensor VM (ap-hyderabad-1 · E2.1.Micro · Ubuntu 24.04)
   |-- Cowrie 3.0.13 SSH honeypot :22 → cowrie.json* + tty + downloads/
   |-- Monitor stack (Promtail → Loki → Grafana, localhost only)
   |
Analyst --ssh -L 3000:localhost--> Grafana in browser
```

## Data Flow

```text
Cowrie cowrie.json* --read-only--> Promtail (job="cowrie")
  --> Loki :3100 --LogQL--> Grafana :3000 (6 table panels, via tunnel)
Cowrie cowrie.json* --offline Python parse (scripts/parse_remote.py)-->
  aggregates only --> Repo: analysis/metrics.json, analysis/summary.md,
  evidence/manifest.md --> README leaderboard + public stats site
  (https://aaadarsh1337.github.io/intel, separate static site) +
  diagrams/activity-timeline.png, diagrams/session-funnel.png
```

Flow diagram source: `diagrams/data-pipeline.mmd` /
`diagrams/data-pipeline.dot`. Node labels stay count-free by design; live
numbers live in `analysis/metrics.json`, not in the image.

## Published vs Local Views

- Public stats site, no login: [aaadarsh1337.github.io/intel](https://aaadarsh1337.github.io/intel)
  + README leaderboard (both refreshed every 24h from the same aggregates;
  separate from Grafana)
- Local Grafana, operator-only via tunnel: (`dashboard/grafana-dashboard.json`,
  UID `b3f714e8-54fc-420f-b0ea-1aabea9d4858`) — see `dashboard/README.md`,
  never public
- Raw logs, source IPs, payloads, keys stay on the sensor; only aggregates,
  /16 volume buckets, and redacted hashes leave it.
