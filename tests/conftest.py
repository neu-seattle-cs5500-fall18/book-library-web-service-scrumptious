import os
import pytest

from app_factory import create_app
from model import db as _db


TESTDB = 'test_project.db'
TESTDB_PATH = "{}".format(TESTDB)
TEST_DATABASE_URI = 'sqlite:///' + TESTDB_PATH


@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""
    settings_override = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': TEST_DATABASE_URI,
        #'SQLALCHEMY_TRACK_MODIFICATIONS' : False,
    }
    app = create_app(__name__, settings_override)


    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    print("DB Fixture!")
    """Session-wide test database."""

    _db.init_app(app)
    _db.create_all()

    #db.create_all()


    def teardown():
        _db.drop_all()
        ctx.pop()
        os.unlink(TESTDB_PATH)

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def db(app, request):
    print("DB Fixture!")
    """Session-wide test database."""
    # if os.path.exists(TESTDB_PATH):
    #     os.unlink(TESTDB_PATH)
    #
    # def teardown():
    #     _db.drop_all()
    #     os.unlink(TESTDB_PATH)
    #
    # _db.app = app
    # _db.create_all()
    #
    # request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session