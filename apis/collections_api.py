from flask_restplus import Namespace, Resource, fields

api = Namespace('collections', 'Book collections operations')

# restplus automatically returns json object type.
collection_marshaller = api.model('BookCollections', {
    'collection_id': fields.Integer('The collection record'),
    'book_id': fields.Integer('The book record'),
    'title': fields.String('The book title.'),
})


@api.route('', endpoint='bookcollections')
class BookCollections(Resource):
    @api.marshal_with(collection_marshaller)
    @api.response(200, 'Resource successfully gotten')
    def get(self):
        """
        Gets all collections of books
        :return: Json object of all collections of books
        """
        book_col = []
        book = BookCollection(
            44, 1, "Harry"
        )
        book_col.append(book)
        return book_col



