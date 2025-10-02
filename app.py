"""
Main Flask application for the Weather Dashboard.
Handles user interface: 
- Searching for weather by city and country.
- Displaying current weather.
- Managing favorites (add and remove).
- Managing search history.

Utilizes utils/api_client.py for API interactions and utils/storage.py for data persistence.
"""

from flask import Flask, render_template, request, redirect, url_for
from utils.api_client import main as get_weather
from utils.storage import add_to_history, add_to_favorites, get_history, get_favorites

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main page to search for weather and display results.
    Handles both GET (display page) and POST (process search) requests.
    Args:
        None
    Returns:
        Rendered HTML page with weather data, error message (if any), history, and favorites.
    """

    data = None
    error = None

    if request.method == 'POST':
        city = request.form['cityName']
        country = request.form['countryName']
        data = get_weather(city, country)

        if not data:
            error = "Could not find weather for that location. Please check the city and country code."
        else:
            add_to_history(city, country)

    history = get_history()
    favorites = get_favorites()

    return render_template('index.html', data=data, error=error, history=history, favorites=favorites)

@app.route('/favorite', methods=['POST'])
def favorite():
    """
    Adds a city to the favorites list.
    Expects 'city' and 'country' in the form data.

    Args:
        None

    Returns:
        Redirects back to the main page.
    """
    
    city = request.form['city']
    country = request.form['country']
    add_to_favorites(city, country)
    return redirect(url_for('index'))

@app.route('/remove_favorite', methods=['POST'])
def remove_favorite_route():
    """
    Removes a city from the favorites list.
    Expects 'city' and 'country' in the form data. 

    Args:
        None

    Returns:
        Redirects back to the main page.
    """
    
    from utils.storage import remove_favorite
    city = request.form['city']
    country = request.form['country']
    remove_favorite(city, country)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
