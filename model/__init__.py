# from flask_sqlalchemy import SQLAlchemy
# from flask_restplus import Api
# from flask import Flask
# from .books import api as books_ns
# from .checkouts import api as checkouts_ns
# from .users import api as users_ns
# from .collections import api as collections_ns
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lnvbfbgadkzbcx:ea44d8a7b2eb90295b602a8f34c9b450d699b0429cf97c5b932aae77f9c126c0@ec2-174-129-35-61.compute-1.amazonaws.com:5432/d7bpp6n8jmhhdo'
# api = Api(app)
# api.add_namespace(books_ns)
# api.add_namespace(checkouts_ns)
# api.add_namespace(collections_ns)
# api.add_namespace(users_ns)
# db = SQLAlchemy(app)
# db.create_all()