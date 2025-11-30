# Deployment Guide — WeatherDashboard

This document describes how the WeatherDashboard application is deployed using Docker, Azure Container Registry, GitHub Actions, and Azure Web App for Containers.

## 1. Docker Image

The app is containerized using the Dockerfile:

- Base image: python:3.13-slim
- Install requirements
- Expose port 5001
- Run `app.py`

To build manually:
```bash
docker build -t weatherapp .
```

## 2. Azure Container Registry (ACR)
The GitHub Actions pipeline logs into:
ACR_LOGIN_SERVER = fairouzweatherdashboardregistry.azurecr.io
Secrets used:
- AZURE_CREDENTIALS
- ACR_LOGIN_SERVER
- AZURE_USERNAME
- AZURE_PASSWORD
- WEBAPP_NAME

## 3. CI/CD Pipeline
The CD pipeline:
- Logs into Azure
- Logs into ACR
- Builds Docker image
- Pushes image to ACR
- Deploys the updated image to Azure Web App

Pipeline location:
.github/workflows/cd.yml

## 4. Azure Web App for Containers

App Service configuration:
Image source: Azure Container Registry
Repository: weatherapp
Tag: latest
App setting:
WEBSITES_PORT = 5001

## 5. Final Deployment Flow
Push to main
GitHub Actions builds Docker image
Image is pushed to ACR
Azure Web App pulls latest image
App restarts automatically. 