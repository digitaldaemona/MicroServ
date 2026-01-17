# MicroServ: Modular Microservice Deployment & Management

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) 
[![Tech Stack](https://img.shields.io/badge/Tech-Flask%2C%20React%2C%20Docker-blue)](#technologies)
[![Status: Deployed](https://img.shields.io/badge/Status-Deployed-green)](https://msrv.digitaldaemona.com)

---

## Overview

MicroServ is the **central control plane** for managing the deployment, scaling, monitoring, and logging of all other microservices in the ecosystem. It demonstrates **DevOps principles** and **resource orchestration** by interacting directly with the Docker Engine API.

### Key Features
* **Deployment:** Launch and terminate microservice containers via UI.
* **Resource Management:** View current CPU/RAM usage and set resource limits/reservations for running containers.
* **Observability:** Centralized access to structured logs, service health status, and key Prometheus metrics.
* **API:** Flask backend with a dedicated API for managing the Docker environment.

---

## File Structure

```
msrv/
├── .github/
│   └── workflows/
│       ├── backend-ci-cd.yml          # Build & push backend images
│       └── frontend-ci-cd.yml         # Build & push frontend images
│
├── backend/
│   ├── Dockerfile                     # Multi-stage: dev & prod targets
│   ├── requirements.txt
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py                    # Flask app entry
│   │   ├── api/                       # API routes
│   │   └── services/                  # Docker socket logic
│   └── tests/
│
├── frontend/
│   ├── Dockerfile                     # Multi-stage: build & serve
│   ├── package.json
│   ├── src/
│   │   ├── app.jsx                    # Management UI
│   │   └── components/
│   └── public/
│
├── config/
│   ├── nginx/
│   │   ├── nginx.conf                 # Main config
│   └── postgres/
│       ├── postgresql.conf            # Tuned for 200MB limit
│       └── init.sql                   # Schema initialization
│
├── cli/
│   ├── setup.py                       # Click CLI package
│   └── msrv/
│       ├── __init__.py
│       ├── cli.py                     # Main CLI entry (deploy/update/remove)
│       ├── commands/
│       │   ├── deploy.py              # Deploy logic
│       │   └── remove.py              # Cleanup logic
│       ├── templates/
│       │   ├── docker-compose.dev.yml
│       │   └── docker-compose.prod.yml
│       └── utils/
│           ├── docker_client.py       # Docker API wrapper
│           └── remote_ssh.py          # Remote deployment via SSH
│
├── .env.example                       # Environment variables template
├── .dockerignore
├── .gitignore
├── README.md                          # Project overview
├── LICENSE
└── CHANGELOG.md
```

---

## Getting Started (Local Development)

### Prerequisites

* **Python**
* **Git**
* **Docker** (Installed and running with sufficient resources)
* **Docker Compose**

### Installation and Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/digitaldaemona/MicroServ.git
    cd MicroServ
    ```

---

## Usage

### Accessing the Management UI (React Frontend)

The main management dashboard is accessible through the Nginx gateway:

**URL:** `https://msrv.domain.com`

For local development, ensure domain and subdomains for msrv and services are registered in hosts file (e.g. `msrv.local.com`). For server deployment, ensure domain and subdomains are registered to the server ip.

---

## Technologies Used <a name="technologies"></a>

This project utilizes a multi-container microservice architecture built with:
* **Orchestration:** Docker Compose / Docker Engine API
* **Database:** PostgreSQL
* **Backend API:** Python (Flask) / Nginx
* **Monitoring:** Loki Stack (Prometheus / Promtail / cAdvisor / Loki / Grafana)
* **Frontend UI:** React / JavaScript

---

## Contributing & Contact

* **Author:** [Jarran Pedersen](https://digitaldaemona.com)
* **License:** MIT - See the [LICENSE](LICENSE) file for details.
