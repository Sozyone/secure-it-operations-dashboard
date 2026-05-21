# Runbook
This runbook explains basic checks for the Secure IT Operations Dashboard.

## Start the app with Python
Go to the project folder:
cd ~/secure-it-operations-dashboard

Activate the Python virtual environment:
source venv/bin/activate

Start the Flask app:
python app.py

## Start the app with Docker
Go to the project folder:
cd ~/secure-it-operations-dashboard

Build the Docker image:
docker build -t secure-it-dashboard .

Run the container:
docker run -p 5000:5000 secure-it-dashboard

## Stop the app
If the app is running in the terminal, press:
Ctrl + C

## Check if the app answers locally
Open another SSH terminal and run:
curl http://localhost:5000
If the app is running, HTML output should be shown in the terminal.

## Check the health endpoint
curl http://localhost:5000/health
Expected result:
{"status":"healthy"}

## Check Docker container health

When the app is running in Docker, check container status:
docker ps
If the health check is working, the STATUS column should show: healthy
The Docker health check uses the /health endpoint inside the container.
