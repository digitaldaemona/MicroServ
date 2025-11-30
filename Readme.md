# MicroServ: Modular Microservice Deployment & Management

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) 
[![Tech Stack](https://img.shields.io/badge/Tech-Flask%2C%20React%2C%20Docker-blue)](#technologies)
[![Status: Deployed](https://img.shields.io/badge/Status-Deployed-green)](https://msrv.digitaldaemona.com)

---

## Overview

MicroServ is the **central control plane** for managing the deployment, scaling, monitoring, and logging of all other microservices in the ecosystem. It demonstrates **DevOps principles** and **resource orchestration** by interacting directly with the Docker Engine API.

### Key Features
* **Deployment:** Launch and terminate microservice containers via CLI or UI.
* **Resource Management:** View current CPU/RAM usage and set resource limits/reservations for running containers.
* **Observability:** Centralized access to structured logs, service health status, and key Prometheus metrics.
* **API:** Flask backend with a dedicated API for managing the Docker environment.

---

## Getting Started (Local Development)

### Prerequisites

* **Docker** (Installed and running with sufficient resources)
* **Git**
* **Docker Compose**

### Installation and Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/digitaldaemona/MicroServ.git
    cd MicroServ
    ```

2.  **Build and Run Core Services:**
    *(This brings up the Nginx gateway, Flask backend, and React frontend.)*
    ```bash
    ???
    ```

3.  **Verify Setup:**
    *(This verifies msrv is setup and what resource limits it has.)*
    ```bash
    ???
    ```

---

## Usage

### Accessing the Management UI (React Frontend)

The main management dashboard is accessible through the Nginx gateway:

**Local URL:** `http://msrv.local.com`
**Remote URL:** `https://msrv.domain.com`

For local, ensure subdomains for msrv and services are registered in hosts file
For remote, ensure subdomains are registered to the server ip

### Using the CLI (Flask Backend)

While management and service removal is done using the frontend, deploying local code is done through the cli:

1.  **Deploy a new service:**
    ```bash
    ???
    ```

2.  **Update an existing service:**
    ```bash
    ???
    ```

3.  **Remove msrv and all microservices:**
    ```bash
    ???
    ```

---

## Technologies Used <a name="technologies"></a>

This project utilizes a multi-container microservice architecture built with:
* **Backend API:** Python (Flask/Gevent)
* **Orchestration:** Docker Compose / Docker Engine API
* **Frontend UI:** React / JavaScript
* **Database:** PostgreSQL

---

## Contributing & Contact

* **Author:** [Jarran Pedersen](https://digitaldaemona.com)
* **License:** MIT - See the [LICENSE](LICENSE) file for details.
