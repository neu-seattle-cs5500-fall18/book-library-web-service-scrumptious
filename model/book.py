from library_webservice import db

#Helper table for many to many relationship.
authorship_table = db.Table('authorship',
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
    authors = db.relationship('Author', secondary=authorship_table, lazy='subquery',
                              backref=db.backref('books',lazy=True))

    def __init__(self, **kwargs):
        self.book_id = kwargs['book_id']
        self.title = kwargs['title']
        self.publish_date = kwargs['publish_date']
        self.subject = kwargs['subject']
        self.genre = kwargs['genre']
        self.book_note = kwargs['book_note']
        self.is_deleted = kwargs['is_deleted']
        self.authors = kwargs['authors']

    def __repr__(self): return"<Book(book_id='%s',title='%s',publish_date='%s',subject='%s',genre='%s'," \
                              "book_note='%s',is_deleted='%s'>" \
                              %(self.book_id,self.title,self.publish_date,self.subject,self.genre,self.book_note,
                                self.is_deleted)

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

    def update(self, **kwargs):
        for key, value in kwargs:
            self[key] = value

