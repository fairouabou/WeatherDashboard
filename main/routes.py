from flask import render_template, request, redirect, url_for
from main import main_bp
from utils.api_client import WeatherService
from utils.storage import StorageService
import os

# Load API key and prepare services
API_KEY = os.getenv("API_KEY")
weather_service = WeatherService(API_KEY)

# Build file path for preferences.json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREF_PATH = os.path.join(BASE_DIR, "data", "preferences.json")

storage = StorageService(PREF_PATH)


@main_bp.route("/", methods=["GET", "POST"])
def index():
    data = None
    error = None

    if request.method == "POST":
        city = request.form.get("cityName")
        country = request.form.get("countryName")

        if city and country:
            data = weather_service.fetch(city, country)

            if data is None:
                error = "Could not find weather for that location."
            else:
                storage.add_to_history(city, country)
        else:
            error = "Please enter both a city and a country code."

    favorites = storage.get_favorites()
    history = storage.get_history()

    return render_template(
        "index.html",
        data=data,
        error=error,
        favorites=favorites,
        history=history
    )


@main_bp.route("/favorite", methods=["POST"])
def favorite():
    city = request.form.get("city")
    country = request.form.get("country")
    storage.add_to_favorites(city, country)
    return redirect(url_for("main.index"))


@main_bp.route("/remove_favorite", methods=["POST"])
def remove_favorite_route():
    city = request.form.get("city")
    country = request.form.get("country")
    storage.remove_favorite(city, country)
    return redirect(url_for("main.index"))
