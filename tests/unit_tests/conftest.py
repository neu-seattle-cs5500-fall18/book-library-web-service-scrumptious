import pytest
from model.author import Author
from model.book import Book
from model.book_copy import BookCopy
from model.note import Note
from model.user import User
from data_access_layer.book_dao import BookDao
from data_access_layer.author_dao import AuthorDao
from data_access_layer.note_dao import NoteDao
from data_access_layer.book_copy_dao import BookCopyDao
import pytest
#from model import db
from model.book import Book

from app_factory import create_app

# # This file sets up fixtures to be used for scoped testing.

#@pytest.fixture(scope='session')
# def client():
#     print('test fixture client')
#     # Create instance of app via factory and configure as test
#     test_app = create_app(test_flag=True)
#
#     #handles context locals
#     client = test_app.test_client()
#
#     #application context
#     context = test_app.app_context()
#     #add context to stack
#     context.push()
#
#     #testing block for tests that call client fixture
#     yield client
#
#     #remove from stack
#     context.pop()
#
#     return client
#

# @pytest.fixture(scope='session')
# def test_db(client):
#    # app already has url to test db instance.
#     test_db = db
#   #  Associate db with current app.
#     test_db.init_app(client)
#
#
#   #  add initial objects here.
#    book1 = Book(title='Old Man', publish_date='1980', subject='Fiction', genre='Novel')
#    book2 = Book(title='The Left Hand of Darkness', publish_date='1975', subject='Fiction', genre='Science Fiction')
#
#    test_db.session.add(book1)
#    test_db.session.add(book2)
#    test_db.session.commit()
#
#
#    return test_db



# @pytest.fixture(scope='function')
# def function_test(test_db):
#
#     connection = test_db.engine.connect()
#     # creates transaction object on each connection.
#     transaction = connection.begin()
#     session = test_db.create_scoped_session()
#     test_db.session = session
#
#     yield test_db
#
#     transaction.rollback()
#     connection.close()
#     session.remove()
#
#     return session
#
# this file sets up fixtures for scoped testing
# Label instances that haven't been added to db as 'new_Class#' ie new_book1.
# Label instances that have been added to db as 'class#' ie book1.

@pytest.fixture(scope='module')
def book1_dict():
    book = dict(book_id=1,title='Old Man', publish_date='1980', subject='Fiction', genre='Novel')
    return book


def book2_dict():
    book = dict(book_id=2,title='The Left Hand of Darkness', publish_date='1975', subject='Fiction', genre='Science Fiction')
    return book


@pytest.fixture(scope='module')
def new_book1():
    book = Book(title='Old Man', publish_date='1980', subject='Fiction', genre='Novel')
    return book


@pytest.fixture(scope='module')
def new_book2():
    book = Book(title='The Left Hand of Darkness', publish_date='1975', subject='Fiction', genre='Science Fiction')
    return book


@pytest.fixture(scope='module')
def book1():
    book = Book(book_id=1, title='Old Man', publish_date='1980', subject='Fiction', genre='Novel')
    return book


@pytest.fixture(scope='module')
def book2():
    book = Book(book_id=2, title='The Left Hand of Darkness', publish_date='1975', subject='Fiction',
                genre='Science Fiction')
    return book


@pytest.fixture(scope='module')
def new_author1():
    author = Author(first_name='Herman', last_name='Melville', middle_name='M')
    return author


@pytest.fixture(scope='module')
def new_author2():
    author = Author(first_name='Ursela', last_name='LeGuin', middle_name='K')
    return author


@pytest.fixture(scope='module')
def existing_author1():
    author = Author(author_id=1, first_name='Herman', last_name='Melville', middle_name='M')
    return author


@pytest.fixture(scope='module')
def existing_author2():
    author = Author(author_id=2, first_name='Ursela', last_name='LeGuin', middle_name='K')
    return author


@pytest.fixture(scope='module')
def new_book_copy1():
    copy = BookCopy(book_id=1, is_checked_out=False)
    return copy


@pytest.fixture(scope='module')
def new_book_copy2():
    copy = BookCopy(book_id=2, is_checked_out=False)
    return copy


@pytest.fixture(scope='module')
def book_copy1():
    copy = BookCopy(book_copy_id=1, book_id=1, is_checked_out=False)
    return copy


@pytest.fixture(scope='module')
def book_copy2():
    copy = BookCopy(book_copy_id=2, book_id=2, is_checked_out=False)
    return copy


@pytest.fixture(scope='module')
def new_note():
    note = Note(note_title='Cool Book', note='Really enjoyed the book', book_id=1)
    return note


@pytest.fixture(scope='module')
def new_user():
    user = User(user_first_name='FirstaaName', user_last_name='LastName', email='asdf@some.com')
    return user


@pytest.fixture(scope='module')
def new_book_dao():
    book_dao = BookDao
    return book_dao


@pytest.fixture(scope='module')
def new_author_dao():
    author_dao = AuthorDao
    return author_dao


@pytest.fixture(scope='module')
def new_note_dao():
    note_dao = NoteDao
    return note_dao


@pytest.fixture(scope='module')
def new_book_copy_dao():
    book_copy_dao = BookCopyDao
    return book_copy_dao