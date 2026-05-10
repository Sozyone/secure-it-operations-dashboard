
# Security Notes

This document explains the basic security choices in the Secure IT Operations Dashboard project.

## Local lab only

The app currently runs only inside a local Ubuntu Server VM.

It is not exposed to the public internet. This is safer while the project is still in the learning phase.

## No real data

The dashboard uses fake example systems and fake status information.

No real customer data, passwords, tokens, private keys, or sensitive information should be stored in this project.

## SSH access

SSH is used to connect from Windows using PowerShell to the Ubuntu Server VM.

The SSH key added to GitHub is used only for GitHub authentication.

The private SSH key must stay inside the VM and should never be shared.

## GitHub email privacy

Git is configured to use a GitHub noreply email.

This helps avoid exposing a personal email address in public commits.

## Dependencies

Python dependencies are stored in requirements.txt.

This makes it easier to see what packages the project needs.

## Future security improvements

Later the project will include:

- Secret scanning with Gitleaks
- Vulnerability scanning with Trivy
- Docker image scanning
- GitHub Actions security checks
- Basic Linux hardening
- Better deployment setup

