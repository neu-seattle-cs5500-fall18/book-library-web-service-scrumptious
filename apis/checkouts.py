# adding some reviews to pull from sarah for lab3

from flask_restplus import Namespace, fields, Resource, reqparse

api = Namespace('checkouts', description='Checkouts operations')

checkout = api.model('Checkout', {
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


class CheckOut(object):
    def __init__(self, checkout_id, user_id, book_id, checkout_date, due_date, return_date):
        self.checkout_id = checkout_id
        self.user_id = user_id
        self.book_id = book_id
        self.checkout_date = checkout_date
        self.due_date = due_date
        self.return_date = return_date

        self.status = 'active'


@api.route('/', endpoint='checkouts')
@api.response(code=400, description='Validation Error')
class Checkouts(Resource):

    @api.doc(body=query_parser, validate=True)
    @api.marshal_with(checkout, code=200, description='Success')
    def get(self):
        """
        Queries the checkouts resource based on URL.
        :return: Json object of all checkouts that match the query parameter.
        """
        return "got a checkout"

    @api.doc(body=checkout, validate=True)
    @api.marshal_with(checkout, code=201, description='Success')
    def post(self, checkout_id):
        """
        Create a new checkout for the book.
        :param checkout_id: Record for a checkout id.
        :return: checkout_id for the create book
        """
        return "Successfully added checkout" % checkout_id


@api.route('/checkout_id')
@api.doc(params={'checkout_id': 'Record of a checkout'})
@api.response(code=400, description='Validation error')
class CheckoutRecord(Resource):
    @api.marshal_with(checkout, code=200, description='Success')
    def get(self, checkout_id):
        """
        Gets a specific checkout record based on checkout_id.
        :param checkout_id: Record of a checkout.
        :return: JSON of requested checkout record.
        """
        return "Successfully got %s " % checkout_id

    @api.doc(body=checkout, validate=True)
    @api.response(code=200, description='Success')
    def put(self, checkout_id):
        """
        Updates an existing checkout record based on checkout_id.
        :param checkout_id: Record checkout id to be updated.
        :return: Json with checkout_id of updated record.
        """
        return "Successfully updated %s " % checkout_id

    @api.response(code=200, description='Checkout deleted')
    def delete(self, checkout_id):
        """
        Delete a checkout record based on checkout_id.
        :param checkout_id: Record to be deleted.
        :return: Json of checkout_id of deleted record.
        """
        return "Successfully deleted" % checkout_id


@api.route('/reminders/')
@api.response(code=400, description='Validation Error')
class Reminder(Resource):
    @api.doc(body=checkout, validate=True)
    @api.marshal_with(checkout, code=200, description="Success")
    def get(self, return_date):
        """
        Return the checkouts that have not been returned.
        :param return_date: the date when the book is returned.
        :return: the checkouts that don't have a return date yet.
        """
        return "got the list of checkouts for reminders"


