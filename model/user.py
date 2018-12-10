from model import db
from sqlalchemy import UniqueConstraint


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String, nullable=False)
    user_last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    UniqueConstraint(email)

    def __repr__(self): return'<User %r, %r, %r, %r,>' % \
                              (self.user_id,self.user_first_name,self.user_last_name,self.email)

    def to_dict(self):
        print('User to_dict')
        user_dict = {
            'user_id': self.user_id,
            'user_first_name': self.user_first_name,
            'user_last_name': self.user_last_name,
            'user_email': self.email,
        }
        return user_dict

    def update(self, **kwargs):
        print('User.update()')
        for key, value in kwargs.items():
            setattr(self, key, value)

