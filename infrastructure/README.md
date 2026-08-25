# Mahogany VPS Infrastructure

## Production Host

Mahogany services run on a Docker-based production VPS.

| Component | Value |
|---|---|
| OS | Ubuntu 24.04 LTS |
| Architecture | x86-64 |
| Virtualization | KVM |
| Docker Engine | 29.6.1 |
| Docker Compose | 5.2.0 |

## Docker Architecture

Production services are isolated using Docker Compose projects and networks.

### Main Services

- ERPNext / Frappe
- WordPress
- Nginx Proxy Manager
- OpenClaw
- 9router
- Portainer

### Networks

Relevant application networks include:

```text
erpnext_frappe_network
npm_network
openclaw_default

Nginx Proxy Manager uses npm_network as the shared reverse-proxy network.

Firewall

UFW is enabled.

Publicly exposed services:

SSH
HTTP (80)
HTTPS (443)

Administrative interfaces such as Nginx Proxy Manager, Portainer, and other internal management ports are restricted rather than exposed publicly.

Reverse Proxy

Nginx Proxy Manager provides the reverse-proxy and HTTPS entry point for web services.

Public web traffic is handled through:
Internet
    |
    v
Nginx Proxy Manager
    |
    +--> ERPNext
    +--> WordPress
    +--> Other web services

Backup

Production data is backed up outside the application containers.

Current backup coverage includes:

ERPNext database and site files
WordPress files and MariaDB
Nginx Proxy Manager data and Let's Encrypt certificates
n8n data
OpenClaw configuration and source
Docker and host configuration snapshots

Backup archives are stored under the VPS backup directory and should not be committed to this repository.

Recovery Principle

The repository contains deployment documentation and configuration required to understand the production architecture.

Actual secrets, credentials, TLS private keys, database data, application state, and backup archives remain outside Git.
