import requests
import json
import geocoder

def get_weather():
    lat, lng = get_lat_lng()
    headers = {
        "User-Agent": "alarm-clock-app (your_email@example.com)",
        "Accept": "application/ld+json"
    }

    points_url = f"https://api.weather.gov/points/{lat},{lng}"
    points_resp = requests.get(points_url, headers=headers)
    location_data = points_resp.json()

    city = location_data["relativeLocation"]["city"]
    state = location_data["relativeLocation"]["state"]
    forecast_url = location_data["forecast"]

    forecast_resp = requests.get(forecast_url, headers=headers)
    forecast_resp.raise_for_status()
    forecast_data = forecast_resp.json()
    forecast_periods = forecast_data["periods"]
    

def get_lat_lng():
    my_location = geocoder.ip("me")
    return my_location.latlng


if __name__ in "__main__":
    get_weather()