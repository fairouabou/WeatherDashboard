from flask import Flask, render_template, request
from utils import api_client
from utils.api_client import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form['cityName']
        country = request.form['countryName']
        data = get_weather(city, country)
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)