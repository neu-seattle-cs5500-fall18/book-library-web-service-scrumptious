from flask import request, jsonify
from flask_restplus import abort, Namespace, Resource, fields
from controller.user_checker import get_all_users, get_user, create_user, update_user, delete_user


ns = Namespace('users', description='User operations')

user_marshaller = ns.model('User', {
    'user_id': fields.Integer(description='The user\'s unique identifying record'),
    'user_first_name': fields.String(required=True, max_length=25, description='The user\'s first name'),
    'user_last_name': fields.String(required=True, max_length=25, description='The user\'s last name'),
    'user_email': fields.String(required=True, max_length=25, description='The user\'s email address'),
})

user_input_marshaller = ns.model('UserInput', {
    'user_first_name': fields.String(required=True, max_length=25, description='The user\'s first name'),
    'user_last_name': fields.String(required=True, max_length=25, description='The user\'s last name'),
    'user_email': fields.String(required=True, max_length=50, description='The user\'s email address'),
})





@ns.route('')
@ns.response(404, 'Record not found')
@ns.response(201, 'Created new user.')
@ns.response(200, 'Successful request')
class Users(Resource):
    def get(self):
        """
        Gets all users
        :return: Json List of users of type Dict
        """
        print('Received GET on resources /users')
        response = jsonify(get_all_users())
        return response

    @ns.expect(user_input_marshaller)
    @ns.marshal_with(user_marshaller, 201)
    def post(self):
        """
        Creates a new user record.
        :return: User ID of the created record.
        """
        print('Received POST on resource /users')
        user_info = request.get_json()
        response = create_user(user_info)
        return response, 201


@ns.route('/<user_id>', endpoint='user_record')
@ns.doc(params={'user_id': 'An ID for a user record'})
@ns.response(400, 'Invalid input for user_id in url')
@ns.response(400, 'Record not found')
@ns.response(200, 'Success')
@ns.response(204, 'User deleted')
class UserRecord(Resource):
    @ns.marshal_with(user_marshaller)
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

    @ns.expect(user_input_marshaller, validate=True)
    @ns.marshal_with(user_marshaller, 200)
    def put(self, user_id):
        """
        Updates an existing user record based on user_id.
        :param user_id: Record number to be updated.
        :return: JSON of updated user record.
        """
        print('Received PUT on resource /users/<user_id>')

        if user_id.isdigit():
            request_body = request.get_json()
            user = update_user(user_id, request_body)
            return user
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
            return id_of_deleted, 204

        else:
            return abort(400, 'Invalid input for user_id in url')
