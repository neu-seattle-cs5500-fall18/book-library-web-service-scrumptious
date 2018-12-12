from data_access_layer import book_copy_dao
from data_access_layer.checkout_dao import CheckoutDao
from flask_restplus import abort


def clean_checkout(user_id, book_id, book_copy_id, checkout_date, due_date, return_date):
    print('Clean checkout Info')

    checkout = {
        'user_id': user_id,
        'book_id': book_id,
        'book_copy_id': book_copy_id,
        'checkout_date': checkout_date,
        'due_date': due_date,
        'return_date': return_date
    }
    print(checkout)
    return checkout


def get_all_checkouts():
    """
    Method to retrieve all checkouts within the database.
    :return: a Json list of Checkout Dicts.
    """
    list_of_checkouts = CheckoutDao.get_all_checkouts()
    print("after get all checkouts in the checker layer")
    return list_of_checkouts


def create_checkout(json_checkout_info):

    user_id = json_checkout_info['user_id']
    book_id = json_checkout_info['book_id']
    book_copy_id = json_checkout_info['book_copy_id']
    checkout_date = json_checkout_info['checkout_date']
    due_date = json_checkout_info['due_date']
    return_date = json_checkout_info['return_date']

    checkout_dict = clean_checkout(user_id, book_id, book_copy_id, checkout_date, due_date, return_date)
    return CheckoutDao.create_new_checkout(checkout_dict)


def get_checkout(checkout_id):
    """
    Method to get a specific checkout record based on checkout_id.
    :param checkout_id: Record of Checkout to get.
    :return: Json of a Checkout Dict.
    """
    print('Get checkout %r' % checkout_id)
    a_checkout = CheckoutDao.query_checkout(checkout_id)
    print(a_checkout)
    if a_checkout is None:
        abort(400, 'Invalid input')
    return a_checkout


def update_checkout(checkout_id, json_checkout_info):
    """
    method to update a checkout since the checkout is returned.
    :param json_checkout_info:
    :return: the to-be-update information of checkout
    :param checkout_id: the checkout_id that has been returned.
    :return: the updated checkout id adding the return date of the record.
    """
    user_id = json_checkout_info['user_id']
    book_id = json_checkout_info['book_id']
    book_copy_id = json_checkout_info['book_copy_id']
    checkout_date = json_checkout_info['checkout_date']
    due_date = json_checkout_info['due_date']
    return_date = json_checkout_info['return_date']

    checkout_dict = clean_checkout(user_id, book_id, book_copy_id, checkout_date, due_date, return_date)
    return CheckoutDao.update(checkout_id, checkout_dict)


def delete_checkout(checkout_id):
    """
    Delete a particular checkout record.
    :param checkout_id: the checkout id needs to be deleted.
    :return: the deleted checkout id record.
    """
    print('Delete checkout %r' % checkout_id)
    a_checkout = CheckoutDao.delete_checkout(checkout_id)
    if a_checkout is None:
        abort(400, 'Invalid input')
    return CheckoutDao.delete_checkout(checkout_id)
