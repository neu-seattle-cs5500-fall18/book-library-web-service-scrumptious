from library_webservice import db


class User(db.Model):
    user_id: db.Column(db.Integer, primary_key=True)
    user_first_name: db.Column(db.String, nullable=False)
    user_last_name: db.Column(db.String, nullable=False)
    email: db.column(db.String, nullable=False)
    is_deleted: db.column(db.Boolean, nullable=False, default=False)
