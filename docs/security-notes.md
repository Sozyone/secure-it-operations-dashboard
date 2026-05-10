# Security Notes

This document explains the basic security choices in the Secure IT Operations Dashboard project.

## Local lab only

The app currently runs only inside a local Ubuntu Server VM.
It is not exposed to the public internet.
This is safer while the project is still in the learning phase.

## No real data

The dashboard uses fake example systems and fake status information.
No real customer data, passwords, tokens, private keys, or sensitive information should be stored in this project.

## SSH access

SSH is used to connect from Windows PowerShell to the Ubuntu Server VM.
The SSH key added to GitHub is used only for GitHub authentication.
The private SSH key must stay inside the VM and should never be shared.

## GitHub email privacy

Git is configured to use a GitHub noreply email.
This helps avoid exposing a personal email address in public commits.

## Dependencies

Python dependencies are stored in requirements.txt.
This makes it easier to see what packages the project needs.

## Gitleaks secret scan

Gitleaks was added to the CI pipeline to scan the repository for secrets.
The purpose is to detect sensitive information like passwords, API keys, tokens,
private keys, and other secrets before they become a security problem.
The project should not contain real secrets or private information.
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

## Future security improvements

Later the project will include:

- Basic Linux hardening
- Better deployment setup
- Monitoring and logging
- Stricter CI rules for security findings
