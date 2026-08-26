# Hardening

## Administrative Access

- Use SSH keys rather than passwords.
- Disable direct root login.
- Use a non-root administrative account.
- Use MFA for the OCI account.
- Store private keys outside the VM and repository.
- Rotate keys if exposure is suspected.

## Network Controls

Public exposure should be limited to the Cowrie listener ports. Administrative and analytical services must remain private or localhost-bound.
 
Validate the effective rules from both OCI and the host firewall.

## Host Controls

- Apply security updates on a documented schedule.
- Remove unused packages and services.
- Keep Cowrie pinned to a documented version.
- Avoid mounting sensitive host paths into containers.
- Do not run unrelated workloads on the sensor.
- Monitor CPU, memory, disk, and process behavior.
- Configure log rotation and retention.

## Data Handling

Do not store production data, personal data, credentials, private keys, or sensitive information on the sensor.

Treat captured commands, usernames, passwords, URLs, and payload metadata as potentially sensitive. Redact before publication.
