from library_webservice import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String, nullable=False)
    user_last_name = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, nullable=False)

    def __repr__(self): return'<User %r>' %(self.user_id)

    def to_dict(self):
        print('User to_dict')
        user_dict = {
            'user_id': self.user_id,
            'user_first_name': self.user_first_name,
            'user_last_name': self.user_last_name,
            'user_email': self.email,
        }
        return user_dict



