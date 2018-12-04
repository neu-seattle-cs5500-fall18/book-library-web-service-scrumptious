import pytest
from model import db

from app_factory import create_app

# # This file sets up fixtures to be used for scoped testing.

@pytest.fixture(scope='session')
def client(request):
    print('test fixture client')

    # Create instance of app via factory and configure as test
    test_app = create_app(test_flag=True)
    test_app.config['TESTING'] = True
    client = test_app.test_client()

    context = test_app.app_context()
    context.push()

    print('db tables created')

    yield client

    context.pop()

    return client


@pytest.fixture(scope='session')
def test_db(client):
    #app already has url to test db instance.
    test_db = db
    # initialize db
    test_db.init_app(client)

    return test_db

# #
# @pytest.fixture(scope='function')
# def function_test(test_db, request):
#
#     # # connect to db
#     # connection = test_db.engine.connect()
#     # # creates transaction object on each connection.
#     # transaction = connection.begin()
#     #
#     # #do need to commit?()
#
#
#     yield test_db
#
#     test_db.session.rollback()
#
#     # request.addfinalizer(teardown())




