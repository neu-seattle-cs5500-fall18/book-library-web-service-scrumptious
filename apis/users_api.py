from flask import request
from flask_restplus import Namespace, Resource, fields
from model.user_dao import create_new_user, get_all_users, get_user, update_user, delete_user


api = Namespace('users', description='User operations')

user_marshaller = api.model('User', {
    'user_id': fields.Integer(description='The user\'s unique identifying record'),
    'user_first_name': fields.String(required=True, max_length=50, description='The user\'s first name'),
    'user_last_name': fields.String(required=True, max_length=50, description='The user\'s last name'),
    'email': fields.String(required=True, max_length=50, description='The user\'s email address'),
    'is_deleted': fields.Boolean(description='Designates whether a user is deleted'),
})


@api.route('')
class Users(Resource):
    @api.marshal_with(user_marshaller, code=200)
    def get(self):
        """
        Gets all users
        :return: Json object of all users
        """
        print('Received GET on resources /users')
        response = get_all_users()

        return response

    @api.response(400, 'Record not found')
    @api.response(201, 'Created new user.')
    @api.expect(user_marshaller)
    def post(self):
        """
        Creates a new user record.
        :return: User ID of the created record.
        """
        print('Received POST on resource /users')

        user_info = request.get_json()
        response = create_new_user(user_info)

        return response, 201


@api.route('/<user_id>', endpoint='user_record')
@api.doc(params={'user_id': 'An ID for a user record'})
class UserRecord(Resource):
    @api.marshal_with(user_marshaller)
    def get(self, user_id):
        print('Received GET on resource /users/<user_id>')

        user_record = get_user(user_id)
        # print(user_record)
        # if user_record == 404:
        #     abort(400, 'User not found')
        # else:
        return user_record

    @api.response(code=400, description='Record not found')
    @api.response(code=200, description='Success')
    @api.expect(user_marshaller, validate=True)
    def put(self, user_id):
        """
        Updates an existing user record based on user_id.
        :param user_id: Record number to be updated.
        :return: Json with user_id of updated record.
        """
        print('Received PUT on resource /users/<user_id>')
        request_body = request.get_json()

        user_id = update_user(user_id, request_body)

        return user_id

    @api.response(code=200, description='User deleted')
    def delete(self, user_id):
        """
        Delete a user based on user_id.
        :param user_id: User to be deleted.
        :return: Json of user_id of deleted record.
        """
        print('Received DELETE on resource /users/<user_id>')

        id_of_deleted = delete_user(user_id)

        return id_of_deleted
