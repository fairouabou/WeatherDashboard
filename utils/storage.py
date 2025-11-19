"""
Handles loading and saving user preferences (favorites and history) using a StorageService class.
Refactored to follow SOLID principles and improve testability.
"""

import json
import os


class StorageService:
    """
    Class responsible for managing loading and saving user data.
    This allows dependency injection and easy mocking during tests.
    """

    def __init__(self, file_path=None):
        if file_path is None:
            base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(base, "data", "preferences.json")
        self.file_path = file_path

    def _load(self):
        """Internal: load JSON data."""
        if not os.path.exists(self.file_path):
            return {"favorites": [], "history": []}
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _save(self, data):
        """Internal: save JSON data."""
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    # ---------- Public API ----------

    def get_history(self):
        return self._load().get("history", [])

    def get_favorites(self):
        return self._load().get("favorites", [])

    def add_to_history(self, city, country):
        data = self._load()
        entry = {"city": city, "country": country}

        if entry not in data["history"]:
            data["history"].insert(0, entry)
            data["history"] = data["history"][:5]

        self._save(data)

    def add_to_favorites(self, city, country):
        data = self._load()
        entry = {"city": city, "country": country}

        if entry not in data["favorites"]:
            data["favorites"].append(entry)

        self._save(data)

    def remove_favorite(self, city, country):
        data = self._load()
        data["favorites"] = [
            f for f in data["favorites"]
            if not (f["city"] == city and f["country"] == country)
        ]
        self._save(data)
