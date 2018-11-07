from flask import request
from flask_restplus import Namespace, Resource, fields
from model.collection_dao import get_all_collections, create_new_collection,add_book_to_collection_id, \
    delete_book_from_collection_id, get_collection, delete_collection

api = Namespace('collections', 'Book collections operations')

# restplus automatically returns json object type.
collection_marshaller = api.model('BookCollections', {
    'collection_id': fields.Integer('The collection record'),
    'book_id': fields.Integer('The book record'),
    'title': fields.String('The book title.'),
})


@api.route('')
class BookCollections(Resource):
    @api.marshal_with(collection_marshaller, code=200)
    def get(self):
        """
        Gets all users
        :return: Json object of all users
        """
        print('Received GET on resources /users')
        response = get_all_collections()

        return response

    @api.response(400, 'Record not found')
    @api.response(201, 'Created new collection.')
    @api.expect(collection_marshaller)
    def post(self):
        """
        Creates a new book collection.
        :return: collection ID of the created record.
        """
        print('Received POST on resource /collections')

        collection_info = request.get_json()
        response = create_new_collection(collection_info)

        return response, 201


@api.route('/<collection_id>', endpoint='book_collections')
@api.doc(params={'collection_id': 'An ID for a collection record'})
class BookCollectionRecord(Resource):
    @api.marshal_with(collection_marshaller)
    def get(self, collection_id):
        print('Received GET on collection /collections/<collection_id>')

        collection_record = get_collection(collection_id)

        return collection_record

    @api.route('/<collection_id>/add/<book_id>', endpoint='book_collections')
    @api.response(code=400, description='Record not found')
    @api.response(code=200, description='Success')
    def put(self, collection_id, book_id):
        """
        Updates an existing collection record based on collection_id.
        :param collection_id: Record number to be updated.
        :return: Json with collection_id of updated record.
        """
        print('Received PUT on resource /collections/<collection_id>/<book_id>')

        collection_id = add_book_to_collection_id(collection_id, book_id)

        return collection_id

    @api.route('/<collection_id>/delete/<book_id>', endpoint='book_collections')
    @api.response(code=400, description='Record not found')
    @api.response(code=200, description='Success')
    def put(self, collection_id, book_id):
        """
        Updates an existing collection record based on collection_id.
        :param collection_id: Record number to be updated.
        :return: Json with collection_id of updated record.
        """
        print('Received PUT on resource /collections/<collection_id>/<book_id>')

        collection_id = delete_book_from_collection_id(collection_id, book_id)

        return collection_id

    @api.response(code=200, description='Collection deleted')
    def delete(self, collection_id):
        """
        Delete a collection based on collection_id.
        :param collection_id: Collection to be deleted.
        :return: Json of collection_id of deleted record.
        """
        print('Received DELETE on resource /collections/<collection_id>')

        id_of_deleted_collection = delete_collection(collection_id)

        return id_of_deleted_collection


