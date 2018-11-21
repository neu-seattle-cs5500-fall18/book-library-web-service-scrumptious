from model import db


class Checkout(db.Model):
    checkout_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    book_copy_id = db.Column(db.Integer, nullable=False)
    checkout_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)

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
        }
        return checkout_dict

