from flask import Flask
import os


def create_app(test_flag=None):
    app = Flask(__name__)

    if (test_flag is None):
        database_uri = os.environ.get("DATABASE_URL", "postgres://postgres@localhost:5432/booklibrary")
        app.config['SQLALCHEMY_DATABASE_URI']=database_uri

    else:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@localhost:5432/booklibrary'

    from apis import api
    api.init_app(app)

    return app
