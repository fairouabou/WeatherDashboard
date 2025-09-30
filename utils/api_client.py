import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv("API_KEY")

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float
    humidity: int
    city: str
    country: str

def get_lan_lon(city_name, country_code, API_key):
    try:
        resp = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={API_key}",
            timeout=5
        )
        resp.raise_for_status()
        data = resp.json()

        if not data:  # no results
            return None, None

        lat, lon = data[0].get("lat"), data[0].get("lon")
        return lat, lon
    except Exception as e:
        print(f"Error in get_lan_lon: {e}")
        return None, None

def get_current_weather(lat, lon, API_key, city_name, country_name):
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