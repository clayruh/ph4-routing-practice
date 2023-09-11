#!/usr/bin/env python3

# IMPORTS #

from flask import Flask, request

app = Flask(__name__)
app.json.compact = False

db.init_app(app)

# ROUTES #

@app.get('/')
def index():
    return "Hello world"

@app.get('/time')
def get_time():
    return "display the current time instead of this string"

# RUN #

if __name__ == '__main__':
    app.run(port=5555, debug=True)
