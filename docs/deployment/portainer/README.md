# Portainer Deployment

## Production Environment

Portainer is used to manage Docker containers and stacks on the Mahogany VPS.

| Component | Value |
|---|---|
| Image | `portainer/portainer-ce:latest` |
| Container | `portainer` |
| Restart Policy | `unless-stopped` |
| Working Directory | `/` |
| HTTP | `9000` (internal only) |
| Edge Agent | `8000` |
| HTTPS Admin | `9443` |
| Network | `bridge` |

## Persistent Data

Portainer uses one Docker volume:

```text
portainer_data
    -> /data

The Docker socket is also mounted:
/var/run/docker.sock
    -> /var/run/docker.sock

This allows Portainer to manage the Docker environment.

Backup

Portainer persistent data is included in the VPS backup:
volumes/portainer_data_*.tar.gz
