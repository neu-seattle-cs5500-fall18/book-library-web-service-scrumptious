from data_access_layer import checkout_dao, book_copy_dao
from flask_restplus import abort

from data_access_layer.book_copy_dao import BookCopyDao
from model.checkout import Checkout
from model.book import Book


def clean_checkout(user_id, book_id, book_copy_id, checkout_date, due_date):
    print('Clean checkout Info')

    checkout = {
        'user_id': user_id,
        'book_id': book_id,
        'book_copy_id': book_copy_id,
        'checkout_date': checkout_date,
        'due_date': due_date
    }
    print(checkout)
    return checkout


def get_all_checkouts():
    """
    Method to retrieve all checkouts within the database.
    :return: a Json list of Checkout Dicts.
    """
    list_of_checkouts = checkout_dao.CheckoutDao.get_all_checkouts()
    return list_of_checkouts


def create_checkout(user_id, book_id):
    """
    Checking if a new checkout can be created.
    :param user_id: given a user id.
    :param book_id: given a book id.
    :return: a checkout of the book.
    """
    print('Checker layer')

    existing_checkout = Checkout.query.filter_by(user_id=user_id, book_id=book_id).first()

    if existing_checkout is not None:
        abort(400, 'checkout already existed')
    else:

        book_copy = BookCopyDao.get_next_available(book_id)

    if book_copy is None:
        abort(400, 'Book not available')

    print('passing the ifs')

    checkout_dict = {
        'user_id': user_id,
        'book_id': book_id,
    }
    return checkout_dao.CheckoutDao.create_new_checkout(checkout_dict)


def get_checkout(checkout_id):
    """
    Method to get a specific checkout record based on checkout_id.
    :param checkout_id: Record of Checkout to get.
    :return: Json of a Checkout Dict.
    """
    print('Get checkout %r' % checkout_id)
    a_checkout = checkout_dao.CheckoutDao.query_checkout(checkout_id)
    if a_checkout is None:
        abort(400, 'Invalid input')
    return a_checkout


def update_checkout(checkout_id):
    """
    method to update a checkout since the checkout is returned.
    :param checkout_id: the checkout_id that has been returned.
    :return: the updated checkout id adding the return date of the record.
    """
    a_checkout = checkout_dao.CheckoutDao.query_checkout(checkout_id)
    if a_checkout is None:
        abort(400, 'Invalid input')

    return checkout_dao.CheckoutDao.update_checkout(checkout_id)


def delete_checkout(checkout_id):
    """
    Delete a particular checkout record.
    :param checkout_id: the checkout id needs to be deleted.
    :return: the deleted checkout id record.
    """
    print('Delete checkout %r' % checkout_id)
    a_checkout = checkout_dao.CheckoutDao.delete_checkout(checkout_id)
    if a_checkout is None:
        abort(400, 'Onvalid input')
    return checkout_dao.CheckoutDao.delete_checkout(checkout_id)


def get_reminder_list():
    """
    Return a list of checkouts that do not have a return date yet.
    """
    checkouts = Checkout.query.filter_by(return_date=None)
    if checkouts is None:
        abort(400, 'all checkouts have been returned')
    return checkout_dao.CheckoutDao.get_reminder()
