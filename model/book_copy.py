from library_webservice import db


class BookCopy(db.Model):
    book_copy_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False)
    is_checked_out = db.Column(db.Boolean, nullable=False, default=False)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    #
    # def __init__(self, book_copy_id, is_checked_out, is_deleted):
    #     self.book_copy_id = book_copy_id
    #     self.is_checked_out = is_checked_out
    #     self.is_deleted = is_deleted

    def __repr__(self):
        return("<BookCopy(book_copy_id='%s',book_id='%s',is_checked_out='%s',is_deleted='%s'>"
               % (self.book_copy_id,self.book_id,self.is_checked_out,self.is_deleted))

    def to_dict(self):
        print('Book Copy to_dict')
        copy_dict = {
            'book_copy_id': self.book_copy_id,
            'book_id': self.book_id,
            'is_checked_out': self.is_checked_out,
            'is_deleted': self.is_deleted
        }
        return copy_dict

    def update(self, **kwargs):
        for key, value in kwargs:
            self[key] = value

