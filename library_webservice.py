#!/usr/bin/env python3


from db_routing import get_books, post_books, put_books, delete_books, get_users, post_users, put_users, delete_users
from flask import Flask, make_response, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# Need a start point?  what about landing for library?
@app.route('/start')
def start_service():
    return make_response(jsonify("Starting Library Web Service"), 201)


# this allows for a string query
# GET - returns all books
# POST - add a book record
# PUT - bulk update records
# DELETE - bulk delete
# books? <param> = specify query parameters.
@app.route('/books', methods=['GET', 'POST', 'PUT', 'DELETE'])
def books():
    # error checking here.
        parameters = request.args
        json_obj = request.json
        if request.method == 'GET':
            response = jsonify(get_books(parameters))
            return response
        elif request.method == 'POST':
            post_books(json_obj)
        elif request.method == 'PUT':
            put_books(parameters, json_obj)
        elif request.method == 'DELETE':
            delete_books(parameters)


# this does not allow for a string query
# GET - returns specific record of books.
# POST - N/A
# PUT - Edit specific record
# DELETE - remove specific record
@app.route('/books/<record>/', methods=['GET', 'PUT', 'DELETE'])
def books(record):
    json_obj = request.json
    if request.method == 'GET':
        response = jsonify(get_books(record))
        return response
    if request.method == 'PUT':
        put_books(record, json_obj)
    if request.method == 'DELETE':
        delete_books(record)


# GET  - users?param= query by parameters
# GET - all users
# POST - new record
# PUT - bulk edit
# DELETE - delete all

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    parameters = request.args
    json_obj = request.json
    if request.method == 'GET':
        response = jsonify(get_users(parameters))
        return response
    elif request.method == 'POST':
        post_users(json_obj)
    elif request.method == 'PUT':
        put_users(parameters, json_obj)
    elif request.method == 'DELETE':
        delete_users(parameters)


# Is the api responsible for abstracting information?, GUID?
# GET - user record / how specify fields?, return all fields?
# PUT - edit user record.
# DELETE - remove user record.
@app.route('/users/<record>/', methods=['GET', 'PUT', 'DELETE'])
def users(record):
    json_obj = request.json
    if request.method == 'GET':
        return get_users(record)
    elif request.method == 'PUT':
        put_users(record, json_obj)
    elif request.method == 'DELETE':
        delete_users(record)


# root endpoint
# use Get to retrieve a list of all resource endpoints

if __name__ == '__main__':
    app.run(debug=True)
