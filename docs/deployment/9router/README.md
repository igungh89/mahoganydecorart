# 9router Deployment

## Production Environment

9router runs as a Docker-based service on the Mahogany VPS.

| Component | Value |
|---|---|
| Image | `decolua/9router:latest` |
| Container | `9router` |
| Restart Policy | `unless-stopped` |
| Working Directory | `/app` |
| Port | `20128` |
| Network | `npm_network` |

## Persistent Data

9router uses a host bind mount for application data:

```text
/.9router
    -> /app/data

Network

The service is connected to the shared npm_network Docker network.
