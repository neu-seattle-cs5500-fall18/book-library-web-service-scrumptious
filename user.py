from flask import Flask


# User class
class User:
    def __init__(self, user_id, user_first, user_last):
        self.user_id = user_id
        self.user_first = user_first
        self.user_last = user_last
