from model import db


class Note(db.Model):
    note_title = db.Column(db.String, primary_key=True)
    note = db.Column(db.String, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False)

    def __repr__(self):
        return '<Note %r : %r %r>' %(self.note_title, self.note, self.book_id)

    def to_dict(self):
        """
        Method to convert a Note object to a dict object representation
        :return: dict representation of a Note
        """
        a_dict = {
            'note_title': self.note_title,
            'note': self.note,
            'book_id': self.book_id
        }

        return a_dict

    def update(self, **kwargs):
        """
        Method to update a Note's attributes
        :param kwargs: A dict of valid key-value pairs
        :return: None
        """
        for key, value in kwargs.items():
            setattr(self, key, value)


