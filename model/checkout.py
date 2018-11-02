from library_webservice import db


class Checkout(db.Model):
    checkout_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    checkout_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, checkout_id, user_id, book_id, checkout_date, due_date, return_date):
        self.checkout_id = checkout_id
        self.user_id = user_id
        self.book_id = book_id
        self.checkout_date = checkout_date
        self.due_date = due_date
        self.return_date = return_date



