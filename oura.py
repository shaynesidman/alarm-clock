import os
import requests
from datetime import date
import json
from dotenv import load_dotenv
load_dotenv()

OURA_API_KEY = os.getenv("OURA_API_KEY")
HEADERS = { "Authorization": f"Bearer {OURA_API_KEY}" }

def get_sleep_summary():
    url = "https://api.ouraring.com/v2/usercollection/sleep"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    sleep_list = data["data"]
    valid_heart_rates = [entry["average_heart_rate"] for entry in sleep_list if entry["average_heart_rate"] != 0]

    return {
        "avg_heart_rate": sum(valid_heart_rates) / len(valid_heart_rates) if valid_heart_rates else 0,
        "bedtime_start": sleep_list[0].get("bedtime_start"),
        "bedtime_end": sleep_list[len(sleep_list) - 1]["bedtime_end"],
        "time_in_bed": sum(entry["time_in_bed"] for entry in sleep_list), # in seconds
        "total_sleep": sum(entry["total_sleep_duration"] for entry in sleep_list), # in seconds
    }