from model import db
from model.book import Book

collection_table = db.Table('collections',
                            db.Column('book_id', db.Integer, db.ForeignKey('book.book_id'), primary_key=True),
                            db.Column('collection_id', db.Integer, db.ForeignKey('book_collection.collection_id'), primary_key=True))


class BookCollection(db.Model):
    collection_id = db.Column(db.Integer, primary_key=True)
    book_ids = db.relationship(Book, secondary=collection_table, backref=db.backref('books', lazy='dynamic'))
    title = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self): return "<Collection(collection_id='%s',books='%s',title='%s'>" \
                               % (self.collection_id, self.book.ids,self.title)

    def to_dict(self):
        print('Book collections to_dict')
        list_of_books = []
        for book in self.book_ids:
            list_of_books.append({'book_id':book.book_id, 'title':book.title})
        print(list_of_books)
        collection_dict = {
            'collection_id': self.collection_id,
            'book_ids': list_of_books,
            'title': self.title
        }
        print(collection_dict)
        return collection_dict

    def update(self, **kwargs):
        for key, value in kwargs:
            self[key] = value
