# OpenClaw Deployment

## Production Environment

OpenClaw runs as a Docker-based service on the Mahogany VPS.

| Component | Value |
|---|---|
| Image | `openclaw:local` |
| Container | `openclaw-openclaw-gateway-1` |
| Restart Policy | `unless-stopped` |
| Working Directory | `/app` |
| Network | `openclaw_default` |
| Gateway Port | `18789` |
| Bridge Port | `18790` |
| Additional Port | `3978` |

## Persistent Data

OpenClaw uses host bind mounts for its configuration, authentication secrets, and workspace.

```text
~/.openclaw-auth-profile-secrets
    -> /home/node/.config/openclaw

~/.openclaw
    -> /home/node/.openclaw

~/.openclaw/workspace
    -> /home/node/.openclaw/workspace

Backup

The OpenClaw source configuration is backed up under:
configs/openclaw/

A local Docker image backup is also maintained:
images/openclaw-local.tar
