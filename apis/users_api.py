from flask import request
from flask_restplus import abort, Namespace, Resource, fields
from controller.user_checker import get_all_users, get_user, create_user, update_user, delete_user


api = Namespace('users', description='User operations')

user_marshaller = api.model('User', {
    'user_id': fields.Integer(description='The user\'s unique identifying record'),
    'user_first_name': fields.String(required=True, max_length=25, description='The user\'s first name'),
    'user_last_name': fields.String(required=True, max_length=25, description='The user\'s last name'),
    'user_email': fields.String(required=True, max_length=25, description='The user\'s email address'),
    'is_deleted': fields.Boolean(description='Designates whether a user is deleted'),
})

user_input_marshaller = api.model('UserInput', {
    'user_first_name': fields.String(required=True, max_length=25, description='The user\'s first name'),
    'user_last_name': fields.String(required=True, max_length=25, description='The user\'s last name'),
    'user_email': fields.String(required=True, max_length=50, description='The user\'s email address'),
})


@api.route('')
@api.response(400, 'Record not found')
@api.response(201, 'Created new user.')
@api.response(200, 'Successful request')
class Users(Resource):
    def get(self):
        """
        Gets all users
        :return: Json List of users of type Dict
        """
        print('Received GET on resources /users')
        response = get_all_users()
        return response, 200

    @api.expect(user_input_marshaller)
    def post(self):
        """
        Creates a new user record.
        :return: User ID of the created record.
        """
        print('Received POST on resource /users')
        user_info = request.get_json()
        response = create_user(user_info)
        return response, 201


@api.route('/<user_id>', endpoint='user_record')
@api.doc(params={'user_id': 'An ID for a user record'})
@api.response(400, 'Invalid input for user_id in url')
@api.response(400, 'Record not found')
@api.response(200, 'Success')
@api.response(200, 'User deleted')
class UserRecord(Resource):
    @api.marshal_with(user_marshaller)
    def get(self, user_id):
        """
        Gets a user record.
        :param user_id: Record number to be retrieved.
        :return: A user record.
        """
        print('Received GET on resource /users/<user_id>')

        if user_id.isdigit():
            user_record = get_user(user_id)
            print(user_record)
            return user_record
        else:
            return abort(400, 'Invalid input for user_id in url')

    @api.expect(user_input_marshaller, validate=True)
    def put(self, user_id):
        """
        Updates an existing user record based on user_id.
        :param user_id: Record number to be updated.
        :return: Json with user_id of updated record.
        """
        print('Received PUT on resource /users/<user_id>')

        if user_id.isdigit():
            request_body = request.get_json()
            user_id = update_user(user_id, request_body)
            return user_id
        else:
            return abort(400, 'Invalid input for user_id in url')

    def delete(self, user_id):
        """
        Delete a user based on user_id.
        :param user_id: User to be deleted.
        :return: Json of user_id of deleted record.
        """
        print('Received DELETE on resource /users/<user_id>')

        if user_id.isdigit():
            id_of_deleted = delete_user(user_id)
            return id_of_deleted
        else:
            return abort(400, 'Invalid input for user_id in url')
