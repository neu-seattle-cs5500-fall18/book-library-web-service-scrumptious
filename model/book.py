from library_webservice import db

#Helper table for many to many relationship.
authorship = db.Table('authorship',
                      db.Column('book_id', db.Integer, db.ForeignKey('book.book_id'), primary_key=True),
                      db.Column('author_id', db.Integer, db.ForeignKey('author.author_id'), primary_key=True))


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    publish_date = db.Column(db.Date, nullable=False)
    subject = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    book_note = db.Column(db.String, nullable=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, book_id, title, publish_date, subject, genre, book_note, is_deleted):
        self.book_id = book_id
        self.title = title
        self.publish_date = publish_date
        self.subject = subject
        self.genre = genre
        self.book_note = book_note
        self.is_deleted = is_deleted

    def __repr__(self): return'<Book %r>' % self.title

    def to_dict(self):
        print('Book to_dict')
        book_dict = {
            'book_id': self.user_id,
            'title': self.title,
            'publish_date': self.publish_date,
            'subject': self.subject,
            'book_note': self.book_note,
            'is_deleted': self.is_deleted
        }
        return book_dict
