from data_access_layer import checkout_dao
from flask_restplus import abort
from model.checkout import Checkout

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


def create_checkout(json_user_info):
    """
    Method to verify the integrity of the body of a POST request to create a new checkout.
    :param json_user_info: Json body of HTTP request.
    :return: Json of the id of the newly created User.
    """
    print('Create a checkout')

    user_id = json_user_info['user_id']
    book_id = json_user_info['book_id']
    book_copy_id = json_user_info['book_copy_id']
    checkout_date = json_user_info['checkout_date']
    due_date = json_user_info['due_date']

    existing_checkout = Checkout.query.filter_by(user_id=user_id).filter_by(book_id=book_id).\
        filter_by(book_copy_id = book_copy_id).filter_by(
        checkout_date=checkout_date).filter_by(due_date=due_date)

    if existing_checkout is not None:
        abort(400, 'Invalid input')

        checkout_dict = clean_checkout(user_id, book_id, book_copy_id, checkout_date, due_date)

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


def update_checkout(checkout_id, json_user_info):
    a_checkout = checkout_dao.query_checkout(checkout_id)
    if a_checkout is None:
        abort(400, 'Invalid input')

    return checkout_dao.update_checkout(checkout_id, json_user_info)


def delete_checkout(checkout_id):
    print('Delete checkout %r' % checkout_id)
    a_checkout = checkout_dao.delete_checkout(checkout_id)
    if a_checkout is None:
        abort(400, 'Onvalid input')
    return checkout_dao.delete_user(checkout_id)
