import requests
import os
import geocoder

def get_weather():
    weather_api_key = os.getenv("WEATHER_API_KEY")
    lat_lng = get_lat_lng()
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat_lng[0]}&lon={lat_lng[1]}&exclude=minutely&appid={weather_api_key}&units=imperial"

    response = requests.get(url)
    data = response.json()
    print(data)
    weather = {
        
    }
    return weather


def get_lat_lng():
    my_location = geocoder.ip("me")
    return my_location.latlng


if __name__ in "__main__":
    get_weather()