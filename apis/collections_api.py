from flask import request
from flask_restplus import abort, fields, Namespace, Resource
from controller import collection_checker

ns = Namespace('collections', 'Book collections operations')

book_title_marshaller = ns.model('BookTitleMarshaller',{
    'book_id': fields.Integer('Id of a book record.'),
    'title' : fields.String('Title of a book')
})

# restplus automatically returns json object type.
collection_marshaller = ns.model('BookCollections', {
    'collection_id': fields.Integer('The collection record'),
    'book_ids': fields.List(fields.Nested(book_title_marshaller), description='The book IDs and title'),
    'title': fields.String('The book title.')
})


@ns.route('', endpoint='collections')
@ns.response(200, 'Success')
@ns.response(400, 'Validation Error')
class BookCollections(Resource):

    @ns.expect(collection_marshaller, validate=True)
    @ns.response(201, 'Created')
    def post(self):
        """
        Creates a new collection record for a list of books.
        :return: collection ID of the created record.
        """
        print('Received POST on resource /collections')
        request_body = request.get_json()
        print(request_body)
        collection_id = collection_checker.create_collection(request_body)
        return collection_id


@ns.route('/<collection_id>')
@ns.doc(params={'collection_id': 'Record of a collection.'})
@ns.response(200, 'Success')
@ns.response(400, 'Invalid input received for collection_id')
class CollectionRecord(Resource):
    @ns.marshal_with(collection_marshaller, 200)
    def get(self, collection_id):
        """
        Gets a specific collection record based on collection_id.
        :param collection_id: Record of a collection.
        :return: JSON of requested book collection.
        """
        print('Received GET on resource /collections/<collection_id>')
        if collection_id.isdigit():
            collection = collection_checker.get_collection(collection_id)
            return collection
        else:
            abort(400, 'Invalid input received for collection_id')

    @ns.response(200, 'Deleted')
    @ns.marshal_with(collection_marshaller, code=200)
    def delete(self, collection_id):
        """
        Delete a collection record based on collection_id.
        :param collection_id: Record to be deleted.
        :return: Json of collection_id of deleted record.
        """
        return


@ns.route('/<collection_id>/books/<book_id>')
@ns.doc(params={'collection_id': 'A record for a collection.', 'book_id': 'A record for a book.'})
@ns.response(200, 'Success')
@ns.response(400, 'Validation Error')
class BookCollections(Resource):
    @ns.expect(collection_marshaller, validate=True)
    @ns.marshal_with(collection_marshaller, code=200)
    def put(self, collection_id, book_id):
        """
        Updates an existing record  based on collection_id and book_id.
        :param collection_id: Record number to be updated.
        :param book_id: Record number to be added.
        :return: collection_id of updated record.
        """
        print('Received PUT on resource /collections/<collection_id>/books/<book_id>')

        if collection_id.isdigit() and book_id.isdigit():
            updated_collection = collection_checker.add_book_to_collection_id(collection_id, book_id)
            return updated_collection
        else:
            abort(400, 'Invalid input received for collection_id or book_id')

    @ns.response(204, 'Deleted')
    @ns.marshal_with(collection_marshaller, code=204)
    def delete(self, collection_id, book_id):
        """
        Deletes an existing record  based on collection_id and book_id.
        :param collection_id: Record number to be updated.
        :param book_id: Record number to be deleted.
        :return: collection_id of updated record.
        """
        print('Received DELETE on resource /collections/<collection_id>/books/<book_id>')
        if book_id.isdigit() and collection_id.isdigit():
            result = collection_checker.delete_book_from_collection_id(collection_id, book_id)
            return result, 204
        else:
            abort(400, 'Invalid input for book_id or collection_id')