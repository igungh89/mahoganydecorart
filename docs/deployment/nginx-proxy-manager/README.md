# Nginx Proxy Manager Deployment

## Production Environment

Nginx Proxy Manager (NPM) is used as the reverse proxy and HTTPS entry point for Mahogany services.

| Component | Value |
|---|---|
| Image | `jc21/nginx-proxy-manager:latest` |
| Container | `nginx-proxy-manager` |
| Restart Policy | `unless-stopped` |
| HTTP | `80` |
| HTTPS | `443` |
| Admin Interface | `81` |
| Networks | `npm_network`, `frappe_docker_default` |

## Persistent Data

NPM uses two Docker volumes:

```text
## Persistent Data

NPM uses two Docker volumes:

```text
nginx-proxy-manager_npm_data
    -> /data

nginx-proxy-manager_npm_letsencrypt
    -> /etc/letsencrypt

The npm_data volume contains NPM application and configuration data.

The npm_letsencrypt volume contains TLS certificates and related Let's Encrypt data.

Network

NPM is connected to:

npm_network
frappe_docker_default

The npm_network network is used to reach services exposed through the reverse proxy.

Published Ports
Port	Purpose
80	HTTP
443	HTTPS
81	NPM administration

Ports 80 and 443 are published on all host interfaces.

Port 81 is also published on all host interfaces and should be protected appropriately at the infrastructure level.

Backup

The following persistent volumes are backed up:
nginx-proxy-manager_npm_data
nginx-proxy-manager_npm_letsencrypt

Current backup files are stored outside the Docker volume and include timestamped archives.

Recovery

To restore NPM, restore both persistent volumes:

Restore nginx-proxy-manager_npm_data.
Restore nginx-proxy-manager_npm_letsencrypt.
Start the NPM container.
Verify proxy hosts and HTTPS certificates.

Both volumes are required for a complete NPM recovery.
