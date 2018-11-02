from library_webservice import db


class Collection(db.Model):
    collection_name: db.Column(db.Integer, primary_key=True)
    collection_books: db.relationship('CollectionBooks', backref='Collection', lazy=True)
    
    
class CollectionBooks(db.model):
    id: db.Column(db.Integer, primary_key=True)
    collection_name = db.Column(db.String, db.ForeignKey('Collection.collection_name'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('Book.book_id'), nullable=False)

