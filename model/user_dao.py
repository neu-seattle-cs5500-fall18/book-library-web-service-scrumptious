from sqlalchemy import and_
from flask_restplus import abort
from library_webservice import db
from model.user import User

#check edge case of no users
def query_all_users():
    print('Get all users')
    #include query parameters here.
    list_of_users = []
    query_results = User.query.all()

    for user in query_results:
        list_of_users.append(user.to_dict())
    print(list_of_users)
    return list_of_users


def create_user_record(user_info_dict):
    print('Create user record')
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


def query_user(user_id):
    print('Query user')
    a_user = User.query.get(user_id)

    if a_user is None:
        abort(400, 'Record not found')
    else:
        return a_user.to_dict()


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

