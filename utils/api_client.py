"""
Handles interactions with the OpenWeatherMap API.
"""

import requests
from dataclasses import dataclass


@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float
    humidity: int
    city: str
    country: str


class WeatherService:
    """
    Service class responsible for fetching weather and geolocation data.
    Makes the code easier to test and follow SOLID principles.
    """

    GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"
    WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_coordinates(self, city_name, country_code):
        try:
            resp = requests.get(
                self.GEO_URL,
                params={"q": f"{city_name},{country_code}", "appid": self.api_key},
                timeout=5
            )
            resp.raise_for_status()
            data = resp.json()
            if not data:
                return None, None
            return data[0]["lat"], data[0]["lon"]
        except Exception:
            return None, None

    def get_weather(self, lat, lon, city, country):
        try:
            resp = requests.get(
                self.WEATHER_URL,
                params={
                    "lat": lat,
                    "lon": lon,
                    "appid": self.api_key,
                    "units": "metric"
                },
                timeout=5
            )
            resp.raise_for_status()
            data = resp.json()

            return WeatherData(
                main=data["weather"][0]["main"],
                description=data["weather"][0]["description"],
                icon=data["weather"][0]["icon"],
                temperature=data["main"]["temp"],
                humidity=data["main"]["humidity"],
                city=city,
                country=country
            )
        except Exception:
            return None

    def fetch(self, city, country):
        lat, lon = self.get_coordinates(city, country)
        if lat is None or lon is None:
            return None
        return self.get_weather(lat, lon, city, country)