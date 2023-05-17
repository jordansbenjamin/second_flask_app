from flask import Flask
import json
from datetime import datetime

app = Flask("__name__")

@app.route("/")
def homepage():
    return """<p>Hi, welcome to my API! Here are the endpoints that are available:</p>
            <ul>
                <li>Current time: /time</li>
                <li>Educator Info: /educators</li>
            </ul>"""

@app.route("/time")
def current_time():
    time_dict = {"current time": str(datetime.now().strftime('%H:%M'))}
    return json.dumps(time_dict)