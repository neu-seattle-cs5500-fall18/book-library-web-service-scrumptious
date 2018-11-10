from library_webservice import db

collection_table = db.Table('collections',
                            db.Column('book_id', db.Integer, db.ForeignKey('book.book_id'), primary_key=True),
                            db.Column('collection_id', db.Integer, db.ForeignKey('collection.collection_id'), primary_key=True))


class BookCollection(db.Model):
    collection_id = db.Column(db.Integer, primary_key=True)
    book_ids = db.relationship('Collection', secondary=collection_table, backref=db.backref('books', lazy='dynamic'))
    title = db.Column(db.String, nullable=False, unique=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self): return "<Collection(collection_id='%s',books='%s'>" \
                               % (self.collection_id, self.book.ids)

    def to_dict(self):
        print('Book collections to_dict')
        collection_dict = {
            'collection_id': self.collection_id,
            'book_ids': self.book_ids,
            'title': self.title
        }
        return collection_dict

    def update(self, **kwargs):
        for key, value in kwargs:
            self[key] = value
