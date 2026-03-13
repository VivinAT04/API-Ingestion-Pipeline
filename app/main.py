from app.api_clients.weather_client import fetch_weather
from app.api_clients.currency_client import fetch_currency_rates
from app.api_clients.country_client import fetch_country_data


def main():
    print("API Ingestion Pipeline Started")

    weather_data = fetch_weather(51.5074, -0.1278)
    print("\nWeather Data:")
    print(weather_data)

    currency_data = fetch_currency_rates()
    print("\nCurrency Data:")
    print(currency_data)

    country_data = fetch_country_data("United Kingdom")
    print("\nCountry Data:")
    print(country_data)


if __name__ == "__main__":
    main()