#!/usr/bin/env python3

from flask import Flask, request, jsonify

from books import Books

app = Flask(__name__)


# Add, remove, update Books in library
# find books by particular author
# find books published within a date range
# find books on certain subject or genre
# combine the above
# mark books as loaned out
# add remove update notes about a book

# add remove update
# GET - returns all books - status code 200
# POST - add a book record - status code 201
# PUT - N/A
# DELETE - N/A
@app.route('/books', methods=['GET','POST'])
def books():
    # error checking here for valid request.
    if request.method == 'GET':
        response = Books.get()
        return jsonify(response)
    elif request.method == 'POST':
        response = Books.post(request.json)
        return jsonify(response)


# remove, update
# GET - returns specific record of books.
# POST - N/A
# PUT - Edit specific record
# DELETE - remove specific record
@app.route('/books/<BookID>', methods=['GET', 'PUT', 'DELETE'])
def books_record(BookID):
    return


# Optional param of first name ?
@app.route('/books/author/<author_first_name>/<author_last_name')
def books_by_author(author_first_name, author_last_name):
    return


# Books published within date range
# allow for wildcard for empyt date, but must have two params.
@app.route('books/publish_date/<epoch_start>/<epoch_end>')
def books_by_publish_date(epoch_start, epoch_end):
    return

#find by subject

#find by genre

# Get combination of above
# how to enforce only certain parameters?
# getbooks by multiple parameters.


# loanbook
