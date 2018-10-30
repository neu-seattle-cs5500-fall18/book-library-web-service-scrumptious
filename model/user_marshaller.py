
class UserMarshaler(object):
    def __init__(self, user_id, user_first, user_last, user_email, is_deleted):
        self.user_id = user_id
        self.user_first = user_first
        self.user_last = user_last
        self.user_email = user_email
        self.is_deleted = is_deleted
