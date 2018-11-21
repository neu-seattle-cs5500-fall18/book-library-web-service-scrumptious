from model import db

# Helper table for many to many relationship.
authorship_table = db.Table('authorship',
                            db.Column('book_id', db.Integer, db.ForeignKey('book.book_id'), primary_key=True),
                            db.Column('author_id', db.Integer, db.ForeignKey('author.author_id'), primary_key=True))


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    publish_date = db.Column(db.Date, nullable=False)
    subject = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    notes = db.relationship('Note', backref=db.backref('book'))
    authors = db.relationship('Author', secondary=authorship_table, backref=db.backref('books', lazy='dynamic'))
    copies = db.relationship('BookCopy', cascade="all,delete", backref=db.backref('book'))

    def __repr__(self): return"<Book(book_id='%s',title='%s',publish_date='%s',subject='%s',genre='%s'," \
                              "book_note='%s',authors='%s',copies='%s'>" \
                              % (self.book_id, self.title, self.publish_date, self.subject, self.genre, self.notes,
                                 self.authors, self.copies)

    def to_dict(self):
        print('Book to_dict')
        book_dict = {
            'book_id': self.book_id,
            'title': self.title,
            'publish_date': self.publish_date,
            'subject': self.subject,
            'genre': self.genre,
            'notes': self.notes,
            'authors': self.authors,
            'copies': self.copies
        }
        return book_dict

    def update(self, **kwargs):
        print('Book.update()')
        for key, value in kwargs.items():
            setattr(self, key, value)



