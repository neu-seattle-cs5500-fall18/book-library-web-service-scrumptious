from data_access_layer import book_copy_dao
from model.checkout import Checkout
from model.book import Book
from flask_restplus import abort
from library_webservice import db
from datetime import datetime


def query_checkout(checkout_id):
    print('Query user')
    a_checkout = Checkout.query.get(checkout_id)

    if a_checkout is None:
        abort(400, 'Record not found')
    else:
        return a_checkout.to_dict()


def get_all_checkouts():
    print('Get all checkouts')
    list_of_checkouts = Checkout.query.all()
    return list_of_checkouts


def create_new_checkout(user_id, book_id):
    print('Creating new checkout')

    book_copy = Book.query.filter_by(book_id).first()
    book_copy_id = book_copy.book_copy_id
    lending_time = datetime.timedelta(days=21)

    new_checkout = Checkout(user_id=user_id, book_id=book_id,book_copy_id=book_copy_id, checkout_date=datetime.now,
                            due_date=datetime.now+lending_time)

    book_copy.is_checked_out = True

    db.session.add(new_checkout)
    db.session.commit()

    return new_checkout.user_id


def get_checkout(checkout_id):
    print('Get a checkout')

    a_checkout = Checkout.query.get(checkout_id)

    return a_checkout


def update_checkout(checkout_id):
    print('Updating checkout')

    a_checkout = Checkout.query.get(checkout_id)

    a_checkout.return_date = datetime.now
    book_copy_id = a_checkout.book_copy_id
    book_copy = book_copy_dao.get_book_copy(book_copy_id)
    book_copy.is_checked_out = False

    db.session.commit()

    return a_checkout.checkout_id


def delete_checkout(checkout_id):
    print('Delete checkout')

    a_checkout = Checkout.query.get(checkout_id)
    db.session.commit()
    return a_checkout.checkout_id


def get_reminder():
    checkouts = Checkout.query.filter_by(return_date=None)

    return checkouts
