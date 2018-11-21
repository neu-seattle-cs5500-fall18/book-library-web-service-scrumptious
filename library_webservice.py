# from alembic import command
from flask import Flask
from flask_migrate import Migrate
import os

app = Flask(__name__)
database_uri = os.environ.get("DATABASE_URL", "postgres://postgres@localhost:5432/booklibrary")
app.config['SQLALCHEMY_DATABASE_URI']=database_uri

from model import db
db.init_app(app)

from apis import api
api.init_app(app)

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)
