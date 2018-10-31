from flask import request
from flask_restplus import Namespace, Resource, fields
from model import UserDAO


api = Namespace('users', description='User operations')

user = api.model('User', {
    'user_id': fields.Integer(required=True, description='The user\'s unique identifying record'),
    'user_first_name': fields.String(description='The user\'s first name'),
    'user_last_name': fields.String(description='The user\'s last name'),
    'email': fields.String(description='The user\'s email address'),
    'is_deleted': fields.Boolean(description='Designates whether a user is deleted'),
})


class UserMarshaler(object):
    def __init__(self, user_id, user_first, user_last, user_email, is_deleted):
        self.user_id = user_id
        self.user_first = user_first
        self.user_last = user_last
        self.user_email = user_email
        self.is_deleted = is_deleted


@api.route('/', endpoint='users')
class Users(Resource):
    @api.marshal_with(user)
    @api.response(200, 'Resource successfully retrieved')
    def get(self):
        """
        Gets all users
        :return: Json object of all users
        """
        return UserDAO.get_all_users(), 200

    @api.doc(responses={201: 'User successfully created'})
    @api.expect(user)
    def post(self):
        """
        Creates a new user record.
        :return: User ID of the created record.
        """
        info_json = request.get_json()
        new_user_id = UserDAO.create_new_user(info_json)
        return new_user_id, 201


@api.route('/<user_id>')
@api.doc(params={'user_id': 'An ID'})
class UserRecord(Resource):
    @api.marshal_with(user, code=200, description='Success')
    def get(self, user_id):

        user_record = UserDAO.get_user(user_id)

        return user_record, 200

    @api.doc(body=user, validate=True)
    @api.response(code=200, description='Success')
    def put(self, user_id):
        """
        Updates an existing user record based on user_id.
        :param user_id: Record number to be updated.
        :return: Json with user_id of updated record.
        """

        request_body = request.get_json()

        user_id = UserDAO.update_user(user_id, request_body)

        return user_id

    @api.response(code=200, description='User deleted')
    def delete(self, user_id):
        """
        Delete a user based on user_id.
        :param user_id: User to be deleted.
        :return: Json of user_id of deleted record.
        """

        id_of_deleted = UserDAO.delete_user(user_id)
        return id_of_deleted, 200
    