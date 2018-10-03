#!/usr/bin/env python3

from flask import Flask, request, jsonify


# this allows for a string query
# GET - returns all books
# POST - add a book record
# PUT - bulk update records
# DELETE - bulk delete
# books? <param> = specify query parameters.
@app.route('/books', methods=['GET', 'POST', 'PUT', 'DELETE'])
def books():
    # error checking here for valid request.
        parameters = request.args
        json_obj = request.json


# this does not allow for a string query
# GET - returns specific record of books.
# POST - N/A
# PUT - Edit specific record
# DELETE - remove specific record
@app.route('/books/<record>', methods=['GET', 'PUT', 'DELETE'])
def books_record(record):
    json_obj = request.json

