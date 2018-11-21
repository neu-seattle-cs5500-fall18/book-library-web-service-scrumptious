from flask_restplus import Api
from .books_api import ns as books_ns
from .checkouts_api import ns as checkouts_ns
from .users_api import ns as users_ns
# from .collections_api import ns as collections_ns

api = Api(
          title='Library Webservice API',
          version='1.0',
          description='An API for a rest-ful library webservice',
          )

api.add_namespace(books_ns)
api.add_namespace(checkouts_ns)
api.add_namespace(users_ns)
# api.add_namespace(collections_ns)
