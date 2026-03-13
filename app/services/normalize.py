def normalize_weather(data: dict) -> dict:
    current = data.get("current_weather", {})

    return {
        "source": "weather",
        "temperature": current.get("temperature"),
        "windspeed": current.get("windspeed"),
        "time": current.get("time"),
    }


def normalize_currency(data: dict) -> dict:
    rates = data.get("rates", {})

    return {
        "source": "currency",
        "base": data.get("base"),
        "rates_count": len(rates),
    }


def normalize_country(data: dict) -> dict:
    return {
        "source": "country",
        "name": data.get("name", {}).get("common"),
        "capital": data.get("capital", ["Unknown"])[0],
        "population": data.get("population"),
    }