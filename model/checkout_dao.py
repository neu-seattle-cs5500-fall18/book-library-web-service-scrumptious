from model.checkout import Checkout
from flask_restplus import abort
from library_webservice import db


def get_all_checkouts():
    print('Get all checkouts')
    list_of_checkouts = Checkout.query.all()
    return list_of_checkouts


def create_new_checkout(checkout_info):
    print('Creating new user')

    user_id = checkout_info['user_id']
    book_id = checkout_info['book_id']
    checkout_date = checkout_info['checkout_date']
    due_date = checkout_info['due_date']

    new_checkout = Checkout(user_id=user_id, book_id=book_id, checkout_date=checkout_date, due_date=due_date)

    db.session.add(new_checkout)
    db.session.commit()

    return new_checkout.user_id


def get_checkout(checkout_id):
    print('Get a checkout')

    a_checkout = Checkout.query.get(checkout_id)

    if a_checkout is None:
        abort(400, 'Record not found')
    else:
        return a_checkout


def update_checkout(checkout_id, checkout_info):
    print('Updating checkout')

    a_checkout = Checkout.query.get(checkout_id)

    if a_checkout is None:
        abort(400, 'Record not found')

    else:
        a_checkout.user_id = checkout_info['user_id']
        a_checkout.book_id = checkout_info['book_id']
        a_checkout.checkout_date = checkout_info['checkout_date']
        a_checkout.due_date = checkout_info['due_date']

        db.session.commit()

        return a_checkout.checkout_id


def delete_checkout(checkout_id):
    print('Delete checkout')

    a_checkout = Checkout.query.get(checkout_id)

    if a_checkout is None:
        abort(400, 'Record not found')
    else:
        a_checkout.is_deleted = True
        db.session.commit()
        return a_checkout.checkout_id


def get_reminder():
    checkouts = Checkout.query.filter_by(return_date=None)

    return checkouts
