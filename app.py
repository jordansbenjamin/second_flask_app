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

