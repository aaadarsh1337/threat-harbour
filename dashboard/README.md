# Cowrie Dashboard

Grafana dashboard for visualizing SSH honeypot activity collected from Cowrie and stored in Loki.

This is a subcomponent of the main project. Refer to the repository root `README.md` for overall setup, deployment, configuration, and security information.

## Overview

The dashboard provides an overview of activity recorded by the Cowrie honeypot, including:

- SSH connection attempts
- Successful and failed login attempts
- Source IP addresses
- Attempted usernames and passwords
- Commands executed by attackers
- File downloads and uploads
- Event activity over time
- Recent Cowrie log events

## Stack

- [Grafana](https://grafana.com/)
- [Loki](https://grafana.com/oss/loki/)
- Cowrie SSH honeypot logs
- Promtail, Grafana Alloy, or another Loki-compatible log collector

## Dashboard Location

The dashboard definition is stored in:

```text
grafana-dashboard.json

