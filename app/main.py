from app.api_clients.weather_client import fetch_weather
from app.api_clients.currency_client import fetch_currency_rates
from app.api_clients.country_client import fetch_country_data

from app.services.normalize import (
    normalize_weather,
    normalize_currency,
    normalize_country
)

from app.services.validate import validate_record
from app.services.storage import store_record
from app.utils.logger import logger


def process_data(raw_data, normalizer):
    record = normalizer(raw_data)

    if validate_record(record):
        store_record(record)
        logger.info(f"Stored record from {record['source']}")
    else:
        logger.warning("Invalid record skipped")


def main():
    logger.info("API Ingestion Pipeline Started")

    weather_data = fetch_weather(51.5074, -0.1278)
    process_data(weather_data, normalize_weather)

    currency_data = fetch_currency_rates()
    process_data(currency_data, normalize_currency)

    country_data = fetch_country_data("United Kingdom")
    process_data(country_data, normalize_country)


if __name__ == "__main__":
    main()