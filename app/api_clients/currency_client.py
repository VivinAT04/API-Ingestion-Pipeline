import requests


def fetch_currency_rates(base: str = "USD") -> dict:
    url = f"https://open.er-api.com/v6/latest/{base}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()