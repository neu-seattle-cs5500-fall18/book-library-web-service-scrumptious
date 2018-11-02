from library_webservice import db


class Author(db.Model):
    #how to enforce that come combination of names is not null?
    author_id: db.Column(db.Integer, primary_key=True)
    first_name: db.Column(db.String)
    last_name: db.Column(db.String)
    middle_name: db.Column(db.String)
    pen_name: db.Column(db.String)

    def __init__(self, author_id, first_name, last_name, middle_name, pen_name):
        self.author_id = author_id
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.pen_name = pen_name

    def to_diect(self):
        print('Author to_dict')
        author_dict = {
            'author_id': self.author_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'middle_name':self.middle_name,
            'pen_name': self.pen_name
        }
        return author_dict



