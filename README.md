# Flagship DevOps Portfolio 🚀

## What it is
Minimal production-style API used to demonstrate real DevOps workflow.

## Architecture
- FastAPI app
- Docker container
- Docker Compose
- CI/CD (GitHub Actions)
- EC2 deployment
- Terraform IaC (next phase)

## Run locally
```bash
docker build -t portfolio-app .
docker run -p 8080:8080 portfolio-app
