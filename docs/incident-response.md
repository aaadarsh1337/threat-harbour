# Incident Response

## Expected Honeypot Activity

The following is expected:

- Port scans
- Login attempts
- Repeated username/password guesses
- Shell commands in Cowrie sessions
- Attempts to download files
- Automated botnet behavior
- Malformed protocol input

## Possible Host Compromise

Escalate when there is evidence of:

- Unexpected privileged processes
- New users or SSH keys
- Unknown containers
- Unexpected outbound connections from the host
- Modified system configuration
- Persistence mechanisms
- Unusual CPU, memory, or disk activity
- Access outside the intended Cowrie environment

## Severity

| Severity | Description | Action |
|---|---|---|
| Low | Expected interaction with Cowrie | Continue monitoring |
| Medium | Suspicious configuration or resource event | Investigate and document |
| High | Possible host compromise | Isolate VM and preserve evidence |
| Critical | Confirmed compromise or unauthorized impact | Isolate, preserve, destroy, rebuild, review |

## Response Procedure

1. Record the detection time in UTC.
2. Record the symptoms and affected services.
3. Restrict or remove public network access.
4. Preserve available logs and OCI metadata.
5. Do not interact with suspected external systems.
6. Isolate or stop the VM.
7. Export evidence without publishing raw sensitive data.
8. Rebuild from a known-good process.
9. Rotate any potentially exposed credentials or keys.
10. Conduct a post-incident review.

## Evidence Record

```text
Incident ID: <INCIDENT\_ID>
Detected: <YYYY-MM-DDTHH:MM:SSZ>
Detected by: <YOUR\_NAME\_OR\_ALIAS>
Affected VM: <REDACTED\_VM\_IDENTIFIER>
Observed indicators: <INDICATORS>
Containment time: <YYYY-MM-DDTHH:MM:SSZ>
Recovery time: <YYYY-MM-DDTHH:MM:SSZ>
Disposition: <DISPOSITION>
