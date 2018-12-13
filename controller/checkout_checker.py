from data_access_layer import book_copy_dao
from data_access_layer.book_copy_dao import BookCopyDao
from data_access_layer.book_dao import BookDao
from data_access_layer.checkout_dao import CheckoutDao
from flask_restplus import abort

from data_access_layer.user_dao import UserDao


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
    book_copy_id = json_checkout_info['book_copy_id']
    if BookCopyDao.get_book_copy(book_copy_id).is_checked_out is True:
        return abort(400, 'book already checked out')

    user_id = json_checkout_info['user_id']
    book_id = json_checkout_info['book_id']
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


def joint_to_dict(checkout_date, due_date, user_first_name, user_last_name, user_email, title):
    """
    Turning the instance to a ductionary.
    :param checkout_date: the checkout date of the book.
    :param due_date: the due_date of the book.
    :param user_first_name: user's first name.
    :param user_last_name: user's last name.
    :param user_email: user's email.
    :param title: borrowed book's title.
    :return: the dictionary of the reminder information needed to be sent to the user.
    """
    joint_dict = {
        'checkout_date': checkout_date,
        'due_date': due_date,
        'user_first_name': user_first_name,
        'user_last_name': user_last_name,
        'user_email': user_email,
        'title': title,
    }

    return joint_dict


def get_reminders():
    """
    Return the list of checkouts and user's emails that need reminders.
    :return: the list of checkouts that need to be sent email notifications along with the user emails.
    """
    new_list = []
    list_of_reminders = CheckoutDao.get_reminders()

    for checkout in list_of_reminders:
        book = BookDao.get(checkout['book_id'])
        user = UserDao.get(checkout['user_id'])
        title = book['title']
        user_first_name = user['user_first_name']
        user_last_name = user['user_last_name']
        user_email = user['user_email']
        entry = joint_to_dict(checkout['checkout_date'], checkout['due_date'], user_first_name, user_last_name, user_email, title)
        new_list.append(entry)

    return new_list
