<<<<<<< HEAD
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



=======
# from flask import request
# from flask_restplus import abort, fields, Namespace, Resource
# from controller import collection_checker
#
# api = Namespace('collections', 'Book collections operations')
#
# # restplus automatically returns json object type.
# collection_marshaller = api.model('BookCollections', {
#     'collection_id': fields.Integer('The collection record'),
#     'book_ids': fields.List(fields.Integer('The book IDs')),
#     'title': fields.String('The book title.')
# })
#
#
# @api.route('', endpoint='collections')
# @api.response(200, 'Success')
# @api.response(400, 'Validation Error')
# class BookCollections(Resource):
#     @api.marshal_with(collection_marshaller, code=200)
#     def get(self):
#         """
#         Gets all users
#         :return: Json object of all users
#         """
#         print('Received GET on resource /collections')
#         # this should throw error if arg doesn't match the parser
#         collection = collection_checker.get_collections()
#         return collection
#
#     @api.expect(collection_marshaller, validate=True)
#     @api.response(201, 'Created')
#     def post(self):
#         """
#         Creates a new collection record for a single book.
#         :return: collection ID of the created record.
#         """
#         print('Received POST on resource /collections')
#         request_body = request.get_json()
#         print(request_body)
#         collection_id = collection_checker.create_collection(request_body)
#         return collection_id
#
#
# @api.route('/<collection_id>')
# @api.doc(params={'collection_id': 'Record of a collection.'})
# @api.response(200, 'Success')
# @api.response(400, 'Invalid input received for collection_id')
# class CollectionRecord(Resource):
#     @api.marshal_with(collection_marshaller, 200)
#     def get(self, collection_id):
#         """
#         Gets a specific collection record based on collection_id.
#         :param collection_id: Record of a collection.
#         :return: JSON of requested book collection.
#         """
#         print('Received GET on resource /collections/<collection_id>')
#         if collection_id.isdigit():
#             collection = collection_checker.get_collection(collection_id)
#             return collection
#         else:
#             abort(400, 'Invalid input received for collection_id')
#
#     @api.expect(collection_marshaller, validate=True)
#     @api.marshal_with(collection_marshaller, code=200)
#     def put(self, collection_id):
#         """
#         Updates an existing record  based on collection_id.
#         :param collection_id: Record number to be updated.
#         :return: collection_id of updated record.
#         """
#         print('Received PUT on resource /collections/<collection_id>')
#
#         if collection_id.isdigit():
#             request_body = request.get_json()
#             updated_id = collection_checker.update_collection(collection_id, request_body)
#             return updated_id
#         else:
#             abort(400, 'Invalid input received for collection_id')
#
#     @api.response(200, 'Deleted')
#     @api.marshal_with(collection_marshaller, code=200)
#     def delete(self, collection_id):
#         """
#         Delete a collection record based on collection_id.
#         :param collection_id: Record to be deleted.
#         :return: Json of collection_id of deleted record.
#         """
#         return
#
#     @api.route('/<collection_id>/add/<book_id>')
#     @api.response(code=400, description='Record not found')
#     @api.response(code=200, description='Success')
#     def put(self, collection_id, book_id):
#         """
#         Add a specific book for a collection.
#         :param collection_id: Record for a collection.
#         :param book_id: Record for a book in the collection.
#         :return: collection_id of edited record.
#         """
#         if book_id.isdigit() and collection_id.isdigit():
#             id = collection_checker.add_book_to_collection(collection_id)
#             return id
#         else:
#             abort(400, 'Invalid input for book_id or collection_id')
#
#     @api.route('/<collection_id>/delete/<book_id>')
#     @api.response(200, 'Deleted Book from collection')
#     @api.marshal_with(collection_marshaller, code=200)
#     def delete(self, collection_id, book_id):
#         """
#         Delete a specific book for a collection.
#         :param collection_id: Record for a collection.
#         :param book_id: Record for a book in the collection.
#         :return: collection_id of edited record.
#         """
#         if book_id.isdigit() and collection_id.isdigit():
#             id = collection_checker.delete_book_from_collection(collection_id)
#             return id
#         else:
#             abort(400, 'Invalid input for book_id or collection_id')
#
#
#
>>>>>>> 6ff5ea8bef1a7cee113a877d5392aa1cf26392a6
