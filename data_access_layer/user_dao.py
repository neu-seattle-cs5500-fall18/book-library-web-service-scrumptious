from flask_restplus import abort
from library_webservice import db
from model.user import User


def contains(user_id):
    print('user_dao.contains()')
    user = User.query.get(user_id)
    if user is None:
        return False
    else:
        return True


def get(user_id):
    print('user_dao.get()')
    a_user = User.query.get(user_id)
    return a_user.to_dict()


def get_users():
    print('user_dao.get_users()')

    list_of_users = []
    query_results = User.query.all()

    for user in query_results:
        list_of_users.append(user.to_dict())
    return list_of_users


def create(user_info_dict):
    print('user_dao.create()')
    firstname = user_info_dict['user_first_name']
    lastname = user_info_dict['user_last_name']
    email = user_info_dict['email']

    # Check if user info already exists
    existing_user = User.query.filter_by(user_first_name=firstname).filter_by(user_last_name= lastname).filter_by(email= lastname).first()

    print(existing_user)

    if existing_user is None:
        new_user = User(user_first_name=firstname, user_last_name=lastname, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user.user_id
    else:
        abort(400, 'User information combination already exists')


def update(user_id, user_info):
    print('user_dao.update()')

    a_user = User.query.get(user_id)
    a_user.update(**user_info)
    db.session.commit()
    return a_user.to_dict()


def delete(user_id):
    print('user_dao.delete()')
    user = User.query.filter_by(user_id=user_id).delete()
    db.session.commit()
    return user
