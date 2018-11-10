from flask import request
from flask_restplus import abort, fields, Namespace, reqparse, Resource
from controller import book_checker


# this is to update authors directly.
api = Namespace('authors', description='')
