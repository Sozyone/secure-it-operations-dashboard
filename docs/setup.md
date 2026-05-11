# Setup Guide

This document explains how to rebuild this DevOps and DevSecOps lab from a clean Ubuntu Server VM.

This guide is written for a new project. Replace placeholder values like `<GITHUB_USERNAME>`, `<REPO_NAME>`, and `<GITHUB_NOREPLY_EMAIL>` with your own values.

## 1. Base environment

The lab uses:

- Windows host computer
- VirtualBox
- Ubuntu Server VM
- GitHub repository
- Python Flask app
- Docker
- GitHub Actions
- Gitleaks
- Trivy

## 2. VirtualBox and Ubuntu Server

Create a new Ubuntu Server VM in VirtualBox.

Suggested settings:

- RAM: 2048 MB minimum
- CPU: 2 cores
- Disk: 40 GB
- Network: NAT
- OpenSSH server: enabled during Ubuntu installation

Optional VirtualBox NAT port forwarding for SSH:

```text
Name: SSH
Protocol: TCP
Host IP: 127.0.0.1
Host Port: 2222
Guest IP: leave empty
Guest Port: 22
```

Connect from Windows PowerShell:

```bash
ssh <UBUNTU_USERNAME>@127.0.0.1 -p 2222
```
## 3. Ubuntu Server setup

Update Ubuntu:

```bash
sudo apt update
sudo apt upgrade
```

Install basic tools:

```bash
sudo apt install git curl nano python3 python3-venv python3-pip openssh-server
```

Tools used:

- `git`: version control and GitHub work
- `curl`: test web endpoints and download files
- `nano`: terminal text editor
- `python3`: Python runtime
- `python3-venv`: Python virtual environments
- `python3-pip`: Python package installer
- `openssh-server`: allows SSH access into the VM

## 4. GitHub repository setup

Create a new public GitHub repository.

Clone the repository:

```bash
git clone git@github.com:<GITHUB_USERNAME>/<REPO_NAME>.git
```

Go into the project folder:

```bash
cd <REPO_NAME>
```

Check Git status:

```bash
git status
```

## 5. Git identity

Set Git username:

```bash
git config --global user.name "<YOUR_NAME>"
```

Set GitHub noreply email:

```bash
git config --global user.email "<GITHUB_NOREPLY_EMAIL>"
```

Check Git settings:

```bash
git config --global user.name
git config --global user.email
```

## 6. SSH key for GitHub

Create an SSH key:

```bash
ssh-keygen -t ed25519 -C "<GITHUB_NOREPLY_EMAIL>"
```

Press Enter to use the default save location.

Show the public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Add the public key to GitHub:

```text
GitHub Settings
SSH and GPG keys
New SSH key
Paste the public key
```

Test GitHub SSH access:

```bash
ssh -T git@github.com
```

## 7. Basic project files

Create the Flask app file:

```bash
nano app.py
```

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install Flask:

```bash
pip install flask
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

Run the app:

```bash
python app.py
```

Test the app in another SSH terminal:

```bash
curl http://localhost:5000
```

Stop the app:

```text
Ctrl + C
```

## 8. Docker installation

Install required packages:

```bash
sudo apt install ca-certificates curl
```

Create the keyrings folder:

```bash
sudo install -m 0755 -d /etc/apt/keyrings
```

Download Docker's signing key:

```bash
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
```

Make the key readable:

```bash
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Add the Docker repository:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Update package lists:

```bash
sudo apt update
```

Install Docker:

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Test Docker:

```bash
sudo docker run hello-world
```

Allow the current user to run Docker without sudo:

```bash
sudo usermod -aG docker $USER
```

Log out and back in from server, then test:

```bash
docker run hello-world
```

## 9. Dockerfile

Create the Dockerfile:

```bash
nano Dockerfile
```

Build the Docker image (use a name for your image):

```bash
docker build -t secure-it-dashboard .
```

Run the container:

```bash
docker run -p 5000:5000 secure-it-dashboard
```

Test the app:

```bash
curl http://localhost:5000
```

Test the health endpoint:

```bash
curl http://localhost:5000/health
```

Stop the running container:

```text
Ctrl + C
```

## 10. GitHub Actions CI

Create the workflow folder:

```bash
mkdir -p .github/workflows
```

Create the CI workflow file:

```bash
nano .github/workflows/ci.yml
```

## 11. Security scanning

Gitleaks checks the repository for exposed secrets.

Trivy checks the Docker image for vulnerabilities.

## 12. Useful Git commands

Check changed files:

```bash
git status
```

Prepare one file for commit:

```bash
git add FILENAME
```

Prepare all changed files:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Commit message"
```

Push changes to GitHub:

```bash
git push
```

See commit history:

```bash
git log --oneline
```

## 13. Suggested documentation files

Suggested `docs` folder:

```text
docs/
  architecture.md
  runbook.md
  security-notes.md
  setup.md
```
