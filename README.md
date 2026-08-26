# Threat Harbour
## A T-Pot-Based Cloud Threat Intelligence Sensor

Hello Hackers! 
Today, I will be trying out something new. Usually I am all about red teaming, CTF's and breaking into stuff (legally of course)
But today, I've decided to spin up my own honeypot, using T-Pot, to learn more about the other side of the game. 
We will analyze what happens to our instance on internet, which will provide us an insight on how attackers think and work. 
------------------

> A defensive security research project that deploys the T-Pot multi-honeypot
platform on Oracle Cloud Infrastructure to observe opportunistic attacks,
collect telemetry, and analyze attacker behavior.

## Skills demonstrated:

- Linux server administration
- Oracle Cloud Infrastructure
- Virtual networks and firewall rules
- Docker and containerized security tools
- Honeypot deployment
- Log ingestion and analysis
- Kibana dashboards
- Threat intelligence
- Incident triage
- Detection engineering
- Technical documentation
- Secure operations

## Project status

| Item | Status |
|---|---|
| Cloud deployment | Operational |
| Honeypot platform | T-Pot |
| Cloud provider | Oracle Cloud Infrastructure |
| Architecture | Single-node public sensor |
| Data visualization | Kibana |
| Monitoring period | YYYY-MM-DD to YYYY-MM-DD |
| Last tested | YYYY-MM-DD |

## Objectives

1. Deploy a multi-honeypot sensor in a cloud environment.
2. Expose realistic but isolated services to the public Internet.
3. Collect and visualize attack telemetry.
4. Identify recurring source networks, usernames, passwords, tools, and payloads.
5. Produce defensible threat-intelligence findings.
6. Document the deployment so it can be reproduced safely.

## Architecture

The system consists of:

- Oracle Cloud public subnet
- Ubuntu or Debian host
- T-Pot Docker-based honeypot platform
- Internet-facing honeypot services
- T-Pot management interface
- Elastic/Kibana-based visualization
- Administrative SSH access on the T-Pot management port

See [`docs/architecture.md`](docs/architecture.md).

## Key findings

This section is updated periodically.

- Observation period:
- Total connection attempts:
- Unique source IPs:
- Most targeted service:
- Most common usernames:
- Most common passwords:
- Most frequent countries or networks:
- Malware or payload families observed:
- Most significant behavioral pattern:

All findings are based on honeypot telemetry and should not be interpreted
as attribution of activity to a specific person or organization.

## Security model

This sensor is intentionally exposed to hostile traffic. It does not host
production workloads and must not contain personal data, credentials, or
sensitive business information.

Administrative access is restricted to the operator. Honeypot traffic is
treated as untrusted, and collected data is reviewed and redacted before
publication.

## Results

Include screenshots of:

- Overall T-Pot dashboard
- Attack volume over time
- Source-country or ASN distribution
- Credential attacks
- Targeted ports
- Malware or command activity
- Storage and system-health metrics

## Limitations

- The sensor represents one public IP and one cloud region.
- Results are affected by Internet scanning trends.
- GeoIP and ASN data may be inaccurate.
- T-Pot telemetry is not equivalent to telemetry from a production network.
- A honeypot cannot establish attacker identity or intent.

## Ethical use

This project is for defensive research and monitoring. No attempt is made
to access, disrupt, exploit, or retaliate against attacking systems.
