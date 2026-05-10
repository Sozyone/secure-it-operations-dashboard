# Architecture

This document explains the current structure of the Secure IT Operations Dashboard project.

## Current setup

The project is running in a local lab environment.

My Windows computer runs VirtualBox. Inside VirtualBox, I have an Ubuntu Server virtual machine.
The Flask web app runs inside the Ubuntu Server VM.

## Components

### Windows host

The Windows computer is the physical machine that runs VirtualBox.

### VirtualBox

VirtualBox is used to create and run the Ubuntu Server virtual machine.

### Ubuntu Server VM

The Ubuntu Server VM is the main lab server. It is used to run the app and practice Linux, Git, SSH, and later DevOps tools.

### Flask application

The Flask app is a small IT operations dashboard. It shows example systems and their status.

### GitHub repository

The GitHub repository stores the project code and documentation. It is also used to show project progress and version history.

### SSH access

SSH is used to connect from Windows Terminal to the Ubuntu Server VM. This makes it easier to work with the server.

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
Python Flask App
|
| stored in
v
GitHub Repository

## Current status

The project currently runs locally inside the Ubuntu Server VM.

The app is not exposed to the public internet. This is safer while the project is still in the early learning phase.

## Planned improvements

- Add Docker container support
- Add GitHub Actions
- Add security scanning
- Add Ansible automation
- Add Kubernetes later
- Add monitoring and logging later
