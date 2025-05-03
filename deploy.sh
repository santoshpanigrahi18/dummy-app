#!/bin/bash

# Define variables
APP_DIR="/home/ubuntu/appdir"
ZIP_FILE="dummy-app.zip"
VENV_DIR="$APP_DIR/venv"
ARTIFACT_URL="https://trialnt381j.jfrog.io/artifactory/dummy-pypi-local/dummy-app.zip"

# Cleanup previous deployment
echo "Cleaning up old deployment..."
rm -rf "$APP_DIR"
mkdir -p "$APP_DIR"
cd "$APP_DIR"

# Download the artifact
echo "Downloading app zip from Artifactory..."
curl -u "$JFROG_USER:$JFROG_PASSWORD" -O "$ARTIFACT_URL"

# Unzip
echo "Unzipping app..."
unzip -o dummy-app.zip

# Setup virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

# Kill any existing app.py processes
echo "Killing any running app.py processes..."
pkill -f app.py || true

# Start the Flask app
echo "Starting Flask app..."
nohup venv/bin/python3 app.py > app.log 2>&1 &

echo "Deployment complete. App should be available shortly."
