# Intro to Flask Routes Practice

## Getting Started

To get started, fork and clone the repo and then in your terminal run `pipenv install` followed by `pipenv shell`. Once you `cd server` run `python3 app.py` to run the server.

## Postman

You may find it easier to test your code with the Postman utility. You can find and install it here: https://www.postman.com/downloads/

## Deliverables

Your task is to create a variety of routes in your application. These are mostly here to test your ability to build routes as opposed to using SQL or building models (we'll work on that later).

### GET /time

This route responds with the current time as a string formatted like so:

`It is currently 11:59 on September 1 2023`

### PATCH /jeans

This route responds with:

`{ "message": "Your jeans have been patched" }`

### POST /add/<int:numberone>/<int:numbertwo>

This route responds with MATH. It will take numberone and numbertwo and return a response that adds the two numbers together.

If an invalid number or numbers are given, instead send an error message formatted like so:

`{ "error": "Numbers must be integers" }`

### GET /dadjoke

This route takes in a parameter of a dad joke subject as a string and makes a request. You may have to import additional libraries to make this work.

Make a request to `https://icanhazdadjoke.com/`. Additionally, use these headers:

`headers = {"Accept": "application/json"}`

If you don't include the headers in your request it will not respond correctly.

Once you've gotten a response from the dadjokes API, take the joke and forward it as a response to the original GET request.

The flow of this should look like so:

`POSTMAN/CURL --> FLASK --> icanhazdadjoke.com --> FLASK --> POSTMAN/CURL`

### GET /primes/<int:number>

This route responds with a list of prime numbers between 0 and the number sent as a parameter. The number must be between an integer between 1 and 100 inclusive.

If an invalid number is given, instead send an error message formatted like so:

`{ "error": "Number must be an integer between 0 and 100" }`

There are multiple ways of finding the prime numbers but bonus points to those who attempt to find them algorithmically. A prime is any number that's only divisible by itself and 1.

### POST /todo/<str:item>

This route accepts a string `item` as a parameter and attempts to write to a file named `TODO.txt`. You'll need to use python's built in I/O libraries to do this.

If you get stuck you can check out this blog on the `write()` function:
https://www.prepbytes.com/blog/python/write-function-in-python/

Once the operation is complete, this should return an empty dictionary as a response:
`{}`
