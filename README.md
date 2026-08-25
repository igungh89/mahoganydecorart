# Mahogany Decor Art — Custom ERP Platform

A custom ERP platform built with **Frappe Framework and ERPNext**, extended to support the operational requirements of an event and wedding decoration business.

The project combines ERPNext's standard capabilities with custom business logic for **CRM, event management, purchasing, warehouse & inventory, rental operations, and business automation**.

> **Portfolio Project**
>
> This repository contains the public-facing source code and technical documentation of the Mahogany ERP project. Production credentials, databases, backups, and private infrastructure configuration are intentionally excluded.

---

## Project Overview

Event and wedding decoration businesses have operational requirements that do not always fit standard ERP workflows.

Mahogany ERP was designed to address those requirements while continuing to use ERPNext as the underlying ERP foundation.

The system covers the operational flow from:

```text
Client Inquiry
      ↓
Lead & CRM
      ↓
Availability & Capacity
      ↓
Booking
      ↓
Event Project
      ↓
Requirements & Allocation
      ↓
Purchasing / Warehouse
      ↓
Event Execution
      ↓
Returns & Inventory Updates
```

The objective is to build a system around the actual business process rather than forcing the business to adapt to a generic ERP workflow.

---

## Core Modules

### CRM

Custom CRM functionality manages the client lifecycle from initial inquiry through booking.

Example workflow:

```text
Client Inquiry
      ↓
Lead
      ↓
Availability Check
      ↓
Meeting / Follow-up
      ↓
Booking
      ↓
Event Project
```

Custom logic handles event dates, booking allocation, and operational capacity.

---

### Event Project

The Event Project layer connects the commercial process with operational execution.

It provides the foundation for:

* Event dates
* Service requirements
* Crew requirements
* Item requirements
* Project status
* Booking allocation
* Operational preparation

The architecture distinguishes between an **opportunity/slot** and an actual confirmed project.

This allows availability and capacity to be evaluated before a booking becomes an operational project.

---

### Purchasing

The purchasing module extends ERPNext to match the company's procurement workflow.

Key processes include:

* Purchase Request
* Purchase Order
* Goods Receipt
* Purchase Return
* Supplier / Business Partner management

Purchasing is connected with warehouse receiving and inventory operations so that procurement activities can flow into the operational inventory system.

---

### Warehouse & Inventory

Warehouse and inventory are one of the main custom development areas.

The system manages:

* Item Categories
* Item Master
* Individual Item Units
* Warehouse
* Locations
* Stock Movements
* Stock Opname
* Item Allocation

A key architectural decision is separating the **item definition** from the **physical item unit**.

For example:

```text
Item Master
"Chiavari Chair"
      │
      ├── CHAIR-0001
      ├── CHAIR-0002
      ├── CHAIR-0003
      └── CHAIR-0004
```

This allows reusable and asset-type inventory to be tracked individually, including its physical status and location.

---

## Item Lifecycle

The warehouse architecture supports different operational behaviors:

```text
Consumable
Reusable
Asset
Rental
```

Procurement and item lifecycle are intentionally separated.

This allows the system to distinguish between:

**How was the item acquired?**

and:

**How should the item behave operationally?**

This separation provides flexibility for future procurement and inventory workflows.

---

## Stock Movement

Stock operations are handled through a unified transaction model.

The intended lifecycle is:

```text
Draft
  ↓
Allocated / Reserved
  ↓
Completed / Submitted
  ↓
Cancelled
```

Important business rules include:

* Draft transactions do not automatically reserve stock.
* Physical cancellation of an OUT movement is handled through a return movement.
* Corrections are represented through reverse movements rather than silently modifying historical transactions.
* Individual units maintain their own physical status and location.
* Stock balance and individual-unit state are synchronized during movement processing.

The goal is to maintain a clear transaction history instead of relying on direct inventory quantity manipulation.

---

## Item Allocation

The allocation layer connects operational requirements with available inventory.

The architecture separates:

```text
Requirement
     ↓
Allocation
     ↓
Physical Item
     ↓
Event / Project
```

This allows inventory to be planned and allocated before the actual warehouse movement takes place.

For an event-based business, this is important because the same physical inventory may be required by different projects on different dates.

---

## Rental Management

Custom rental workflows are implemented for rental-oriented inventory.

The rental lifecycle is designed around the physical movement and condition of rented items:

```text
Rental Request
      ↓
Rental Order
      ↓
Rental Receipt
      ↓
Rental Inspection
      ↓
Rental Return
```

The inspection stage allows the operational condition of returned items to be handled as part of the rental workflow rather than treating the process as a simple sales transaction.

---

## Custom Development

The project extends ERPNext using the native capabilities of the Frappe Framework.

Custom development includes:

