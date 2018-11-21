# from alembic import command
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
database_uri = os.environ.get("DATABASE_URL", "postgres://postgres@localhost:5432/booklibrary")
app.config['SQLALCHEMY_DATABASE_URI']=database_uri
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from apis import api
api.init_app(app)

#app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://lnvbfbgadkzbcx:ea44d8a7b2eb90295b602a8f34c9b450d699b0429cf97c5b932aae77f9c126c0@ec2-174-129-35-61.compute-1.amazonaws.com:5432/d7bpp6n8jmhhdo'


# from model.user import User
# from model.book import Book
# from model.book_copy import BookCopy
# from model.author import Author
# from model.note import Note

#This Creates the Table in the DB.
# user = User
# author = Author
# book = Book
# book_copy = BookCopy
# note = Note

#db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
