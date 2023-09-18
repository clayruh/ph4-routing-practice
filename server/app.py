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
    # difference between using requests.get from importing requests vs request from Flask?
    response = requests.get(url, headers={"Accept": "application/json"})
    # why can't I do jsonify(response), 200
    return response.json(), 200

#     Make a request to https://icanhazdadjoke.com/. Additionally, use these headers:

# headers = {"Accept": "application/json"}

# If you don't include the headers in your request it will not respond correctly.

# Once you've gotten a response from the dadjokes API, take the joke and forward it as a response to the original GET request.

# The flow of this should look like so:

# POSTMAN/CURL --> FLASK --> icanhazdadjoke.com --> FLASK --> POSTMAN/CURL

@app.get('/primes/<int:number>')
def get_primes(number):
    if 1 <= number <= 100:
        numbers = [n + 1 for n in range(number) if n%3 == 1]
    # prime numbers are only divisible by itself and 1
        return numbers
    else: 
        return jsonify({"error": "Number must be an integer between 1 and 100"})

# This route responds with a list of prime numbers between 0 and the number sent as a parameter. The number must be between an integer between 1 and 100 inclusive.

# There are multiple ways of finding the prime numbers but bonus points to those who attempt to find them algorithmically. A prime is any number that's only divisible by itself and 1.

@app.post('/todo/<path:item>')
def add_todo(item):
    data = request.json

    return jsonify({"hello world"}), 201


# RUN #

if __name__ == '__main__':
    app.run(port=5555, debug=True)
