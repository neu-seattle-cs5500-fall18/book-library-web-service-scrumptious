from library_webservice import db


class Checkout(db.Model):
    checkout_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    checkout_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, checkout_id, user_id, book_id, checkout_date, due_date, return_date, is_deleted):
        self.checkout_id = checkout_id
        self.user_id = user_id
        self.book_id = book_id
        self.checkout_date = checkout_date
        self.due_date = due_date
        self.return_date = return_date
        self.is_deleted = is_deleted

    def __repr__(self): return'<Checkout %r>' %(self.checkout_id)

    def to_dict(self):
        print('Checkout to_dict')
        checkout_dict = {
            'checkout_id': self.checkout_id,
            'use_id': self.user_id,
            'book_id': self.book_id,
            'checkout_date': self.checkout_date,
            'due_date': self.due_date,
            'return_date': self.return_date,
            'is_deleted': self.is_deleted
        }
        return checkout_dict

