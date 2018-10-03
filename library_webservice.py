#!/usr/bin/env python3

from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# Root UrL to access service. Need to decide on this.
# probably return the json object for api schema
@app.route('/library/api')
def library_api():
    return make_response(jsonify("SCRUMptious Library Web Service"), 200)


if __name__ == '__main__':
    app.run(debug=True)
