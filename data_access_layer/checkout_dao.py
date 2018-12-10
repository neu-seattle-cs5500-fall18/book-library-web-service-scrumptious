from data_access_layer import book_copy_dao
from model.book_copy import BookCopy
from model.checkout import Checkout
from model.book import Book
from flask_restplus import abort
from model import db
from datetime import datetime, timedelta


class CheckoutDao:

    @staticmethod
    def query_checkout(checkout_id):

        print('Query user')
        a_checkout = Checkout.query.get(checkout_id)

        if a_checkout is None:
            abort(400, 'Record not found')
        else:
            return a_checkout.to_dict()

    @staticmethod
    def get_all_checkouts():
        print('Get all checkouts')
        list_of_checkouts = Checkout.query.all()
        return list_of_checkouts

    @staticmethod
    def create_new_checkout(checkout_dict):
        print('Creating new checkout')
        new_checkout = Checkout(**checkout_dict)
        print("pre-add")
        db.session.add(new_checkout)
        print("pre-commit")
        db.session.commit()
        print('checkout created')

        return new_checkout.checkout_id

    @staticmethod
    def get_checkout(checkout_id):

        print('Get a checkout')

        a_checkout = Checkout.query.get(checkout_id)

        return a_checkout.to_dict

    @staticmethod
    def update_checkout(checkout_id):

        print('Updating checkout')

        a_checkout = Checkout.query.get(checkout_id)

        a_checkout.return_date = datetime.now
        book_copy_id = a_checkout.book_copy_id
        book_copy = book_copy_dao.get_book_copy(book_copy_id)
        book_copy.is_checked_out = False

        db.session.commit()

        return a_checkout.checkout_id

    @staticmethod
    def delete_checkout(checkout_id):

        print('Delete checkout')

        a_checkout = Checkout.query.filter_by(checkout_id=checkout_id).delete()
        db.session.commit()
        return None

