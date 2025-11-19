import pytest
from unittest.mock import MagicMock
from app import create_app


@pytest.fixture
def client(mocker):
    """
    Creates a test client with mocked WeatherService and StorageService.
    """
    # Mock WeatherService
    mock_weather = MagicMock()
    mock_weather.fetch.return_value = None  # default unless overridden
    mocker.patch("main.routes.weather_service", mock_weather)

    # Mock StorageService
    mock_storage = MagicMock()
    mock_storage.get_favorites.return_value = []
    mock_storage.get_history.return_value = []
    mocker.patch("main.routes.storage", mock_storage)

    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_get_home_page(client):
    """Test GET request renders the homepage."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Weather Dashboard" in response.data


def test_post_valid_city_country(client, mocker):
    """Test POST with valid data calls weather_service."""
    mock_weather = mocker.patch("main.routes.weather_service")
    mock_weather.fetch.return_value = None

    response = client.post("/", data={"cityName": "Madrid", "countryName": "ES"})
    assert response.status_code == 200

    mock_weather.fetch.assert_called_once_with("Madrid", "ES")


def test_post_missing_fields(client):
    """Test POST with missing form fields shows error."""
    response = client.post("/", data={"cityName": ""})

    assert response.status_code == 200
    assert b"Please enter both a city and a country code." in response.data


def test_add_favorite_route(client, mocker):
    """Test /favorite route."""
    mock_storage = mocker.patch("main.routes.storage")

    response = client.post("/favorite", data={"city": "Paris", "country": "FR"})
    assert response.status_code == 302  # redirect

    mock_storage.add_to_favorites.assert_called_once_with("Paris", "FR")


def test_remove_favorite_route(client, mocker):
    """Test /remove_favorite route."""
    mock_storage = mocker.patch("main.routes.storage")

    response = client.post("/remove_favorite", data={"city": "Paris", "country": "FR"})
    assert response.status_code == 302

    mock_storage.remove_favorite.assert_called_once_with("Paris", "FR")
