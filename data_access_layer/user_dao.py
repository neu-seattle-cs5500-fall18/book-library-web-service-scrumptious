from library_webservice import db
from model.user import User


class UserDao:
    @staticmethod
    def contains(user_id):
        print('UserDao.contains()')
        user = User.query.get(user_id)
        if user is None:
            return False
        else:
            return True

    @staticmethod
    def get(user_id):
        print('UserDao.get()')
        a_user = User.query.get(user_id)
        return a_user.to_dict()

    @staticmethod
    def get_users():
        print('UserDao.get_users()')

        list_of_users = []
        query_results = User.query.all()

        for user in query_results:
            list_of_users.append(user.to_dict())
        return list_of_users

    @staticmethod
    def create(user_info_dict):
        print('UserDao.create()')
        new_user = User(**user_info_dict)
        db.session.add(new_user)
        db.session.commit()
        return new_user.user_id

    @staticmethod
    def update(user_id, user_info_dict):
        print('UserDao.update()')

        a_user = User.query.get(user_id)
        a_user.update(**user_info_dict)
        db.session.commit()
        return a_user.to_dict()

    @staticmethod
    def delete(user_id):
        print('UserDao.delete()')
        user = User.query.filter_by(user_id=user_id).delete()
        db.session.commit()
        return None
