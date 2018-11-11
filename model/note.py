from library_webservice import db


class Note(db.Model):
    note_title = db.Column(db.String, primary_key=True)
    note = db.Column(db.String, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False)

    def __repr__(self):
        return '<Note %r : %r>' %(self.note_title, self.note)

    def to_dict(self):
        a_dict = {
            'note_title': self.note_title,
            'note' : self.note
        }

        return a_dict

    def update(self, **kwargs):
        for key, value in kwargs:
            self[key] = value


