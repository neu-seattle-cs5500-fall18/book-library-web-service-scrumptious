from data_access_layer import user_dao
from flask_restplus import abort


def valid_input(first_name, last_name, email):
    print('Validate user info input')
    return first_name.isalpha() and last_name.isalpha() and ('@' in email)


def clean_user(first_name, last_name, email):
    print('Clean User Info')

    user = {
        'user_first_name': first_name.lower().title(),
        'user_last_name': last_name.lower().title(),
        'email': email
    }
    print(user)
    return user


def get_all_users():
    """
    Method to retrieve all users within the database.
    :return: a Json list of User Dicts.
    """
    list_of_users = user_dao.get_users()
    return list_of_users


def create_user(json_user_info):
    """
    Method to verify the integrity of the body of a POST request to create a new user.
    :param json_user_info: Json body of HTTP request.
    :return: Json of the id of the newly created User.
    """
    print('Create user')

    fname = json_user_info['user_first_name']
    lname = json_user_info['user_last_name']
    email = json_user_info['email']

    if valid_input(fname, lname, email):
        user_dict = clean_user(fname, lname, email)
        return user_dao.create(user_dict)
    else:
        abort(400, 'Invalid input')


def get_user(user_id):
    """
    Method to get a specific user record based on user_id.
    :param user_id: Record of User to get.
    :return: Json of a User Dict
    """
    print('Get user %r' % user_id)
    a_user = user_dao.get(user_id)
    return a_user


def update_user(user_id, json_user_info):
    fname = json_user_info['user_first_name']
    lname = json_user_info['user_last_name']
    email = json_user_info['email']

    if valid_input(fname, lname, email):
        user = clean_user(fname, lname, email)
        return update_user(user_id, user)
    else:
        abort(400, 'Invalid input')


def delete_user(user_id):
    print('Delete user %r' % user_id)
    return user_dao.delete(user_id)
