# Architecture

## Overview

This project uses one OCI VM as a lightweight public honeypot sensor.

The VM contains:

- Canonical Ubuntu 24.04
- Cowrie
- Docker Cowrie runtime
- JSON log collection
- Local storage
- Analysis scripts

The term single-node refers to the infrastructure layout. It does not mean that only one honeypot behavior or service exists. Cowrie can provide SSH and Telnet emulation from the same VM.

## Network Flow

```text
Internet
   |
OCI Internet Gateway
   |
VCN
   |
Public subnet
   |
Security list / NSG rules
   |
Public Cowrie VM
   |
Cowrie SSH/Telnet listeners
   |
JSON logs and session artifacts
   |
Offline analysis and optional dashboard
```