* Custom DocTypes
* Child Tables
* Client Scripts
* Server-side Python logic
* REST/API endpoints
* Custom workflows
* Workspace configuration
* Custom JavaScript
* Business validation
* Inventory synchronization
* Event-driven automation
* Custom web forms

The primary custom application is located under:

```text
custom-apps/mahogany/
```

Additional supporting applications are maintained under:

```text
custom-apps/
```

---

## Architecture

High-level architecture:

```text
                    ┌───────────────────┐
                    │       Users       │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Frappe / ERPNext  │
                    └─────────┬─────────┘
                              │
               ┌──────────────┼──────────────┐
               │              │              │
               ▼              ▼              ▼
        ┌────────────┐ ┌────────────┐ ┌────────────┐
        │  Mahogany  │ │  ERPNext   │ │   Custom   │
        │    App     │ │  Features  │ │   Logic    │
        └────────────┘ └────────────┘ └────────────┘
                              │
                              ▼
                       ┌────────────┐
                       │  MariaDB   │
                       └────────────┘

Supporting services:
- Redis
- Docker
- Reverse Proxy / SSL
```

The production environment is containerized using Docker.

---

## Technology Stack

| Layer            | Technology                 |
| ---------------- | -------------------------- |
| ERP Framework    | Frappe Framework           |
| ERP              | ERPNext                    |
| Backend          | Python                     |
| Frontend Logic   | JavaScript                 |
| Database         | MariaDB                    |
| Cache / Queue    | Redis                      |
| Containerization | Docker                     |
| Reverse Proxy    | Nginx-based infrastructure |
| Source Control   | Git / GitHub               |

---

## Repository Structure

```text
mahogany/
│
├── custom-apps/
│   ├── mahogany/
│   └── bypass_phone/
│
├── infrastructure/
├── n8n/
├── wordpress/
├── overrides/
├── development/
├── tests/
│
├── compose.yaml
├── pwd.example.yml
├── example.env
├── DEPLOY_RESTORE.md
└── README.md
```

The repository contains public source code and deployment templates.

Production credentials, databases, runtime volumes, and private configuration are intentionally excluded.

---

## Security & Configuration

The project separates **public configuration templates** from **private production configuration**.

Sensitive values such as:

* Database passwords
* Administrator passwords
* API credentials
* SSH keys
* Environment secrets
* Production databases
* Backups

are not intended to be stored in the public repository.

Public configuration uses environment variables instead of hard-coded credentials:

```yaml
MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}
MARIADB_ROOT_PASSWORD: ${DB_PASSWORD}
```

Production credentials are supplied separately during deployment.

---

## Engineering Approach

### Business-first Design

The system is designed around the actual operational workflow of the business.

### Reuse ERPNext Where Appropriate

Standard ERPNext functionality is used whenever it already solves the requirement.

Custom development is introduced where the business requires behavior beyond the standard ERPNext workflow.

### Single Source of Truth

Master data and operational state are designed around centralized models rather than duplicated information.

### Traceability

Important inventory changes are represented through transactions instead of silently overwriting historical state.

### Separation of Concerns

Master data, physical inventory units, requirements, allocation, and stock movement are treated as separate concepts.

---

## What This Project Demonstrates

This project demonstrates practical experience in:

* ERPNext customization
* Frappe Framework development
* Python backend development
* JavaScript client-side development
* Custom DocType architecture
* Business workflow design
* Inventory architecture
* Individual asset and unit tracking
* Rental management
* Purchasing workflows
* REST/API development
* Docker-based deployment
* Git-based development workflow
* Production-oriented infrastructure
* Security separation between source code and credentials

---

## Why Custom ERP?

Generic ERP software provides a strong foundation, but every business has operational rules that may not fit standard workflows.

The approach used in this project is:

```text
Business Requirement
        ↓
Business Process
        ↓
System Architecture
        ↓
ERPNext Foundation
        ↓
Custom Business Logic
        ↓
Operational Workflow
```

The result is an ERP platform adapted to the business rather than forcing the business to work around the ERP.

---

## Current Status

**Active development**

The platform is being developed incrementally, with modules introduced and refined according to operational requirements.

Some components are production-oriented while others remain under active development.

---

## Portfolio / Client Work

This repository demonstrates an approach that can be applied to custom business systems such as:

* ERP implementation
* ERPNext customization
* Inventory management
* Warehouse management
* Purchasing systems
* Rental management
* CRM workflows
* Business process automation
* API integrations
* Docker-based deployments

The focus is not simply on implementing software features, but on translating business processes into maintainable system architecture.

---

## License

This repository contains custom project work built on top of open-source technologies.

Refer to the individual application directories for applicable licensing information.

---

## Author

**Igun Gunawan, ST**

Custom ERP & Business Automation Developer

**ERPNext · Frappe · Python · JavaScript · Docker · Automation**
