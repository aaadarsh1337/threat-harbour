# Operations

Sensor is live. Grafana/Loki are localhost-bound; use an SSH tunnel.

## Daily checks (read-only, from workstation)

```bash
ssh -p <ADMIN_PORT> -i <PRIVATE_KEY> -L 3000:localhost:3000 <ADMIN_USER>@<REDACTED_HOST> \
  'sudo docker ps --format "table {{.Names}}\t{{.Status}}"; \
   sudo ls -lh /home/jack/honeypot/var/log/cowrie/ | tail -n 5; \
   sudo wc -l /home/jack/honeypot/var/log/cowrie/cowrie.json* | tail -n 3'
```

Then open `http://localhost:3000/d/b3f714e8-54fc-420f-b0ea-1aabea9d4858/cowrie`
and confirm fresh `cowrie.session.connect` events.

(The legacy `./scripts/health-check.sh` / `./scripts/disk-usage.sh` names
are retired; `scripts/` now holds the automation below. The commands above
are the current manual health procedure.)

## Automated daily metrics (GitHub Actions)

`.github/workflows/daily-metrics.yml` runs at `00:00 UTC` daily (plus manual
`workflow_dispatch`): SSH to the sensor as the restricted `metrics` user,
`scp` + execute `scripts/parse_remote.py` read-only, render
`scripts/render.py` output (README block, `analysis/`, `evidence/`, charts),
then auto-commit + push when numbers changed.

- Sensor side: `metrics` user, key-only auth (`~/.ssh/threat-harbour-metrics`
  pubkey in `authorized_keys`), passwordless sudo limited to
  `/usr/bin/python3 /tmp/th-parse-*.py` (`/etc/sudoers.d/metrics-read` —
  redacted example: `configs/sudoers.d-metrics-read.example`).
  It cannot run anything else as root — verified (`sudo whoami` denied).
- Secrets (repo Settings → Secrets → Actions): `SSH_HOST`, `SSH_PORT`,
  `SSH_USER`, `SSH_PRIVATE_KEY`, `SSH_KNOWN_HOSTS`, plus the OCI API
  set below (`OCI_TENANCY_OCID`, `OCI_USER_OCID`, `OCI_FINGERPRINT`,
  `OCI_PRIVATE_KEY`, `OCI_REGION`, `OCI_INSTANCE_OCID`).
- Workflow needs Settings → Actions → General → Workflow permissions →
  "Read and write permissions".
- The admin SSH port must be reachable from GitHub-hosted runners, so the
  OCI security list allows it from `0.0.0.0/0`. Accepted tradeoff: port is
  key-only, and the automation account is restricted to log parsing.
- Failures fail loud and push nothing — a stale README beats a wrong one.
  Manual equivalent of one run is documented in `evidence/manifest.md`.

Key rotation: `ssh-keygen -t ed25519`, replace the pubkey in
`/home/metrics/.ssh/authorized_keys`, update the `SSH_PRIVATE_KEY` secret.

## Pre-run reboot (why + setup)

Symptom: `scp`/`ssh` from the workflow times out or resets even though the
action itself is correct — the E2.Micro sensor wedges under memory pressure
(Cowrie + Loki/Grafana/Promtail on ~1 GB RAM) and `sshd` stops answering.
A dashboard reboot fixes it because it reboots out-of-band via the
hypervisor; an in-band `ssh ... "sudo reboot"` cannot work once `sshd` is
dead. The workflow therefore issues an OCI `RESET` (force reboot, the API
equivalent of Console → Compute → Instances → Reboot with "Force reboot"
checked) on every run, waits up to ~10 min for SSH to return, then does
the collect with 3× retries per `scp`/`ssh` step.

One-time setup (OCI console):

1. Identity → Users → your user → API Keys → Add API Key → generate a pair.
   Download the private key; note the fingerprint.
2. Collect: tenancy OCID (Profile → Tenancy), user OCID (Users → details),
   region (e.g. `ap-hyderabad-1`), instance OCID (Compute → Instances →
   sensor → details).
3. Repo → Settings → Secrets and variables → Actions → New repository
   secret, one each for: `OCI_TENANCY_OCID`, `OCI_USER_OCID`,
   `OCI_FINGERPRINT`, `OCI_PRIVATE_KEY` (paste the full PEM including
   `-----BEGIN/END PRIVATE KEY-----` — this is the API key, not the SSH
   key), `OCI_REGION`, `OCI_INSTANCE_OCID`.
4. Principle of least privilege: create a dedicated OCI user (or group +
   policy limited to `manage instances` on this one compartment/instance)
   for the workflow; do not reuse your admin API key.
5. Test: Actions → daily-metrics → Run workflow. Expect `RESET
   issued` → `SSH is back` → collect → commit. If SSH never returns, check
   the instance state in the console and the serial console / boot volume.

Notes:

- The workflow uses force `RESET` (immediate power off, then power back
  on) deliberately. There is no `SOFTREBOOT` action in the OCI API/CLI —
  valid `--action` values are `STOP`, `START`, `SOFTRESET`, `RESET`,
  `SOFTSTOP`, etc. — so the previous `SOFTREBOOT` value failed every run.
  `SOFTRESET` (graceful) was not chosen because a wedged sensor may never
  answer the OS shutdown signal, and `SOFTRESET` then waits up to 15 min
  before power-cycling anyway; `RESET` recovers immediately and works even
  when the OS/`sshd` is fully dead.
- Tradeoff of a force reboot: at most the in-flight Cowrie JSON line being
  written at power-off can truncate. The collector tolerates this (the
  parser skips/counts malformed lines), ext4 journaling recovers the
  filesystem, and the next run re-parses the full log set — so worst case
  is one lost event, versus a stuck pipeline with no run at all.
- Local equivalent of one run: `oci compute instance action
  --instance-id <OCID> --action RESET`, wait for `ssh` to answer,
  then the manual collect in `evidence/manifest.md`.

## What to watch

- All three monitor containers up: `grafana`, `loki`, `promtail`
- Cowrie daily log file growing; per-day counts refresh in
  `analysis/metrics.json` with each daily run
- Cowrie JSON grows daily — watch `du -sh` on the log dir and rotate before
  Free Tier disk pressure; never delete without recording hashes/counts
- Resource limits in `honeypot-monitor/docker-compose.yml`
  (loki 280M, grafana 220M, promtail 80M)

## Change control

Record Cowrie version (`3.0.13`), config rev, and compose rev in
`CHANGELOG.md` on any infra or config change. Raw logs stay on sensor;
publish aggregates only.
