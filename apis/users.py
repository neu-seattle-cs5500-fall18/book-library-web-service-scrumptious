from flask_restplus import Namespace, Resource, fields

api = Namespace('users', description='User operations')

user = api.model('User', {
    'user_id': fields.Integer(required=True, description='The user\'s unique identifying record'),
    'user_first_name': fields.String(description='The user\'s first name'),
    'user_last_name': fields.String(description='The user\'s last name'),
    'email': fields.String(description='The user\'s email address'),
})


class User(object):
    def __init__(self, user_id, user_first, user_last, user_email):
        self.user_id = user_id
        self.user_first = user_first
        self.user_last = user_last
        self.user_email = user_email


@api.route('/', endpoint='users')
class Users(Resource):
    @api.marshal_with(user)
    @api.response(200, 'Resource successfully retrieved')
    def get(self):
        """
        Gets all users
        :return: Json object of all users
        """
        users = []
        user = User(
           1, "Jane", "Doe", "janedoe@me.com"
        )
        users.append(user)
        return users

    @api.doc(responses={201: 'User successfully created'})
    def post(self):
        """
        Creates a new user record.
        :return: User ID of the created record.
        """
        # Query routing function here
        return "Successfully Created User with ID: "


@api.route('/<user_id>')
@api.doc(params={'user_id': 'An ID'})
class UserRecord(Resource):
    @api.marshal_with(user, code=200, description='Success')
    def get(self, user_id):
        return "Successfully retrieved User %s" % user_id

    @api.doc(body=user, validate=True)
    @api.response(code=200, description='Success')
    def put(self, user_id):
        """
        Updates an existing user record based on user_id.
        :param user_id: Record number to be updated.
        :return: Json with user_id of updated record.
        """
        return "Successfully updated User %s " % user_id

    @api.response(code=200, description='User deleted')
    def delete(self, user_id):
        """
        Delete a user based on user_id.
        :param user_id: User to be deleted.
        :return: Json of user_id of deleted record.
        """
        return "Successfully deleted User %s " % user_id
    