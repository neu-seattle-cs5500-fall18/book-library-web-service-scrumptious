from model import db


class BookCopy(db.Model):
    book_copy_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False)
    is_checked_out = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return("<BookCopy(book_copy_id='%s',book_id='%s',is_checked_out='%s'>"
               % (self.book_copy_id, self.book_id, self.is_checked_out))

    def to_dict(self):
        """
        Method to convert a book copy to a python dictionary data object
        :return: dict
        """
        print('Book Copy to_dict')
        copy_dict = {
            'book_copy_id': self.book_copy_id,
            'book_id': self.book_id,
            'is_checked_out': self.is_checked_out,
        }
        return copy_dict

    def update(self, **kwargs):
        """
        Method to update a book copy's attributes
        :param kwargs: A dict of valid key-value pairs
        :return: None
        """
        print('BookCopy.update()')
        for key, value in kwargs.items():
            setattr(self, key, value)

