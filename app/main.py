from app.api_clients.weather_client import fetch_weather


def main():
    print("API Ingestion Pipeline Started")
    weather_data = fetch_weather(51.5074, -0.1278)
    print(weather_data)


if __name__ == "__main__":
    main()