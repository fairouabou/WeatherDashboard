# WeatherDashboard

## Weather Dashboard built with Flask and OpenWeatherMap API. Features: search weather by city, manage favourites, and store recent searches using JSON persistence.

This project is a full-stack Weather Dashboard that allows users to search real-time weather conditions for any city, manage favourites, and track recent searches.
It features a clean UI/UX, responsive design, persistent JSON storage, Docker support, CI automation, Azure deployment, and Prometheus monitoring.

![CI](https://github.com/fairouzabou/WeatherDashboard2/actions/workflows/ci.yml/badge.svg)
![coverage](https://img.shields.io/badge/coverage-97%25-brightgreen)


## Features
- Real-time weather search by city and country
- Displays temperature, condition, humidity, and weather icons
- Manage Favorites (add/remove cities)
- Track Recent Searches (last 5 searches)
- Persistent JSON storage (preferences.json)
- Lightweight /health endpoint
- Prometheus-formatted /metrics endpoint
- Fully tested with pytest (97% coverage)
- GitHub Actions CI pipeline with coverage enforcement
- Docker containerization
- Azure Web App for Containers compatible 


## Project Structure
WeatherDashboard/
├── app.py                  # Main Flask entrypoint / app factory
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
├── pytest.ini              # Pytest configuration
│
├── data/
│   └── preferences.json    # Stores favorites + history
│
├── main/
│   ├── __init__.py         # Blueprint setup
│   ├── routes.py           # All HTTP routes
│   └── templates/
│       └── index.html      # Frontend UI
│
├── utils/
│   ├── api_client.py       # Calls OpenWeatherMap API
│   ├── storage.py          # JSON persistence logic
│   └── metrics.py          # Request count, latency, error metrics
│
├── tests/
│   ├── test_api_client.py
│   ├── test_routes.py
│   └── test_storage.py
│
├── Dockerfile              # Containerization
├── prometheus.yml          # Prometheus configuration
└── .github/
    └── workflows/
        └── ci.yml          # CI pipeline



## Requirements
Before installing and running this project, make sure you have:

- **Python 3.8+** installed on your system  
- A working **virtual environment** (recommended)  
- An **OpenWeatherMap API key** (free at [https://openweathermap.org/api](https://openweathermap.org/api))  

Python dependencies (also listed in `requirements.txt`):
- **Flask** – for the web framework
- **requests** – to make API calls
- **python-dotenv** – to load environment variables


## How to Install This Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/fairouabou/WeatherDashboard.git
   cd WeatherDashboard2

2. **Create and activate a virtual environment**
   ```bash
    python3 -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows

3. **Install dependencies**
   ```bash
    pip install -r requirements.txt


4. **Setup environment variables**
    *Create a .env file in the project root.
    *Add your OpenWeatherMap API key:
    API_KEY=your_api_key_here

5. **Run the application(app.py)**
   ```bash
    python app.py

6. **Open in browser**
    *Go to http://127.0.0.1:5000 to access the Weather Dashboard.


## Running tests: 
To run all tests: 
pytest -vv 

To run tests with coverage: 
pytest --cov=. --cov-report=term-missing --cov-report=xml

Viee HTML coverage report: 
htmlcov/index.html

Coverage is also stored in:
- .coverage
- coverage.xml
- htmlcov/ folder

## Continous Integration (CI):
This project includes a full CI pipeline using GitHub Actions:
- Runs all tests
- Measures code coverage
- Generates HTML & XML coverage reports
- Fails if coverage drops below 70%
- Builds the application by importing app.py

The pipeline is located at: 
.github/workflows/ci.yml


## Docker:
Build the Docker image
docker build -t weatherdashboard .

Run the container
Flask listens on port 5000 internally—host port mapped to 5001:

docker run -p 5001:5000 weatherdashboard

Open the dashboard at:

## Azure Deployment:
The app can be deployed using:
Azure Container Registry (ACR)
Azure Web App for Containers

**Deployment Steps**
- Build Docker image
- Tag and push to ACR
- Create Azure Web App for Containers
- Set container port to 5001
- Add environment variable in Azure:
WEATHER_API_KEY=<your_key>
- Start the web app: The cloud version behaves exactly like the local version.
https://weatherdashboard-fairouz-container-api-g7cxfuckcycbcqae.westeurope-01.azurewebsites.net

## Monitoring 
**Health Check**
- Check if the app is running:
http://localhost:5001/health

- Prometheus Metrics
http://localhost:5001/metrics

Metrics include:
- Total request count
- Total error count
- Average latency

**Run Prometheus**
Place prometheus.yml in your Prometheus installation folder
Run:
./prometheus --config.file=prometheus.yml
Open Prometheus UI: 
http://localhost:9090/query?g0.expr=weather_request_count&g0.show_tree=0&g0.tab=table&g0.range_input=1h&g0.res_type=auto&g0.res_density=medium&g0.display_mode=lines&g0.show_exemplars=0
Query:
- weather_request_count, 
- weather_error_count, 
- weather_request_latency_seconds.

## Expansion of the Project
Future improvements may include:
- Adding authentication for user-specific dashboards
- Migrating storage from JSON to PostgreSQL or Azure MySQL
- Enhancing UI with real-time weather graphs
- Docker Compose setup for multi-service architecture
- Deploying a full Prometheus + Grafana stack
- Adding logging aggregation using ELK or Azure Monitor


