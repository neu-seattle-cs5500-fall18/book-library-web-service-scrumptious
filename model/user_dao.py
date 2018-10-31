from model.user import User
from flask_restplus import abort
from library_webservice import db


def get_all_users():
    print('Get all users')
    list_of_users = User.query.all()
    return list_of_users


def create_new_user(user_info):
    print('Creating new user')

    firstname = user_info['user_first_name']
    lastname = user_info['user_last_name']
    email = user_info['email']

    new_user = User(user_first_name=firstname, user_last_name=lastname, email=email)

    db.session.add(new_user)
    db.session.commit()

    return new_user.user_id


def get_user(user_id):
    print('Get user')

    a_user = User.query.get(user_id)

    if a_user is None:
        abort(400, 'Record not found')
    else:
        return a_user


def update_user(user_id, user_info):
    print('Updating user')

    a_user = User.query.get(user_id)

    if a_user is None:
        abort(400, 'Record not found')

    else:
        a_user.user_first_name = user_info['user_first_name']
        a_user.user_last_name = user_info['user_last_name']
        a_user.email = user_info['email']

        db.session.commit()

        return a_user.user_id


def delete_user(user_id):
    print('Delete user')

    a_user = User.query.get(user_id)

    if a_user is None:
        abort(400, 'Record not found')
    else:
        a_user.is_deleted = True
        db.session.commit()
        return a_user.user_id

