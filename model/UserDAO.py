from model.User import User
from library_webservice import db


def get_all_users():
    list_of_users = User.query.all()
    return list_of_users


def create_new_user(info_json):
    first_name = info_json['user_first_name']
    last_name = info_json['user_last_name']
    email = info_json['email']
    a_user = User(first_name,last_name, email)
    db.session.add(a_user)
    db.session.commit

    return a_user.user_id


def get_user(user_id):
    a_user = User.query.get(user_id)

    return a_user


def update_user(user_id, info_json):
    a_user = User.query.get(user_id)
    a_user.user_first_name = info_json['user_first_name']
    a_user.user_last_name = info_json['user_last_name']
    a_user.email = info_json['email']

    db.session.commit()

    return a_user.user_id


def delete_user(user_id):
    a_user = User.query.get(user_id)
    a_user.is_deleted = True
    db.session.commit()

    return a_user.user_id

