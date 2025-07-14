from flask import Flask, render_template
from datetime import datetime
from weather import get_weather

app = Flask(__name__)

@app.route("/")
def index():
    time = datetime.now().strftime("%H:%M:%S")
    weather = get_weather("Medford")
    return render_template("index.html", time=time, weather=weather)

if __name__ == "__main__":
    app.run(debug=True)