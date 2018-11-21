from sqlalchemy import UniqueConstraint
from model import db
import re


pattern = re.compile('\A(\w\.)+')


class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String, nullable=False)
    middle_name = db.Column(db.String)
    UniqueConstraint(first_name, last_name, middle_name)

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
        print('Author.update()')
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def valid_input(first_name, last_name, middle_name):
        print("author_checker.valid_input()")
        return (first_name is None or first_name.isalpha() or pattern.match(first_name)) and \
               (middle_name is None or middle_name.isalpha() or pattern.match(middle_name)) and \
               (last_name.isalpha() or pattern.match(last_name))

    @staticmethod
    def clean_author(first_name, last_name, middle_name):
        print('author_checker.clean_author')

        if first_name is not None:
            first_name = first_name.lower().title()

        if middle_name is not None:
            if len(middle_name) == 1 and middle_name.isalpha():
                middle_name.append(".")
            elif pattern.match(middle_name):
                middle_name = middle_name[0].upper() + '.'
            else:
                middle_name.lower().title()

        formatted_author = {
            'first_name': first_name.lower().title(),
            'last_name': last_name,
            'middle_name': middle_name
        }
        print(formatted_author)
        return formatted_author
