# CI/CD Pipeline with GitHub Actions, Docker, and Kubernetes

## Project Overview

This project demonstrates an automated CI/CD pipeline for a FastAPI application using GitHub Actions, Docker, Docker Hub, and Kubernetes with Minikube.

When code is pushed to the `main` branch, the pipeline runs automated tests, builds a Docker image, pushes the image to Docker Hub, deploys the application to Kubernetes, and verifies its health.

The goal is to demonstrate how application testing, containerization, deployment, and health verification can be automated using DevOps tools.

## Technologies Used

- **Python** — Application programming language
- **FastAPI** — Web framework for building the API
- **Pytest** — Automated application testing
- **Docker** — Containerization of the application
- **Docker Hub** — Storage and distribution of Docker images
- **GitHub Actions** — CI/CD workflow automation
- **Kubernetes** — Application deployment and management
- **Minikube** — Kubernetes cluster for deployment testing
- **Git and GitHub** — Version control and source code hosting

## Project Structure

```text
ci-cd-local-deployment/
├── .github/
│   └── workflows/
│       └── ci.yml
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── tests/
│   └── test_main.py
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ahmadali238051-a11y/ci-cd-local-deployment.git
cd ci-cd-local-deployment
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 5. Verify the application

Open these URLs in your browser:

- Home endpoint: http://127.0.0.1:8000/
- Health endpoint: http://127.0.0.1:8000/health
- Interactive API documentation: http://127.0.0.1:8000/docs

## Run Tests

Run the automated tests using Pytest:

```bash
python -m pytest -v
```

The tests verify the application's home and health endpoints.

GitHub Actions runs these tests automatically before building and publishing the Docker image.

## Docker

The application is containerized using Docker and published to Docker Hub.

**Docker Hub Image:** https://hub.docker.com/r/w616/ci-cd-local-deployment

### Pull the image

```bash
docker pull w616/ci-cd-local-deployment:latest
```

### Run the container

```bash
docker run --rm -p 8000:8000 w616/ci-cd-local-deployment:latest
```

Access the application at http://127.0.0.1:8000/.

If port 8000 is already in use, stop the other application using that port before running the container.

## Kubernetes Deployment

The application is deployed to Kubernetes using Minikube.

Kubernetes configuration files:

- `k8s/deployment.yaml` — Defines the Deployment and container configuration.
- `k8s/service.yaml` — Exposes the application through a NodePort Service.

The GitHub Actions workflow applies these manifests, waits for the Deployment rollout to complete, and checks the application's `/health` endpoint.

The Minikube cluster created by GitHub Actions is temporary and exists only during the workflow run. It does not deploy the application to a permanent production cluster.

## CI/CD Pipeline Workflow

The GitHub Actions workflow is defined in `.github/workflows/ci.yml`.

It runs when code is pushed to the `main` branch or when a pull request targets `main`.

### Pipeline Steps

1. **Checkout Code** — Downloads the repository source code.
2. **Set Up Python** — Configures Python 3.12 on the GitHub Actions runner.
3. **Install Dependencies** — Installs packages listed in `requirements.txt`.
4. **Run Tests