from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    current_time = datetime.now().strftime("%H:%M:%S")
    return render_template("index.html", time=current_time)

if __name__ == "__main__":
    app.run(debug=True)