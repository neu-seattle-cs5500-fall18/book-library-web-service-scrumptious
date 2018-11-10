from data_access_layer import checkout_dao
from flask_restplus import abort
from model.checkout import Checkout
from model.book import Book

# functions that interact with a checkout record


# def valid_input(user_id, book_id, book_copy_id, checkout_date, due_date):
#     print('Validate checkout info input')
#     return user_id.isdigit() and book_id.isdigit() and checkout_date.isdate() and due_date.isdate()


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
    list_of_checkouts = checkout_dao.get_all_checkouts()
    return list_of_checkouts


def create_checkout(user_id, book_id):
    """
    Checking if a new checkout can be created
    :param user_id: given a user id
    :param book_id: given a book id
    :return: a checkout of the book
    """
    print('Create a checkout')

    existing_checkout = Checkout.query.filter_by(user_id=user_id).filter_by(book_id=book_id)

    if existing_checkout is not None:
        abort(400, 'checkout already existed')

    book_copy = Book.query.filter_by(book_id)

    if book_copy is None:
        abort(400, 'Book not available')

    checkout_dict = {
        'user_id': user_id,
        'book_id': book_id,
    }
    return checkout_dao.create_new_checkout(checkout_dict)


def get_checkout(checkout_id):
    """
    Method to get a specific checkout record based on checkout_id.
    :param checkout_id: Record of Checkout to get.
    :return: Json of a Checkout Dict
    """
    print('Get checkout %r' % checkout_id)
    a_checkout = checkout_dao.query_checkout(checkout_id)
    if a_checkout is None:
        abort(400, 'Invalid input')
    return a_checkout


def update_checkout(checkout_id):
    a_checkout = checkout_dao.query_checkout(checkout_id)
    if a_checkout is None:
        abort(400, 'Invalid input')

    return checkout_dao.update_checkout(checkout_id)


def delete_checkout(checkout_id):
    print('Delete checkout %r' % checkout_id)
    a_checkout = checkout_dao.delete_checkout(checkout_id)
    if a_checkout is None:
        abort(400, 'Onvalid input')
    return checkout_dao.delete_user(checkout_id)
