# Mahogany WordPress Deployment

## Production Environment

Mahogany Decor Art public website runs on a Docker-based WordPress environment.

| Component | Value |
|---|---|
| WordPress | `wordpress:latest` |
| Database | MariaDB 11 |
| Container | `wordpress` |
| Database Container | `mariadb` |
| Working Directory | `/var/www/html` |
| Restart Policy | `unless-stopped` |
| Network | `npm_network` |
| WordPress Volume | `wordpress_wordpress_data` |
| Database Volume | `wordpress_mariadb_data` |

## Architecture

The production WordPress stack consists of:

- WordPress application
- MariaDB database
- Docker persistent volumes
- Nginx Proxy Manager for reverse proxy and HTTPS
- External domain and DNS configuration

WordPress application data is persisted in:

```text
wordpress_wordpress_data
    -> /var/www/html

MariaDB database data is persisted in:
wordpress_mariadb_data
    -> /var/lib/mysql

The WordPress container and reverse proxy communicate through:
npm_network

Data Protection

The production WordPress environment is protected through separate backups of:

WordPress application files
WordPress uploads and configuration
MariaDB database data

Backup files are stored outside the Git repository.

Production databases, uploaded media, credentials, API keys, and other runtime secrets are not committed to source control.

Recovery

A WordPress recovery requires restoration of:

WordPress application volume
MariaDB database volume
Docker deployment configuration
Reverse proxy configuration
DNS and HTTPS configuration

The latest verified volume backups are maintained separately from the source repository.

Source Control

The Mahogany repository contains project documentation and source/configuration where appropriate.

Production runtime data is intentionally kept outside Git.

Operational Principle

The WordPress production environment should be changed carefully.

Existing website functionality, uploaded content, database data, reverse proxy configuration, and production behavior should not be changed unintentionally during development or maintenance.
