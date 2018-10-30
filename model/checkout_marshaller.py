
class CheckOutMarshaller(object):
    def __init__(self, checkout_id, user_id, book_id, checkout_date, due_date, return_date):
        self.checkout_id = checkout_id
        self.user_id = user_id
        self.book_id = book_id
        self.checkout_date = checkout_date
        self.due_date = due_date
        self.return_date = return_date

        self.status = 'active'
