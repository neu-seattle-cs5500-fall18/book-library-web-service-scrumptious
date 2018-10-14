from flask_restplus import Api
from .books import api as books_ns
from .checkouts import api as checkouts_ns

api = Api(
    title='Library Webservice API',
    version='1.0',
    description='An API for a rest-ful library webservice',
    endpoint='library',
)

api.add_namespace(books_ns)
api .add_namespace(checkouts_ns)


