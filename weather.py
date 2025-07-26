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
    next_three_periods = forecast_periods[:3]

    return next_three_periods, city, state


def get_lat_lng():
    my_location = geocoder.ip("me")
    return my_location.latlng

def get_weather_icon(shortForecast):
    # Table mapping shortForecast in weather data to icon
    condition_to_icon = {
        "Severe storm": "rain",               # nsvrtsra
        "Showers storms": "rain",             # scttsra
        "Thunder storm": "rain",              # tsra
        "Chance Snow/Rain": "snow",           # rasn
        "Rain and Snow": "snow",              # rasn
        "Rain or Snow": "snow",               # rasn
        "Rain Sleet": "snow",                 # raip
        "FrzgRn Snow": "snow",                # fzra_sn
        "Freezing Rain": "snow",              # fzra
        "Rain likely": "rain",                # ra
        "Snow showers": "snow",               # sn
        "Showers likely": "rain",             # shra
        "Chance showers": "rain",             # shra
        "Isolated showers": "rain",           # shra
        "Scattered showers": "rain",          # shra
        "Chance rain": "rain",                # ra
        "Rain": "rain",                       # ra
        "Mix": "snow",                        # rasn
        "Sleet": "snow",                      # ip
        "Snow": "snow",                       # sn
        "Fog a.m.": "cloudy",                 # sctfg
        "Fog late": "cloudy",                 # sctfg
        "Fog": "cloudy",                      # fg
        "Very Cold": "snow",                  # cold
        "Very Hot": "sunny",                  # hot
        "Hot": "sunny",                       # hot
        "Overcast": "cloudy",                 # ovc
        "Mostly Cloudy": "cloudy",            # bkn
        "Partly Cloudy": "cloudy",            # sct
        "Cloudy": "cloudy",                   # cloudy
        "Partly Sunny": "cloudy",             # sct
        "Mostly Sunny": "sunny",              # few
        "Mostly Clear": "sunny",              # few
        "Sunny": "sunny",                     # skc
        "Clear": "sunny",                     # skc
        "Fair": "sunny",                      # few
        "Variable Clouds": "cloudy",          # bkn
    }

    return condition_to_icon[shortForecast]


if __name__ in "__main__":
    get_weather()