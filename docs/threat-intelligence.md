# Threat Intelligence

## Scope

This report covers activity observed by one Cowrie sensor between
`<START_UTC>` and `<END_UTC>`.

## Data Sources

- Cowrie JSON logs
- Cowrie session metadata
- Host health records
- OCI network and instance metadata
- Optional enrichment source: `<ENRICHMENT_SOURCE>`

## Metrics

- Total events: `<NUMBER_OF_EVENTS>`
- Unique source IPs: `<NUMBER_OF_SOURCE_IPS>`
- Sessions: `<NUMBER_OF_SESSIONS>`
- Login attempts: `<NUMBER_OF_LOGIN_ATTEMPTS>`
- Commands: `<NUMBER_OF_COMMANDS>`
- Download attempts: `<NUMBER_OF_DOWNLOADS>`
- Top targeted accounts: `<TOP_ACCOUNTS>`
- Top command categories: `<TOP_COMMAND_CATEGORIES>`

## Behavioral Categories

Classify activity using observable behavior:

- Scanning
- Credential guessing
- Interactive shell use
- Discovery commands
- Persistence attempts
- Downloader behavior
- Malware execution attempts
- Cryptocurrency-mining indicators
- Destructive or disruptive commands
- Unclassified

## Attribution Language

Use:

> The source IP geolocated to `<LOCATION>`; this does not establish the
> identity, physical location, or intent of the operator.

Use “observed from,” “associated with the session,” and “consistent with”
rather than “attacker,” “criminal,” or “operator from `<COUNTRY>`.”

## Indicators of Compromise

Publish only appropriately redacted indicators:

| Type | Value | First observed | Last observed | Confidence | Notes |
|---|---|---|---|---|---|
| IP | `<REDACTED_IP>` | `<DATE>` | `<DATE>` | `<LEVEL>` | `<NOTES>` |
| Domain | `<REDACTED_DOMAIN>` | `<DATE>` | `<DATE>` | `<LEVEL>` | `<NOTES>` |
| URL | `<REDACTED_URL>` | `<DATE>` | `<DATE>` | `<LEVEL>` | `<NOTES>` |
| Hash | `<SHA256>` | `<DATE>` | `<DATE>` | `<LEVEL>` | `<NOTES>` |

## Confidence

- High: directly observed and supported by multiple event fields
- Moderate: supported by consistent behavioral indicators
- Low: incomplete, ambiguous, or indirect evidence

## Findings

1. `<FINDING_WITH_EVIDENCE>`
2. `<FINDING_WITH_EVIDENCE>`
3. `<FINDING_WITH_LIMITATION>`

## Limitations

The findings are sensor-specific and may reflect Cowrie's emulation, deployment location, public IP reputation, collection gaps, and the limited observation period. No attacker attribution is made.
