# Architecture

## Local lab flow

    Windows PC
        |
        | VirtualBox
        v
    Ubuntu Server VM
        |
        | SSH from PowerShell
        |
        | Ansible setup
        | - basic packages
        | - ufw firewall
        | - fail2ban
        |
        | Docker
        v
    Docker Container
        |
        | Docker HEALTHCHECK
        | checks /health
        v
    Flask App
        |
        | endpoints
        v
    /          dashboard
    /health   health check
    /metrics  monitoring metrics

## CI and security flow

    Local code change
        |
        | git add
        | git commit
        | git push
        v
    GitHub Repository
        |
        | triggers
        v
    GitHub Actions CI
        |
        | security and build checks
        v
    Gitleaks
        |
        | checks for secrets
        v
    Python setup
        |
        | installs dependencies
        v
    Flask import check
        |
        | checks app basics
        v
    Ansible syntax check
        |
        | checks playbook format
        v
    Docker image build
        |
        | uses Alpine Python image
        v
    Trivy image scan
        |
        | checks vulnerabilities
        v
    Latest result:
    0 vulnerabilities

## Future monitoring flow

    Flask App
        |
        | exposes /metrics
        v
    Prometheus
        |
        | collects metrics
        v
    Grafana
        |
        | shows dashboards
        v
    IT operations monitoring
