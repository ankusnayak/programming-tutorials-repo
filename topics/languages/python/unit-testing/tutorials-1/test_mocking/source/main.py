import requests


def get_weather(city):
    # Data fetch - GET Request
    response = requests.get(f"https://api.weather.com/v1/{city}")

    # 200: success
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Could not fetch weather data")
