from flask import Flask
import os


def create_app(name, settings_override=None):
    app = Flask(name)

    if (settings_override is None):
        database_uri = os.environ.get("DATABASE_URL", "postgres://postgres@localhost:5432/booklibrary")
        app.config['SQLALCHEMY_DATABASE_URI']=database_uri

    else:
        app.config.update(settings_override)
        #app.config['TESTING'] = True
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@localhost:5432/booklibrary'

    from apis import api
    api.init_app(app)

    return app
