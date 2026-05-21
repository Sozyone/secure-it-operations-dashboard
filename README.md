# Secure IT Operations Dashboard
This is a DevOps and DevSecOps home lab project.

The goal is to build a small IT operations dashboard and use it to practice:
- Linux server administration
- Python Flask
- Git and GitHub
- Documentation
- Security thinking
- Docker
- GitHub Actions
- Security scanning
- Ansible
- Kubernetes later

## Current status
The project currently has a simple Flask web app. It shows basic IT system status information.
It also has a health endpoint at /health. The app can run with Python or inside Docker.

## Current DevOps and security features
- Dockerfile for containerizing the app
- GitHub Actions CI pipeline
- Gitleaks secret scanning
- Trivy Docker image vulnerability scanning
- Alpine based Python image to reduce vulnerabilities
- Ansible playbook for basic server setup
- Ansible syntax check in Github Actions
- Architecture documentation
- Runbook documentation
- Security notes documentation

## Run with Python
Activate the Python virtual environment:
source venv/bin/activate

Run the app:
python app.py

Test the app locally:
curl http://localhost:5000

Check the health endpoint:
curl http://localhost:5000/health

## Run with Docker
Build the Docker image:
docker build -t secure-it-dashboard .

Run the container:
docker run -p 5000:5000 secure-it-dashboard

Test the app locally:
curl http://localhost:5000

Check the health endpoint:
curl http://localhost:5000/health

## Long-term goal
The long-term goal is to turn this into a small but realistic DevSecOps portfolio project.
It will include deployment, automation, security scanning, monitoring, and documentation.
