from library_webservice import db
from model import book


class BookCollection(db.Model):
    collection_id: db.Column(db.Integer, primary_key=True)
    book_ids: db.Column('book_id', backref='Book', lazy=True)
    title: db.Column(db.String)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

