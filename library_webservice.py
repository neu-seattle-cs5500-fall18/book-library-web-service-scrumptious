from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://lnvbfbgadkzbcx:ea44d8a7b2eb90295b602a8f34c9b450d699b0429cf97c5b932aae77f9c126c0@ec2-174-129-35-61.compute-1.amazonaws.com:5432/d7bpp6n8jmhhdo'

db = SQLAlchemy(app)

from model.user import User
from model.book import Book
from model.book_copy import BookCopy
from model.author import Author
from model.note import Note
from model.checkout import Checkout
from model.collection import BookCollection


#This Creates the Table in the DB.
user = User
author = Author
book = Book
book_copy = BookCopy
note = Note
checkout = Checkout
book_collection = BookCollection

db.create_all()

from apis import api

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
