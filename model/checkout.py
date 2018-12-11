from model import db


class Checkout(db.Model):
    checkout_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    book_copy_id = db.Column(db.Integer, nullable=False)
    checkout_date = db.Column(db.String, nullable=False)
    due_date = db.Column(db.String, nullable=False)
    return_date = db.Column(db.String, nullable=True)

    def __repr__(self): return"<Checkout(checkout_id='%s', user_id='%s', book_id='%s', book_copy_id='%s'," \
                              "checkout_date='%s', due_date='%s', return_date='%s'>" % \
                              (self.checkout_id, self.user_id, self.book_id, self.book_copy_id, self.checkout_date,
                               self.due_date, self.return_date)

    def to_dict(self):
        print('Checkout to_dict')
        checkout_dict = {
            'checkout_id': self.checkout_id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'book_copy_id': self.book_copy_id,
            'checkout_date': self.checkout_date,
            'due_date': self.due_date,
            'return_date': self.return_date,
        }
        return checkout_dict

    def update(self, **kwargs):
        print('Checkout.update()')
        for key, value in kwargs.items():
            setattr(self, key, value)
