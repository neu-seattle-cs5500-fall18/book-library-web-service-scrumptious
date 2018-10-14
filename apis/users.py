from flask_restplus import Namespace

api = Namespace('users', description='User related operations')


# this allows for a string query
# GET - returns all users
# POST - add a user
# PUT - bulk update user records
# DELETE - bulk delete users
# users? <param> = specify query parameters.
@api.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    # error checking here for valid request.
        parameters = request.args
        json_obj = request.json

# this does not allow for a string query
# GET - returns specific user
# POST - N/A
# PUT - edit user
# DELETE - remove user
@api.route('/users/<user>', methods=['GET', 'PUT', 'DELETE'])
def access_user(user):
    json_obj = request.json