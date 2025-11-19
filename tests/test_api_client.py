import pytest
from utils.api_client import WeatherService, WeatherData


@pytest.fixture
def weather_service():
    return WeatherService(api_key="TESTKEY")


def test_get_coordinates_success(requests_mock, weather_service):
    url = "http://api.openweathermap.org/geo/1.0/direct"

    mock_response = [
        {"lat": 40.4168, "lon": -3.7038}  # Madrid
    ]

    requests_mock.get(url, json=mock_response)

    lat, lon = weather_service.get_coordinates("Madrid", "ES")

    assert lat == 40.4168
    assert lon == -3.7038


def test_get_coordinates_failure(requests_mock, weather_service):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    requests_mock.get(url, json=[])

    lat, lon = weather_service.get_coordinates("UnknownCity", "ZZ")

    assert lat is None
    assert lon is None


def test_get_weather_success(requests_mock, weather_service):
    url = "https://api.openweathermap.org/data/2.5/weather"

    mock_response = {
        "weather": [{"main": "Clear", "description": "sunny", "icon": "01d"}],
        "main": {"temp": 25.5, "humidity": 40},
    }

    requests_mock.get(url, json=mock_response)

    data = weather_service.get_weather(
        lat=40.0, lon=-3.0, city="Madrid", country="ES"
    )

    assert isinstance(data, WeatherData)
    assert data.city == "Madrid"
    assert data.country == "ES"
    assert data.temperature == 25.5
    assert data.humidity == 40


def test_get_weather_failure(requests_mock, weather_service):
    url = "https://api.openweathermap.org/data/2.5/weather"
    requests_mock.get(url, status_code=500)

    data = weather_service.get_weather(
        lat=40, lon=-3, city="Madrid", country="ES"
    )

    assert data is None


def test_fetch_full_flow(requests_mock, weather_service):
    # Mock coordinates API
    geo_url = "http://api.openweathermap.org/geo/1.0/direct"
    requests_mock.get(geo_url, json=[{"lat": 10.0, "lon": 20.0}])

    # Mock weather API
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    requests_mock.get(weather_url, json={
        "weather": [{"main": "Clouds", "description": "overcast", "icon": "02d"}],
        "main": {"temp": 18.2, "humidity": 60}
    })

    data = weather_service.fetch("TestCity", "TC")

    assert isinstance(data, WeatherData)
    assert data.main == "Clouds"
    assert data.temperature == 18.2
    assert data.humidity == 60
