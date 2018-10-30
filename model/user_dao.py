from model.user import User
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
    print('Get user %d') %user_id

    a_user = User.query.get(user_id)

    return a_user


def update_user(user_id, info_json):
    # a_user = User.query.get(user_id)
    # a_user.user_first_name = info_json['user_first_name']
    # a_user.user_last_name = info_json['user_last_name']
    # a_user.email = info_json['email']
    #
    # db.session.commit()
    print('updating user')

    return 'user updated'


def delete_user(user_id):
    print('Delete user %d') %user_id

    a_user = User.query.get(user_id)
    a_user.is_deleted = True
    db.session.commit()

    return a_user.user_id

