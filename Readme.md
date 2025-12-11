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

For local development, ensure domain and subdomains for msrv and services are registered in hosts file (e.g. `msrv.local.com`)
For server deployment, ensure domain and subdomains are registered to the server ip

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
