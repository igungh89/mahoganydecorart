# Mahogany ERPNext Deployment

## Production Environment

Mahogany ERPNext runs in a Docker-based production environment.

| Component | Value |
|---|---|
| ERPNext | 16.30.0 |
| Frappe | 16.29.0 |
| Custom App | mahogany 0.0.1 |
| bypass_phone | 0.0.1 |
| Database | MariaDB 11.8 |
| Site | frontend |
| Production Domain | `<your-production-domain>` |
| Container Image | frappe/erpnext:v16.30.0-custom |

> **Environment snapshot:** Verified on 2026-08-25.

## Architecture

The ERPNext production stack consists of:

- Frontend
- Backend
- WebSocket
- Queue Short
- Queue Long
- Scheduler
- Configurator
- MariaDB
- Redis Cache
- Redis Queue

The application source code for Mahogany-specific functionality is stored under:

```text
custom-apps/
├── mahogany/
└── bypass_phone/

Deployment Source

The Docker deployment is based on the Frappe Docker project.

The upstream Frappe Docker repository is maintained separately from this repository.

Mahogany-specific deployment configuration is maintained in this repository.

Production Data

Production data is intentionally kept outside Git source control.

The following are NOT stored in GitHub:

Production database
Database dumps
Docker volumes
Redis data
Uploaded files
Site private files
Passwords
API keys
Access tokens
SSH keys
Production .env files
Runtime logs
Backup

A full Frappe site backup was successfully created on 2026-08-25 using:
bench --site frontend backup --with-files

The backup contains:

Site configuration backup
Database backup
Public files backup
Private files backup

The database backup is stored separately from GitHub.

Recovery Principle

Recovery is divided into several layers:

Git repository
Application source code
Deployment configuration
Documentation
Frappe site backup
Database
Public files
Private files
Site configuration
Production infrastructure backup
Docker configuration
Reverse proxy configuration
Server configuration
Other infrastructure-specific data

The Git repository must never be treated as a replacement for the production database backup.

Important

Production changes must be performed carefully.

Do not run migrations, modify production data, or change deployment configuration without verifying the impact first.
