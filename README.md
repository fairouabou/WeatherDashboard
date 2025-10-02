# WeatherDashboard

## Weather Dashboard built with Flask and OpenWeatherMap API. Features: search weather by city, manage favourites, and store recent searches using JSON persistence.

This project consists of a Weather Dashboard which displays the weather condition and related information regarding a city that a user enters. The Dashabord interacts with the user through UI/UX, and is both user-friendly & intuitive. 

## Features
- Search real-time weather by city and country  
- Display temperature, condition, humidity, and weather icons  
- Manage **Favorites** (add/remove cities)  
- Track **Recent Searches** (last 5 searches)  
- Store user preferences in a local JSON file  
- Simple and responsive **UI/UX** with Bootstrap  

## Project Structure
WeatherDashboard/
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Git ignore rules
├── .env # Environment variables (ignored in Git)
│
├── data/
│ └── preferences.json # Stores favorites and recent searches
│
├── templates/
│ └── index.html # Frontend UI (Bootstrap + Jinja2)
│
└── utils/
├── api_client.py # Handles API requests to OpenWeatherMap
└── storage.py # JSON storage logic for favorites & history

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
   cd WeatherDashboard

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


