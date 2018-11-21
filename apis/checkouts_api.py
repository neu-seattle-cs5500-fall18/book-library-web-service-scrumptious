from flask import request
from flask_restplus import Namespace, fields, Resource, reqparse
from controller import checkout_checker

ns = Namespace('checkouts', description='Checkouts operations')

checkout_marshaller = ns.model('Checkout', {
    'checkout_id': fields.Integer(readOnly=True, description='checkout id'),
    'user_id': fields.Integer(required=True, description='user who checks out the book'),
    'book_id': fields.Integer(required=True, description='the book that user checks out'),
    'book_copy_id': fields.Integer(required=True, description="the specific copy of the book for checkout"),
    'checkout_date': fields.Date(required=True, description='the date that the book is checked out'),
    'due_date': fields.Date(required=True, desciription='the date that the checkout book is due'),
    'return_date': fields.Date(required=True, description='the date that the checkout book is returned'),
})

#parser
query_parser = reqparse.RequestParser()
query_parser.add_argument('checkout_id', required=False)
query_parser.add_argument('user_id', required=False)
query_parser.add_argument('book_id', required=False)
query_parser.add_argument('book_copy_id', required=False)
query_parser.add_argument('checkout_date', required=False)
query_parser.add_argument('due_date', required=False)
query_parser.add_argument('return_date', required=False)


@ns.route('', endpoint='checkouts')
@ns.response(code=400, description='Validation Error')
class Checkouts(Resource):

    @ns.doc(body=query_parser, validate=True)
    @ns.marshal_with(checkout_marshaller, code=200, description='Success')
    def get(self):
        """
        Queries the checkouts resource based on URL.
        :return: Json object of all checkouts that match the query parameter.
        """
        response = checkout_checker.get_all_checkouts

        print('got all checkouts')
        return response


@ns.route('/user/<user_id>/book/<book_id>')
@ns.response(code=400, description='Validation Error')
class CreateCheckout(Resource):

    @ns.marshal_with(checkout_marshaller, code=201, description='Success')
    def post(self, user_id, book_id):
        """
        Create a new checkout for the book.
        :return: checkout_id for the create book
        """
        response = checkout_checker.create_checkout(user_id, book_id)

        return response, 201


@ns.route('/<checkout_id>')
@ns.doc(params={'checkout_id': 'Record of a checkout'})
@ns.response(code=400, description='Validation error')
class CheckoutRecord(Resource):
    @ns.marshal_with(checkout_marshaller, code=200, description='Success')
    def get(self, checkout_id):
        """
        Gets a specific checkout record based on checkout_id.
        :param checkout_id: Record of a checkout.
        :return: JSON of requested checkout record.
        """
        checkout_record = checkout_checker.get_checkout(checkout_id)
        return checkout_record

    @ns.doc(body=checkout_marshaller, validate=True)
    @ns.response(code=200, description='Success')
    def put(self, checkout_id):
        """
        Update an existing checkout when the checked-out book is returned.
        :param checkout_id: Record checkout id to be updated.
        :return: Json with checkout_id of updated record.
        """
        print('Received PUT on resource /checkout/<checkout_id>')

        checkout_id = checkout_checker.update_checkout(checkout_id)

        return checkout_id

    @ns.response(code=200, description='Checkout deleted')
    def delete(self, checkout_id):
        """
        Delete a checkout record based on checkout_id.
        :param checkout_id: Record to be deleted.
        :return: Json of checkout_id of deleted record.
        """
        print('Received DELETE on resource /checkouts/<checkout_id>')

        id_of_deleted = checkout_checker.delete_checkout(checkout_id)

        return id_of_deleted



