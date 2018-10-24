from library_webservice import db


class Checkout(db.Model):
    checkout_id: db.Column(db.Integer, primary_key=True)
    user_id: db.Column(db.Integer, )
    book_id: db.Column(db.Integer, )
    checkout_date: db.Column(db.Date, Nullable=False)
    due_date: db.Column(db.Date, nullable=False)
    return_date: db.Column(db.Date, nullable=False)

