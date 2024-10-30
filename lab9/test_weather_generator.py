import pytest
from app import weather_generator

def test_weather_generator(mocker):
    cities = ["London", "Paris"]
    api_key = "test_api_key"
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"temp": 20, "weather": "Cloudy"}

    with mocker.patch('requests.get', return_value=mock_response):
        generator = weather_generator(cities, api_key)
        data = next(generator)
        assert data == {"temp": 30, "weather": "Sunny"}
        