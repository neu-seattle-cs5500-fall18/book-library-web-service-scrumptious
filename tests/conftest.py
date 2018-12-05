import pytest
from model import db
from model.book import Book

from app_factory import create_app

# # This file sets up fixtures to be used for scoped testing.

@pytest.fixture(scope='session')
def client():
    print('test fixture client')
    # Create instance of app via factory and configure as test
    test_app = create_app(test_flag=True)

    #handles context locals
    client = test_app.test_client()

    #application context
    context = test_app.app_context()
    #add context to stack
    context.push()

    #testing block for tests that call client fixture
    yield client

    #remove from stack
    context.pop()

    return client


@pytest.fixture(scope='session')
def test_db(client):
    #app already has url to test db instance.
    test_db = db
    # Associate db with current app.
    test_db.init_app(client)


    # add initial objects here.
    book1 = Book(title='Old Man', publish_date='1980', subject='Fiction', genre='Novel')
    book2 = Book(title='The Left Hand of Darkness', publish_date='1975', subject='Fiction', genre='Science Fiction')

    test_db.session.add(book1)
    test_db.session.add(book2)
    test_db.session.commit()


    return test_db



@pytest.fixture(scope='function')
def function_test(test_db):

    connection = test_db.engine.connect()
    # creates transaction object on each connection.
    transaction = connection.begin()
    session = test_db.create_scoped_session()
    test_db.session = session

    yield test_db

    transaction.rollback()
    connection.close()
    session.remove()

    return session




