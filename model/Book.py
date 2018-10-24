from library_webservice import db

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author_first_name = db.Column(db.String, nullable=False)
    author_last_name = db.Column(db.String, nullable=False)
    publish_date = db.Column(db.Date, nullable=False)
    subject = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    loaned_out = db.Column(db.Boolean, nullable=False)
    notes = db.Column(db.String, nullable=True)
    #'collections': fields.List(fields.Integer, descritpion='List of Collections a book belongs to.'),
    #'is_deleted': fields.Boolean(description='Field to indicate of a book is deleted or not, for soft delete.')
