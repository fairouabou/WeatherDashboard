"""
Handles interactions with the OpenWeatherMap API to fetch weather data based on city and country.
Provides functions to get latitude and longitude, as well as current weather information.
"""

import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

# Load API key from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

@dataclass
class WeatherData:
    """
    Data structure to hold weather information.

    Attributes:
        main (str): Main weather condition.
        description (str): Detailed weather description.
        icon (str): Icon code for the weather condition.
        temperature (float): Current temperature in Celsius.
        humidity (int): Current humidity percentage.
        city (str): City name.
        country (str): Country code.
    """
    
    main: str
    description: str
    icon: str
    temperature: float
    humidity: int
    city: str
    country: str

def get_lan_lon(city_name, country_code, API_key):
    """
    Fetches latitude and longitude for a given city and country using OpenWeatherMap Geocoding API.
     Args:
        city_name (str): The name of the city.
        country_code (str): The country code (e.g., "US" for the United States).
        API_key (str): Your OpenWeatherMap API key.
        Returns:
        tuple: A tuple containing latitude and longitude (lat, lon). Returns (None, None) if not found or on error.
    """

    try:
        resp = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={API_key}",
            timeout=5
        )
        resp.raise_for_status()
        data = resp.json()

        if not data:  
            return None, None

        lat, lon = data[0].get("lat"), data[0].get("lon")
        return lat, lon
    except Exception as e:
        print(f"Error in get_lan_lon: {e}")
        return None, None

def get_current_weather(lat, lon, API_key, city_name, country_name):
    """
    Fetches current weather data for given latitude and longitude using OpenWeatherMap Current Weather Data API
    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        API_key (str): Your OpenWeatherMap API key.
        city_name (str): The name of the city.
        country_name (str): The name of the country.
    
    Returns:
        WeatherData: An instance of WeatherData containing current weather information. Returns None on error.
    """

    if lat is None or lon is None:
        return None

    try:
        resp = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric",
            timeout=5
        )
        resp.raise_for_status()
        data = resp.json()

        if "weather" not in data or "main" not in data:
            return None

        return WeatherData(
            main=data["weather"][0]["main"],
            description=data["weather"][0]["description"],
            icon=data["weather"][0]["icon"],
            temperature=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            city=city_name,
            country=country_name
        )
    except Exception as e:
        print(f"Error in get_current_weather: {e}")
        return None

def main(city_name, country_name):
    """
    Main function to get weather data for a city and country.
    Args:
        city_name (str): The name of the city.
        country_name (str): The country code (e.g., "US" for the United States).
    
    Returns:
        WeatherData: An instance of WeatherData containing current weather information. Returns None on error.  
    """

    lat, lon = get_lan_lon(city_name, country_name, api_key)
    if lat is None or lon is None:
        return None
    return get_current_weather(lat, lon, api_key, city_name, country_name)

if __name__ == "__main__":
    result = main("Madrid", "ES")  
    if result:
        print(result)
    else:
        print("No weather data returned")