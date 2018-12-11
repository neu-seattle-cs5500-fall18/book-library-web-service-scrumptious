from model import db
from model.user import User

class UserDao:
    @staticmethod
    def contains(user_id):
        """
        Method to determine whether a user_id exists.
        :param user_id: Integer of a user record
        :return: True if present, false otherwise.
        """
        print('UserDao.contains(int)')
        user = User.query.get(user_id)
        if user is None:
            return False
        else:
            return True

    @staticmethod
    def email_exists(email):
        """
        Method to determine if an email is present in the database.
        :param email: String email of a user record.
        :return:  True if present, false otherwise.
        """
        print('UserDao.email_exists(str)')
        user = User.query.filter(User.email == email).all()
        print(user)
        if user == []:
            return False
        else:
            return True


    @staticmethod
    def get(user_id):
        """
        Method to get a user record by user_id.
        :param user_id: Integer record identifier for a user.
        :return: Dictionary of user record.
        """
        print('UserDao.get()')
        a_user = User.query.get(user_id)
        return a_user.to_dict()

    @staticmethod
    def get_users():
        """
        Method to retrieve all users in database.
        :return: A list of user dictionaries.
        """
        print('UserDao.get_users()')

        list_of_users = []
        query_results = User.query.all()

        for user in query_results:
            list_of_users.append(user.to_dict())
        return list_of_users

    @staticmethod
    def create(user_info_dict):
        """
        Method to create a new user record.
        :param user_info_dict: User information as a dictionary.
        :return: Dictionary of created user
        """
        print('UserDao.create()')
        new_user = User(**user_info_dict)
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()

    @staticmethod
    def update(user_id, user_info_dict):
        """
        Method to amend a user record
        :param user_id: Integer identifier for a user record.
        :param user_info_dict: Dictionary of updated user values.
        :return: Dictionary of amended record.
        """
        print('UserDao.update()')

        a_user = User.query.get(user_id)
        a_user.update(**user_info_dict)
        db.session.commit()
        return a_user.to_dict()

    @staticmethod
    def delete(user_id):
        """
        Method to remove a user.
        :param user_id: Integer identifier for a user record.
        :return: None
        """
        print('UserDao.delete()')
        user = User.query.filter_by(user_id=user_id).delete()
        db.session.commit()
        return None
