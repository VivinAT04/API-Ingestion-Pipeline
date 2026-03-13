import requests


def fetch_country_data(country_name: str = "United Kingdom") -> dict:
    url = f"https://restcountries.com/v3.1/name/{country_name}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    return data[0]