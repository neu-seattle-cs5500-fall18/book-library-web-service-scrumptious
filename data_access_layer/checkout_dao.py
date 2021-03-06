

from data_access_layer.book_copy_dao import BookCopyDao
from flask_restplus import abort
from model import db

from model.checkout import Checkout

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

        list_of_checkouts = []
        query_results = Checkout.query.all()

        for checkout in query_results:
            list_of_checkouts.append(checkout.to_dict())
        return list_of_checkouts

    @staticmethod
    def create_new_checkout(checkout_dict):

        new_checkout = Checkout(**checkout_dict)
        book_copy_id = new_checkout.book_copy_id
        book_copy = BookCopyDao.get_book_copy(book_copy_id)
        book_copy.is_checked_out = True

        db.session.add(new_checkout)
        db.session.commit()
        print('checkout created')

        return new_checkout.checkout_id

    @staticmethod
    def get_checkout(checkout_id):

        print('Get a checkout')

        a_checkout = Checkout.query.get(checkout_id)
        print(a_checkout)

        return a_checkout.to_dict()

    @staticmethod
    def update(checkout_id, checkout_info_dict):

        print('Updating checkout')
        a_checkout = Checkout.query.get(checkout_id)
        book_copy_id = a_checkout.book_copy_id
        book_copy = BookCopyDao.get_book_copy(book_copy_id)
        book_copy.is_checked_out = False
        a_checkout.update(**checkout_info_dict)
        db.session.commit()
        return a_checkout.to_dict()

    @staticmethod
    def delete_checkout(checkout_id):

        print('Delete checkout')

        a_checkout = Checkout.query.filter_by(checkout_id=checkout_id).delete()
        book_copy_id = a_checkout.book_copy_id
        book_copy = BookCopyDao.get_book_copy(book_copy_id)
        book_copy.is_checked_out = False
        db.session.commit()
        return a_checkout, 204

    @staticmethod
    def get_reminders():
        list_of_checkouts = []

        results = Checkout.query.filter(Checkout.return_date==None).all()
        print(results)

        print("before printing")
        for checkout in results:
            list_of_checkouts.append(checkout.to_dict())
        return list_of_checkouts





