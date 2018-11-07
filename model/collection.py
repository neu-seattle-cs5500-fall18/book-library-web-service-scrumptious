from library_webservice import db


class BookCollection(db.Model):
    collection_id = db.Column(db.Integer, primary_key=True)
    book_ids = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

