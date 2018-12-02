import os
import tempfile
import sqlite3
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apis import api

# This file sets up fixtures to be used for scoped testing.
basedir = os.path.abspath(os.path.dirname(__file__))

@pytest.fixture
def client():
    test_app = Flask(__name__)
    test_app.config['TESTING'] = True
    test_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'test.db')
    db = SQLAlchemy()
    client = test_app.test_client()

    print('App Initialized')

    with test_app.app_context():
        api.init_app(test_app)
        db.init_app(test_app)
        db.create_all()
        print('db tables created')

    yield client
    print('testing over')

    db.drop_all()
    os.close(test_app.config['SQLALCHEMY_DATABASE_URI'])
    os.unlink(test_app.config['SQLALCHEMY_DATABASE_URI'])
    print('unlinked from db')


#
# @pytest.fixture(scope='session')
# def test_client(request):
#     """
#     Fixture to setup a new application for testing and database, and tear down application and database.
#     :return: None
#     """
#     print('Create fixture test_client')
#     # Create new application and configure
#     test_app = Flask(__name__)
#     # Configure app for testing
#     test_app.config['TESTING'] = True
#     test_app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB_URI
#     api.init_app(test_app)
#
#     context =  test_app.app_context()
#     context.push()
#
#     def teardown():
#         print('Teardown test_client')
#         context.pop()
#
#     #use add finalizer instead of yield to ensure all resources are closed.
#     request.addfinalizer(teardown)
#     return test_client
#
#
# @pytest.fixture(scope='session')
# def test_db(test_client, request):
#     print('Create fixture test_db')
#     #session wide database
#     if os.path.exists(TEST_DB_URI):
#         os.unlink(TEST_DB_URI)
#
#     def teardown():
#         print('Teardown test_db')
#         _db.drop_all()
#         os.close(TEST_DB_URI)
#
#     _db.app = test_client
#     _db.create_all()
#     request.addfinalizer(teardown)
#     return _db
#
#
# @pytest.fixture(scope = 'function')
# def test_session(test_db, request):
#     print('Create fixture test_session')
#     #creates database session
#     connection = test_db.engine.connect()
#     transaction = connection.begin()
#
#     options = dict(bind=connection, binds={})
#     # this is a scoped session object: a registry of Session objects
#     # This is multithread safe.
#     #https://docs.sqlalchemy.org/en/latest/orm/contextual.html
#     test_session = test_db.create_scoped_session(options=options)
#
#     def teardown():
#         print('Teardown test_session')
#         transaction.rollback()
#         connection.close()
#         #Remove scoped session
#         test_session.remove()
#
#     request.addfinalizer(teardown())
#     return test_session
#
#
