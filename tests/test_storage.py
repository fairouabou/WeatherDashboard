import os
import json
import tempfile
from utils.storage import StorageService


def create_temp_storage():
    """Create a temporary JSON file initialized with empty structure."""
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(b'{"favorites": [], "history": []}')
    tmp.close()
    return tmp.name


def test_add_and_get_history():
    path = create_temp_storage()
    storage = StorageService(path)

    storage.add_to_history("Madrid", "ES")
    history = storage.get_history()

    assert len(history) == 1
    assert history[0] == {"city": "Madrid", "country": "ES"}


def test_add_and_get_favorites():
    path = create_temp_storage()
    storage = StorageService(path)

    storage.add_to_favorites("Paris", "FR")
    favorites = storage.get_favorites()

    assert len(favorites) == 1
    assert favorites[0] == {"city": "Paris", "country": "FR"}


def test_remove_favorite():
    path = create_temp_storage()
    storage = StorageService(path)

    storage.add_to_favorites("Paris", "FR")
    storage.remove_favorite("Paris", "FR")

    assert storage.get_favorites() == []
