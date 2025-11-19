from main import main_bp
from flask import Blueprint, render_template, request, redirect, url_for
from utils.api_client import main as get_weather_data
from utils.storage import (
    add_to_history,
    add_to_favorites,
    remove_favorite,
    get_history,
    get_favorites,
)


@main_bp.route("/", methods=["GET", "POST"])
def index():
    data = None
    error = None

    if request.method == "POST":
        city = request.form.get("cityName")
        country = request.form.get("countryName")

        if city and country:
            data = get_weather_data(city, country)

            if data is None:
                error = "Could not find weather for that location."
            else:
                add_to_history(city, country)
        else:
            error = "Please enter both a city and a country code."

    favorites = get_favorites()
    history = get_history()

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
    add_to_favorites(city, country)
    return redirect(url_for("main.index"))

@main_bp.route("/remove_favorite", methods=["POST"])
def remove_favorite_route():
    city = request.form.get("city")
    country = request.form.get("country")
    remove_favorite(city, country)
    return redirect(url_for("main.index"))
