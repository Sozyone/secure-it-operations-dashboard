# Runbook

This runbook explains basic checks for the Secure IT Operations Dashboard.

## Start the app

Go to the project folder:

cd ~/secure-it-operations-dashboard

Activate the Python virtual environment:

source venv/bin/activate

Start the Flask app:

python app.py

## Stop the app

Press:

Ctrl + C

## Check if the app answers locally

Open another SSH terminal and run:

curl http://localhost:5000

If the app is running, HTML output should be shown in the terminal.

## Common problem: Flask is not installed

If this error appears:

ModuleNotFoundError: No module named 'flask'

Activate the virtual environment and install the requirements:

source venv/bin/activate
pip install -r requirements.txt

## Common problem: port 5000 is already in use

If port 5000 is busy, another app process may already be running.

Check running Python processes:

ps aux | grep python

Stop the old process if needed.

## Current limitation

The app currently runs only as a local development server.

Later, the project will use Docker, Nginx, and other tools for a more realistic deployment.
