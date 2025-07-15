from flask import Flask, render_template
from datetime import datetime
from weather import get_weather
from oura import get_sleep_summary

app = Flask(__name__)

@app.route("/")
def index():
    time = datetime.now().strftime("%H:%M:%S")
    # weather = get_weather("Medford")
    sleep = get_sleep_summary()
    return render_template("index.html", time=time, sleep=sleep)

if __name__ == "__main__":
    app.run(debug=True)