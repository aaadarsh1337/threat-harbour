# Deployment

## Prerequisites

- OCI account with Free Tier capacity
- SSH key pair
- Region: `ap-hyderabad-1`
- VM shape: `VM.Standard.E2.1.Micro`
- Cowrie version: `<COWRIE_VERSION>`
- A separate analysis workstation

## 1. Create the OCI Network

Create:

- A VCN
- A public subnet
- An Internet Gateway
- A route table with a default route to the Internet Gateway
- A security list or NSG
- A public IPv4 address

Document the resulting values in a private deployment record. Publish only the information necessary to reproduce the architecture.

## 2. Configure Network Rules

Allow only the intended honeypot ports from the Internet.
