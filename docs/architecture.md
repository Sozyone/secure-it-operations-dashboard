# Architecture

This document explains the current structure of the Secure IT Operations Dashboard project.

## Current setup

The project is running in a local lab environment.
My Windows computer runs VirtualBox. Inside VirtualBox, I have an Ubuntu Server virtual machine.
The Flask web app runs inside the Ubuntu Server VM and can also run inside a Docker container.

## Components

### Windows host

The Windows computer is the physical machine that runs VirtualBox and connects to the Ubuntu Server VM with SSH.

### VirtualBox

VirtualBox is used to create and run the Ubuntu Server virtual machine.

### Ubuntu Server VM

The Ubuntu Server VM is the main lab server.
It is used to run the app and practice Linux, Git, SSH, Docker, and later more DevOps tools.

### Flask application

The Flask app is a small IT operations dashboard. It shows example systems and their status.
It also has a `/health` endpoint that can be used to check if the app is running.

### Docker

Docker is used to package and run the Flask app in a container. The project uses a Dockerfile to build the image.

### GitHub repository

The GitHub repository stores the project code and documentation. It is also used to show project progress and version history.

### GitHub Actions

GitHub Actions runs the CI pipeline when code is pushed.
The pipeline checks Python dependencies, builds the Docker image, runs Gitleaks secret scanning, and runs Trivy image scanning.

### SSH access

SSH is used to connect from Windows PowerShell to the Ubuntu Server VM. This makes it easier to work with the server.

## Simple architecture diagram

    Windows PC
        |
        | runs
        v
    VirtualBox
        |
        | runs
        v
    Ubuntu Server VM
        |
        | runs
        v
    Docker Container
        |
        | runs
        v
    Python Flask App
        |
        | code and documentation stored in
        v
    GitHub Repository
        |
        | triggers
        v
    GitHub Actions CI

## Current status

The project currently runs locally inside the Ubuntu Server VM.
The app can run directly with Python or inside a Docker container.
The app is not exposed to the public internet. This is safer while the project is still in the learning phase.

## Current DevOps and security features

- Flask web app
- Health endpoint
- Dockerfile
- Docker container build
- GitHub Actions CI pipeline
- Gitleaks secret scanning
- Trivy image vulnerability scanning
- Documentation and runbook

## Planned improvements

- Add Ansible automation
- Add basic Linux hardening
- Add monitoring and logging
- Add Kubernetes later
- Add stricter CI rules for security findings
