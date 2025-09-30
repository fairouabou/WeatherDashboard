from flask import Flask, render_template, request, redirect, url_for
from utils.api_client import main as get_weather
from utils.storage import add_to_history, add_to_favorites, get_history, get_favorites

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
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
    city = request.form['city']
    country = request.form['country']
    add_to_favorites(city, country)
    return redirect(url_for('index'))

@app.route('/remove_favorite', methods=['POST'])
def remove_favorite_route():
    from utils.storage import remove_favorite
    city = request.form['city']
    country = request.form['country']
    remove_favorite(city, country)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
