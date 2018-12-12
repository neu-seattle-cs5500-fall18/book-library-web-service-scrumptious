from flask import request, jsonify
from flask_restplus import Namespace, fields, Resource, reqparse, abort
from controller import checkout_checker
from controller.checkout_checker import get_all_checkouts, get_checkout, create_checkout, update_checkout, delete_checkout

ns = Namespace('checkouts', description='Checkouts operations')

checkout_marshaller = ns.model('Checkout', {
    'checkout_id': fields.Integer(readOnly=True, description='checkout id'),
    'user_id': fields.Integer(required=True, description='user who checks out the book'),
    'book_id': fields.Integer(required=True, description='the book that user checks out'),
    'book_copy_id': fields.Integer(required=True, description="the specific copy of the book for checkout"),
    'checkout_date': fields.Date(required=True, description='the date that the book is checked out'),
    'due_date': fields.Date(required=True, desciription='the date that the checkout book is due'),
    'return_date': fields.Date(required=False, description='the date that the checkout book is returned'),
})

checkout_input_marshaller = ns.model('CheckoutInput', {
    'user_id': fields.Integer(required=True, description='user who checks out the book'),
    'book_id': fields.Integer(required=True, description='the book that user checks out'),
    'book_copy_id': fields.Integer(required=True, description="the specific copy of the book for checkout"),
    'checkout_date': fields.Date(required=True, description='the date that the book is checked out'),
    'due_date': fields.Date(required=True, desciription='the date that the checkout book is due'),
    'return_date': fields.Date(required=False, description='the date that the checkout book is returned'),
})


@ns.route('', endpoint='checkouts')
@ns.response(code=400, description='Validation Error')
class Checkouts(Resource):

    @ns.marshal_with(checkout_marshaller, code=200, description='Success')
    def get(self):
        """
        Queries the checkouts resource based on URL.
        :return: Json object of all checkouts that match the query parameter.
        """
        response = get_all_checkouts()
        return response

    @ns.expect(checkout_input_marshaller)
    def post(self):
        """
        Create a new checkout for the book.
        :return: checkout_id for the create book
        """
        checkout_info = request.get_json()
        response = create_checkout(checkout_info)
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

    @ns.doc(body=checkout_input_marshaller, validate=True)
    @ns.marshal_with(checkout_marshaller, 200)
    def put(self, checkout_id):
        """
        Update an existing checkout when the checked-out book is returned.
        :param checkout_id: Record checkout id to be updated.
        :return: Json with checkout_id of updated record.
        """
        print('Received PUT on resource /checkout/<checkout_id>')

        if checkout_id.isdigit():
            request_body = request.get_json()
            checkout = update_checkout(checkout_id, request_body)
            return checkout
        else:
            return abort(400, 'Invalid input for user_id in url')

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



