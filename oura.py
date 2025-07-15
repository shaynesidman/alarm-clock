import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

OURA_API_KEY = os.getenv("OURA_API_KEY")
HEADERS = { "Authorization": f"Bearer {OURA_API_KEY}" }

def get_sleep_summary():
    url = "https://api.ouraring.com/v2/usercollection/sleep"
    response = requests.get(url, headers=HEADERS)
    data = response.json()

    sleep_data = {
        "avg_heart_rate": data.get("data")[0].get("average_heart_rate"),
        "bedtime_start": data.get("data")[0].get("bedtime_start"),
        "bedtime_end": data.get("data")[0].get("bedtime_end"),
        "time_in_bed": data.get("data")[0].get("time_in_bed"), # in seconds
        "total_sleep": data.get("data")[0].get("total_sleep_duration"), # in seconds
    }
    
    return sleep_data

def get_activity_summary():
    url = "https://api.ouraring.com/v2/usercollection/daily_activity"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    if data and "data" in data and len(data["data"]) > 0:
        activity = data["data"][0]
        print({
            "calories": activity.get("cal_active"),
            "steps": activity.get("steps"),
            "score": activity.get("score")
        })
        return
    return {}

def get_heart_rate_summary():
    url = "https://api.ouraring.com/v2/usercollection/daily_hrv"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    if data and "data" in data and len(data["data"]) > 0:
        hrv = data["data"][0]
        return {
            "hrv_avg": hrv.get("rmssd"),
            "hrv_high": hrv.get("rmssd_5min", {}).get("high")
        }
    return {}


if __name__ in "__main__":
    get_sleep_summary()