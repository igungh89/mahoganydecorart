# Mahogany Decor Art

Central repository for the **Mahogany Decor Art digital business system**.

This repository contains the source code, custom business applications, infrastructure configuration, automation components, documentation, and recovery-related information used to develop and maintain the Mahogany digital platform.

> **Repository visibility:** Private  
> **Primary branch:** `main`  
> **Status:** Active Development & Audit

---

## Overview

Mahogany Decor Art uses a modular digital platform built around several technology stacks.

The system is designed to support business operations while keeping application source code, infrastructure, automation, and public website components organized in a single repository.

### Main Components

| Component | Purpose |
|---|---|
| **ERPNext** | Business management and operational system |
| **n8n** | Automation and workflow integration |
| **WordPress** | Public website and web presence |
| **Infrastructure** | Docker, deployment, networking, and server configuration |

---

## System Architecture

```text
Mahogany Decor Art
│
├── ERPNext
│   ├── Frappe Framework
│   ├── ERPNext
│   ├── Mahogany custom application
│   └── Additional custom applications
│
├── n8n
│   └── Automation & workflow integration
│
├── WordPress
│   └── Public website
│
└── Infrastructure
    ├── Docker
    ├── Deployment
    ├── Networking
    └── Server configuration

ERPNext

ERPNext is the primary business management platform for Mahogany Decor Art.

The platform uses the Frappe Framework together with ERPNext and custom Mahogany business logic.

Current Versions
| Component    | Version |
| ------------ | ------- |
| Frappe       | 16.29.0 |
| ERPNext      | 16.30.0 |
| Mahogany     | 0.0.1   |
| bypass_phone | 0.0.1   |

Installed Applications
frappe
erpnext
mahogany
bypass_phone

Custom Application

The main Mahogany business logic is maintained as a custom Frappe application:
custom-apps/
└── mahogany/

The custom application contains functionality specific to Mahogany Decor Art and is maintained separately from the standard ERPNext source.

ERPNext Site

Production ERPNext is deployed as:


Production runtime data is intentionally kept outside the Git repository.

n8n

n8n is used as the automation and workflow integration layer.

It is intended to connect business processes and external services without placing integration logic directly inside every application.

Automation workflows are maintained separately from the ERPNext application logic.
n8n/

The n8n stack is currently under active development and documentation.

WordPress

WordPress is used as the public-facing website and web presence for Mahogany Decor Art.

wordpress/

The WordPress stack is maintained separately from the ERPNext business system while remaining part of the overall Mahogany platform.

Infrastructure

Infrastructure configuration is maintained in:
infrastructure/

This area covers infrastructure-related configuration such as:

Docker
Deployment
Networking
Server configuration
Supporting infrastructure services

Production runtime data, Docker volumes, and other generated runtime data are not maintained as source-controlled application files.

Repository Structure

Current repository structure:

mahogany/
│
├── backups/
│   └── audits/
│       └── erpnext/
│
├── custom-apps/
│   └── mahogany/
│
├── infrastructure/
│
├── n8n/
│
├── wordpress/
│
├── compose.yaml
├── apps.json
├── README.md
└── other project configuration

The repository structure is intentionally organized by system responsibility so each major component can be developed, audited, and documented independently.

Backup & Recovery

Backup strategy separates source code from production data.

Source Code Backup

Git is used as the primary source-control and source-code recovery mechanism.

The repository contains:

Custom applications
Infrastructure configuration
Automation source
Website-related source/configuration
Project documentation
Architecture and audit information

Changes are tracked through Git commits and pushed to the private GitHub repository.

ERPNext Site Backup

ERPNext site backups are created separately using the Frappe backup mechanism.

A full site backup was successfully performed on:
2026-08-25

Using:
bench --site frontend backup --with-files

The backup included:
Site configuration
Database
Public files
Private files

The backup is stored in the ERPNext environment and is not committed to Git.

Detailed audit information is maintained under:
backups/audits/erpnext/

Database Policy

Production databases and database dumps are intentionally excluded from Git version control.

This prevents sensitive production data from being exposed through the source repository.

Security & Data Policy

The following should never be committed to this repository:

Production databases
Database dumps
Passwords
API keys
Access tokens
Private SSH keys
.env files containing secrets
User-uploaded production files
Runtime logs
Docker volumes
Temporary files
Python cache files
Node modules
Other sensitive production data

Production data and production backups are managed separately from the source repository.

Development Principle

Mahogany contains business-critical systems and custom business logic.

Development therefore follows several principles:

Production behavior should not be changed unintentionally.
Existing business logic should be preserved unless a change is explicitly required.
Changes should be reviewed before being deployed to production.
Production database data should not be used for destructive testing.
Backup and recovery procedures should be established before major system changes.
Important architectural and business decisions should be documented.

The goal is to keep the system maintainable while minimizing the risk of unintended changes to production behavior.

Source Control

The primary branch is:
main

Remote repository:
git@github.com:igungh89/mahoganydecorart.git

The repository is maintained as a private GitHub repository.

Git is used to provide:

Version history
Change tracking
Source recovery
Collaboration
Deployment preparation
Auditability

Project Roadmap

The project is being progressively audited and documented.

Completed / In Progress
 Repository structure
 Initial Git repository
 GitHub repository
 Initial GitHub backup
 ERPNext custom application source
 ERPNext source reconciliation
 ERPNext backup
 ERPNext backup audit
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

The Mahogany digital platform is actively being developed and documented.

The repository structure and documentation will evolve as each system component is reviewed.

Major changes should be committed with clear commit messages and kept synchronized with the primary GitHub repository.

Notes for Contributors

Before making changes to production-related functionality:

Understand the existing business logic.
Check the current source and documentation.
Avoid destructive testing against production data.
Create appropriate backups before major changes.
Review the resulting changes before deployment.
Commit meaningful changes with descriptive commit messages.

Mahogany Decor Art
Digital Business Platform
Private Repository
