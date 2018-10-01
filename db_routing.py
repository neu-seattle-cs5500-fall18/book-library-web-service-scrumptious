#!/user/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Function to query by received parameters.
# returns a dictionary of query results.
def get_books(parameters):
    # valid parameters check.
    # string together for valid sql query.
    return


# Function to retrieve record of a single book
def get_books(record):
    return


# Function to query Users by received parameters.
def get_users(parameters):
    return


# Function to get single user by record number.
def get_users(record):
    return


# Post
# function to post new book.
def post_books(json_obj):
    # valid json fields check
    return


# function to post new user
def post_users(json_obj):
    # valid json fields check
    return


# Put
# function to update books based on http query string and json object
def put_books(parameters, json_obj):
    # check valid json object, check valid parameters
    return


# function to update single record with json object
def put_books(record, json_obj):
    # check valid record valid json
    return


# function to update users based on http query string and json object
def put_users(parameters, json_obj):
    # check valide parameters, json object
    return


# function to update single user with json object info
def put_users(record, json_obj):
    # check valid record, valid json object
    return


# DELETE
# delete books according to http query parameters.
def delete_books(parameters):
    return


# delete specific record for book.
# what happens to all other primary key#?
def delete_books(record):
    return


# delete users based on http query parameters.
def delete_users(parameters):
    return


# delete single record user.
def delete_users(record):
    return
