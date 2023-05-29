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

@app.route("/educators")
def educators():
    educator_dict = {
         "educators": [
             {
                 "Name": "Oliver",
                 "Specialty": "Automated testing"
             },
             {
                 "Name": "Jairo",
                 "Specialty": "Discrete Mathematics"
             },
             {
                 "Name": "Amir",
                 "Specialty": "Web Development"
             },
             {
                 "Name": "Iryna",
                 "Specialty": "Database Engineering"
             },
             {
                 "Name": "George",
                 "Specialty": "Internet Security"
             },
         ]
     }
    return json.dumps(educator_dict)

# Example of dynamic routing
# @app.route("/<some_value>")
# def some_page(some_value):
#     return f"<p>You gave the value {some_value} in the route!</p>"

# Its better to do add a section of the route to specify its purpose to avoid colliding routes with the same name
@app.route("/some_page/<some_value>")
def some_page(some_value):
    return f"<p>You gave the value {some_value} in the route!</p>"

@app.route("/info")
def info_page():
    return "<p>This is the info page.</p>"