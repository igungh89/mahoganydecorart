# Mahogany Decor Art

Central repository for the Mahogany Decor Art digital system.

## Project Structure

```text
mahogany/
├── erpnext/
├── n8n/
├── wordpress/
└── infrastructure/
```

##Stack
###ERPNext

Business management system and custom Mahogany ERPNext application.

Current repository content includes the Mahogany custom ERPNext application under:
````text
erpnext/custom-app/mahogany/
````

The ERPNext stack will be audited and documented separately.

###n8n

Automation and workflow integration layer.

The n8n stack will be added and documented separately.

###WordPress

Public website and web presence.

The WordPress stack will be added and documented separately.

###Infrastructure

Infrastructure, Docker, deployment, networking, and server-related configuration.

The infrastructure stack will be added and documented separately.

Repository Status

This repository is currently under active development and audit.

The current structure is intentionally kept simple while each technology stack is reviewed.

Documentation and architecture will be updated as each stack is audited.

Source Control

Primary branch:

main

Repository:

https://github.com/igungh89/mahoganydecorart

Repository visibility:

Private
Production Environment

The Mahogany system currently runs on a VPS using Docker-based infrastructure.

Production configuration and runtime data are kept separate from the Git repository.

This repository is intended primarily for source control, documentation, configuration, and recovery of the project.

Data & Security

The following should not be committed to this repository:

Production databases
Database dumps
Passwords
API keys
Access tokens
Private SSH keys
.env files containing secrets
User-uploaded files
Runtime logs
Docker volumes
Temporary files
Python cache files
Node modules
Other sensitive production data

Production data and backups should be managed separately.

Development Principle

Mahogany contains business-critical systems and custom business logic.

Changes to production functionality should be made carefully and documented when appropriate.

Existing production behavior should not be changed unintentionally during development, testing, or refactoring.

Roadmap
 Repository structure
 ERPNext custom application source
 Initial Git repository
 GitHub repository
 Initial GitHub backup
 ERPNext audit
 ERPNext architecture documentation
 ERPNext development workflow
 Infrastructure audit
 Infrastructure documentation
 n8n audit
 n8n documentation
 WordPress audit
 WordPress documentation
 Database backup documentation
 Disaster recovery documentation
 Deployment workflow
 CI/CD workflow
Project Status

Status: Active Development & Audit

The repository structure and documentation will evolve as the Mahogany system is reviewed and developed.
