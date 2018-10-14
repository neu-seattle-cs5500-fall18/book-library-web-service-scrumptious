from flask_restplus import Namespace, fields, Resource, reqparse

api = Namespace('checkouts', description='Checkouts operations')


class CheckOut(object):
    def __init__(self, checkout_id, user_id, book_id, checkout_date, due_date):
        self.checkout_id = checkout_id
        self.user_id = user_id
        self.book_id = book_id
        self.checkout_date = checkout_date
        self.due_date = due_date

        self.status = 'active'


@api.route('/', endpoint='checkouts')
class Checkouts(Resource):
    def get(self):
        return


