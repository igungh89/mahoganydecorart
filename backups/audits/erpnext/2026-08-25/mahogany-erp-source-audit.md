# Mahogany ERPNext Backup & Source Audit

Date: 2026-08-25
Site: 
Bench site: frontend

## ERPNext Versions

- Frappe: 16.29.0
- ERPNext: 16.30.0
- Mahogany: 0.0.1
- bypass_phone: 0.0.1

## Installed Apps

- frappe
- erpnext
- mahogany
- bypass_phone

## ERPNext Backup

A full Frappe site backup was successfully created on 2026-08-25.

Backup command:

    bench --site frontend backup --with-files

Backup contents:

- Site configuration backup
- Database backup
- Public files backup
- Private files backup

The database backup is intentionally NOT stored in this Git repository.

## Backup Location

Generated inside the ERPNext container:

    /home/frappe/frappe-bench/sites/frontend/private/backups/

## Source Repository

Repository:

    git@github.com:igungh89/mahoganydecorart.git

ERPNext/custom application source is maintained in this repository.

## Repository Policy

GitHub contains source code, configuration/templates, infrastructure definitions,
and audit/backup metadata required to reproduce and maintain the Mahogany stack.

Production database dumps, runtime data, secrets, and generated ERPNext site
backups are intentionally excluded from Git.
