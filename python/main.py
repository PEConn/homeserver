#!/usr/bin/env python3
from bottle import Bottle, request, route, run

app = Bottle()

@app.route('/')
def hello():
    name = request.query.name or "Peter"
    return "Hello " + name

app.run(host="localhost", port=8080, debug=True)
