# Security Notes

This document explains the basic security choices in the Secure IT Operations Dashboard project.

## SSH access

SSH is used to connect from Windows PowerShell to the Ubuntu Server VM.
The SSH key added to GitHub is used only for GitHub authentication.
The private SSH key must stay inside the VM and should never be shared.

## GitHub email privacy

Git is configured to use a GitHub noreply email.
This helps avoid exposing a personal email address in public commits.

## Docker ignore file

A .dockerignore file is used to keep unnecessary files out of Docker build.
This helps avoid copying local files, virtual environments, Git history, logs, editor files, and secrets into Docker image.

## Gitleaks secret scan

Gitleaks was added to the CI pipeline to scan the repository for secrets.
The purpose is to detect sensitive information like passwords, API keys, tokens,
private keys, and other secrets before they become a security problem.
The CI pipeline runs Gitleaks automatically on each push and pull request.

## Trivy image scan result

Trivy was added to the CI pipeline to scan the Docker image for vulnerabilities.
The first scan used the Debian based image python:3.12-slim.
That scan found 7 HIGH vulnerabilities and 0 CRITICAL vulnerabilities.
The vulnerabilities were found in the base operating system packages,
not in the Flask app or Python packages.

To reduce the attack surface, the Docker base image was changed to python:3.12-alpine.
After rebuilding and scanning again, Trivy reported 0 vulnerabilities.
This shows why container image scanning is useful.
Even a simple app can have vulnerabilities because of the base image.

## Basic Linux hardening

Ansible is used to apply basic Linux hardening on the Ubuntu Server VM.
The playbook installs and enables:

- ufw firewall
- fail2ban

The firewall is enabled and OpenSSH is allowed so SSH access still works.
fail2ban is enabled and running. It helps protect the server from failed login tries.
This is a basic first hardening step and will be improved later.

## Future security improvements

Later the project will include:
- Better deployment setup
- Monitoring and logging
- Stricter CI rules for security findings
