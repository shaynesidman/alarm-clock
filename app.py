from flask import Flask, render_template
from datetime import datetime
from weather import get_weather
from oura import get_sleep_summary
from googleCalendar import get_calendar_events

app = Flask(__name__)

@app.route("/")
def index():
    time = datetime.now().strftime("%H:%M:%S")
    weather = get_weather()
    sleep = get_sleep_summary()
    # events = get_calendar_events()
    return render_template("index.html", weather=weather, time=time, sleep=sleep)

if __name__ == "__main__":
    app.run(debug=True)