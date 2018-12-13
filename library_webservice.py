# from alembic import command
from flask_migrate import Migrate
from app_factory import create_app


app = create_app(__name__)

from model import db
db.init_app(app)

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=False)
