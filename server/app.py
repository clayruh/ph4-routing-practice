#!/usr/bin/env python3

# IMPORTS #

from flask import Flask, request, make_response, jsonify
import requests
import pdb
from datetime import datetime

app = Flask(__name__)
app.json.compact = False

# ROUTES #
@app.get('/')
def index():
    return "Hello world"

@app.get('/time')
def get_time():
    now = datetime.now()
    date = now.strftime("%B %d, %Y")
    time = now.strftime("%H:%M")
    if time < "12:00":
        period = "AM"
    else:
        period = "PM"

    return f"It is currently {time} {period} on {date}"

@app.patch('/jeans')
def patch_jeans():
    return { "message": "Your jeans have been patched" }

# a bit unsure about this one
@app.post('/add/<int:numberone>/<int:numbertwo>')
def math(numberone, numbertwo):
    # don't really need this code because <int:numberone> already ensures that the numbers will be integers
    if type(numberone) != int or type(numbertwo) != int:
        return make_response(jsonify({"error": "Numbers must be integers"}))
    else:
        return make_response(jsonify({"sum": numberone + numbertwo}))
    
@app.get('/dadjoke')
def get_joke():
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers={"Accept": "application/json"})
    # why can't I do jsonify(response), 200
    return response.json(), 200

#     Make a request to https://icanhazdadjoke.com/. Additionally, use these headers:

# headers = {"Accept": "application/json"}

# If you don't include the headers in your request it will not respond correctly.

# Once you've gotten a response from the dadjokes API, take the joke and forward it as a response to the original GET request.

# The flow of this should look like so:

# POSTMAN/CURL --> FLASK --> icanhazdadjoke.com --> FLASK --> POSTMAN/CURL


# RUN #

if __name__ == '__main__':
    app.run(port=5555, debug=True)
