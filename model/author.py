from sqlalchemy import UniqueConstraint

from library_webservice import db


class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String, nullable=False)
    middle_name = db.Column(db.String)
    # do not need a field here for books because books defines backref.
    UniqueConstraint(first_name, last_name, middle_name)

    # def __init__(self, **kwargs):
    #     self.author_id = kwargs['author_id']
    #     self.first_name = kwargs['first_name']
    #     self.last_name = kwargs['last_name']
    #     self.middle_name = kwargs['middle_name']

    def __repr__(self):
        return "<Author(author_id='%s', first_name='%s', last_Name='%s', middle_name ='%s')>" \
               % (self.author_id, self.first_name, self.last_name, self.middle_name)

    def to_dict(self):
        print('Author to_dict')
        author_dict = {
            'author_id': self.author_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'middle_name': self.middle_name
        }
        return author_dict

    def update(self, **kwargs):
        for key, value in kwargs:
            self[key] = value
