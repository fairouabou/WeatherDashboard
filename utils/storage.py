import json
import os

FILE_PATH = "/Users/fairouz/Desktop/IE/YEAR3/SEM1/DevOPS/WeatherDashboard/data/preferences.json"


def load_data():
    """Load favorites and history from JSON file."""
    if not os.path.exists(FILE_PATH):
        return {"favorites": [], "history": []}
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    """Save favorites and history back to JSON file."""
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

def add_to_history(city, country):
    """Add a search entry to history (keep only last 5)."""
    data = load_data()
    entry = {"city": city, "country": country}
    if entry not in data["history"]:
        data["history"].insert(0, entry)  
        data["history"] = data["history"][:5]  
    save_data(data)

def add_to_favorites(city, country):
    """Add a city to favorites."""
    data = load_data()
    entry = {"city": city, "country": country}
    if entry not in data["favorites"]:
        data["favorites"].append(entry)
    save_data(data)

def remove_favorite(city, country):
    """Remove a city from favorites."""
    data = load_data()
    data["favorites"] = [f for f in data["favorites"] if not (f["city"] == city and f["country"] == country)]
    save_data(data)

def get_history():
    return load_data().get("history", [])

def get_favorites():
    return load_data().get("favorites", [])
