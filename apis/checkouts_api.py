from flask import request
from flask_restplus import Namespace, fields, Resource, reqparse
from model.checkout_dao import create_new_checkout, get_all_checkouts, get_checkout, update_checkout, delete_checkout, \
    get_reminder

api = Namespace('checkouts', description='Checkouts operations')

checkout_marshaller = api.model('Checkout', {
    'checkout_id': fields.Integer(readOnly=True, description='checkout id'),
    'user_id': fields.Integer(required=True, description='user who checks out the book'),
    'book_id': fields.Integer(required=True, description='the book that user checks out'),
    'checkout_date': fields.Date(required=True, description='the date that the book is checked out'),
    'due_date': fields.Date(required=True, desciription='the date that the checkout book is due'),
    'return_date': fields.Date(required=True, description='the date that the checkout book is returned'),
})

query_parser = reqparse.RequestParser()
query_parser.add_argument('checkout_id', required=False)
query_parser.add_argument('user_id', required=False)
query_parser.add_argument('book_id', required=False)
query_parser.add_argument('checkout_date', required=False)
query_parser.add_argument('due_date', required=False)
query_parser.add_argument('return_date', required=False)


@api.route('', endpoint='checkouts')
@api.response(code=400, description='Validation Error')
class Checkouts(Resource):

    @api.doc(body=query_parser, validate=True)
    @api.marshal_with(checkout_marshaller, code=200, description='Success')
    def get(self):
        """
        Queries the checkouts resource based on URL.
        :return: Json object of all checkouts that match the query parameter.
        """
        response = get_all_checkouts

        print('got all checkouts')
        return response

    @api.doc(body=checkout_marshaller, validate=True)
    @api.marshal_with(checkout_marshaller, code=201, description='Success')
    def post(self):
        """
        Create a new checkout for the book.
        :return: checkout_id for the create book
        """
        checkout_info = request.get_json()
        response = create_new_checkout(checkout_info)

        return response, 201


@api.route('/checkout/<checkout_id>')
@api.doc(params={'checkout_id': 'Record of a checkout'})
@api.response(code=400, description='Validation error')
class CheckoutRecord(Resource):
    @api.marshal_with(checkout_marshaller, code=200, description='Success')
    def get(self, checkout_id):
        """
        Gets a specific checkout record based on checkout_id.
        :param checkout_id: Record of a checkout.
        :return: JSON of requested checkout record.
        """
        checkout_record = get_checkout(checkout_id)
        return checkout_record

    @api.doc(body=checkout_marshaller, validate=True)
    @api.response(code=200, description='Success')
    def put(self, checkout_id):
        """
        Updates an existing checkout record based on checkout_id.
        :param checkout_id: Record checkout id to be updated.
        :return: Json with checkout_id of updated record.
        """
        print('Received PUT on resource /checkout/<checkout_id>')
        request_body = request.get_json()

        checkout_id = update_checkout(checkout_id, request_body)

        return checkout_id

    @api.response(code=200, description='Checkout deleted')
    def delete(self, checkout_id):
        """
        Delete a checkout record based on checkout_id.
        :param checkout_id: Record to be deleted.
        :return: Json of checkout_id of deleted record.
        """
        print('Received DELETE on resource /checkouts/<checkout_id>')

        id_of_deleted = delete_checkout(checkout_id)

        return id_of_deleted


@api.route('/checkout')
@api.response(code=400, description='Validation Error')
class Reminder(Resource):
    @api.doc(body=checkout_marshaller, validate=True)
    @api.marshal_with(checkout_marshaller, code=200, description="Success")
    def get(self):
        """
        Return the checkouts that have not been returned.
        :return: the checkouts that don't have a return date yet.
        """

        checkouts = get_reminder()
        return checkouts


