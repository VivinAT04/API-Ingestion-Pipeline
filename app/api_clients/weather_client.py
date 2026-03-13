import requests


def fetch_weather(latitude: float, longitude: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()