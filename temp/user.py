from flask import Flask


# User class
class User:
    def __init__(self, user_id, user_first_name, user_last_name, user_email):
        self.user_id = user_id
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_email = user_email
