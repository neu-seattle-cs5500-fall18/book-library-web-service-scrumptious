from library_webservice import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String, nullable=False)
    user_last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return "User: %r %r %r %r %r" %self.user_id %self.user_first_name %self.user_last_name %self.email %self.is_deleted
