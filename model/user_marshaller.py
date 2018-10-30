from apis.users_api import api
from flask_restplus import fields




# user_api_model_minimal = api.model('User_Minimal', {
#     'user_first_name': fields.String(description='The user\'s first name'),
#     'user_last_name': fields.String(description='The user\'s last name'),
#     'email': fields.String(description='The user\'s email address'),
# })


# class UserMarshaler(object):
#     def __init__(self, user_id, user_first, user_last, user_email, is_deleted):
#         self.user_id = user_id
#         self.user_first = user_first
#         self.user_last = user_last
#         self.user_email = user_email
#         self.is_deleted = is_deleted
