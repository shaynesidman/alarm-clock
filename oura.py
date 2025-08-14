import os
import requests
from datetime import datetime
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

    # If no sleep data, return nothing
    if len(sleep_list) == 0:
        return {
        "avg_heart_rate": 0,
            "bedtime_start": "",
            "bedtime_end": "",
            "time_in_bed": 0,
            "total_sleep": 0,
        }

    return {
        "avg_heart_rate": int (sum(valid_heart_rates) / len(valid_heart_rates) + 0.5) if valid_heart_rates else 0,
        "bedtime_start": format_time(sleep_list[0].get("bedtime_start")),
        "bedtime_end": format_time(sleep_list[-1]["bedtime_end"]),
        "time_asleep": sum(entry["total_sleep_duration"] for entry in sleep_list),
        "efficiency": int(
            sum(entry["total_sleep_duration"] for entry in sleep_list)
            / sum(entry["time_in_bed"] for entry in sleep_list) * 100
        ),
    }


# Extracts time from long datetime object
def format_time(dt_str):
    dt = datetime.fromisoformat(dt_str)
    return dt.strftime("%I:%M %p")
