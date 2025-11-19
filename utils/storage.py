"""
Handles loading and saving user preferences (favorites and history) to a JSON file.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "data", "preferences.json")


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
    """Adds the user search entry (which includes city and country) to the top of the the history list.

    It stores only up to 5 unique entries and is trimmed to only keep this number of searches.

    Args: 
    - city (str): The name of the city.
    - country (str): The name of the country.
    """

    data = load_data()
    entry = {"city": city, "country": country}
    if entry not in data["history"]:
        data["history"].insert(0, entry)  
        data["history"] = data["history"][:5]  
    save_data(data)

def add_to_favorites(city, country):
    """Add a city to favorites if it's not already present."""
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
    """Returns the list of user search history entries."""
    return load_data().get("history", [])

def get_favorites():
    """Returns the list of favorite cities."""
    return load_data().get("favorites", [])
