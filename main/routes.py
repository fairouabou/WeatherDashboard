from flask import Blueprint, render_template, request
from utils.api_client import get_weather_data
from utils.storage import (
    add_to_history,
    add_to_favorites,
    remove_favorite,
    get_favorites,
    get_history
)

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form.get("city")
        country = request.form.get("country")
        
        if city and country:
            add_to_history(city, country)
            weather_data = get_weather_data(city, country)
        else:
            weather_data = None
    else:
        weather_data = None

    favorites = get_favorites()
    history = get_history()

    return render_template(
        "index.html",
        weather_data=weather_data,
        favorites=favorites,
        history=history
    )

@main_bp.route("/add_favorite", methods=["POST"])
def add_favorite():
    city = request.form.get("city")
    country = request.form.get("country")
    if city and country:
        add_to_favorites(city, country)
    return ("", 204)

@main_bp.route("/remove_favorite", methods=["POST"])
def remove_favorite_route():
    city = request.form.get("city")
    country = request.form.get("country")
    if city and country:
        remove_favorite(city, country)
    return ("", 204)
