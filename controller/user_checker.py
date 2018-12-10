from data_access_layer.user_dao import UserDao
from flask_restplus import abort

def email_exists(email):
    """
    Helper function to see if DAO has a record with the same email.
    :param email: string email
    :return: True if email already exists, false otherwise.
    """
    print('user_checker.email_exists()')
    return UserDao.email_exists(email)


def valid_input(first_name, last_name, email):
    """
    Helper function to validate user information
    :param first_name: String first name, where name only contains alpha characters
    :param last_name: String last name where name onlu contains alpha characters
    :param email: String email where email contains '@'
    :return: True if parameters match, false otherwise.
    """
    print('Validate user info input')
    return first_name.isalpha() and last_name.isalpha() and ('@' in email)


def clean_user(first_name, last_name, email):
    """
    Helper function to prepare user information for entry to DAO
    :param first_name: String first name of user.
    :param last_name: String last name of user.
    :param email: string email of user.
    :return: Dictionary of a user.
    """
    print('Clean User Info')

    user = {
        'user_first_name': first_name.lower().title(),
        'user_last_name': last_name.lower().title(),
        'email': email
    }
    return user


def get_all_users():
    """
    Method to retrieve all users within the database.
    :return: a Json list of User Dicts.
    """
    list_of_users = UserDao.get_users()
    return list_of_users


def create_user(json_user_info):
    """
    Function to create a new user in the database.
    :param json_user_info: Json body of HTTP request.
    :return: Dictionary of created user.
    """
    print('Create user')

    fname = json_user_info['user_first_name']
    lname = json_user_info['user_last_name']
    email = json_user_info['email']

    if email_exists(email):
        abort(400, 'Must provide a unique email')
    else:
        if valid_input(fname, lname, email):
            user_dict = clean_user(fname, lname, email)
            return UserDao.create(user_dict)
        else:
            abort(400, 'Invalid input')


def get_user(user_id):
    """
    Method to get a specific user record based on user_id.
    :param user_id: Record of User to get.
    :return: Dictionary of user.
    """
    print('Get user %r' % user_id)

    if UserDao.contains(user_id):
        a_user = UserDao.get(user_id)
        return a_user
    else:
        abort(404, 'Resource user_id not found')


def update_user(user_id, json_user_info):
    """
    Function to update an existing user record.
    :param user_id: Integer of user record to be updated.
    :param json_user_info: Json of user information to be updated.
    :return:
    """
    print(json_user_info)
    fname = json_user_info['user_first_name']
    lname = json_user_info['user_last_name']
    email = json_user_info['user_email']

    if valid_input(fname, lname, email):
        user = clean_user(fname, lname, email)
        return update_user(user_id, user)
    else:
        abort(400, 'Invalid input')


def delete_user(user_id):
    """
    Function to delete a user.
    :param user_id: Integer of user record
    :return: None
    """
    if UserDao.contains(user_id):
        print('Delete user %r' % user_id)
        return UserDao.delete(user_id)
    else:
        abort(404, 'Resource user_id not found')
