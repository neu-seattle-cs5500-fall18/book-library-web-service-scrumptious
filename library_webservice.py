#!/usr/bin/env python3
from flask import Flask, make_response, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/start')
def start_service():
    return make_response(jsonify("Starting Library Web Service"), 201)


if __name__ == '__main__':
    app.run(debug=True)
