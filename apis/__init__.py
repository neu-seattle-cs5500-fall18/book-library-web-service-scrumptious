
from flask_restplus import Api
from .books import api as books_ns
from .checkouts import api as checkouts_ns
from .users import api as users_ns
from .collections import api as collections_ns

api = Api(
          title='Library Webservice API',
          version='1.0',
          description='An API for a rest-ful library webservice',
          )

api.add_namespace(books_ns)
api.add_namespace(checkouts_ns)
api.add_namespace(collections_ns)
api.add_namespace(users_ns)

