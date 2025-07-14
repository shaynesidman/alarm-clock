import requests
import os
import geocoder

def get_weather(lat=42.3601, lon=-71.0589):
    headers = {
        'User-Agent': 'MyAlarmClockApp (you@example.com)',
        'Accept': 'application/ld+json'
    }

    # Step 1: Get grid/forecast URL
    point_url = f"https://api.weather.gov/points/{lat},{lon}"
    point_response = requests.get(point_url, headers=headers).json()
    print(point_response)
    forecast_url = point_response["forecastZone"]

    # Step 2: Get the actual forecast
    forecast_response = requests.get(forecast_url, headers=headers).json()
    print(forecast_response)
    period = forecast_response["properties"]["periods"][0]

    return {
        "name": period["name"],
        "temp": f"{period['temperature']}°{period['temperatureUnit']}",
        "shortForecast": period["shortForecast"]
    }



def get_lat_lng():
    my_location = geocoder.ip("me")
    return my_location.latlng


if __name__ in "__main__":
    get_weather()