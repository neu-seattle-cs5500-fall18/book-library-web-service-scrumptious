# import os
# import tempfile
from model.author import Author
from model.book import Book
from model.book_copy import BookCopy
from model.note import Note
import pytest

# from library_webservice import app

@pytest.fixture(scope = 'module')
def new_book():
    book = Book(book_id=1, title='Old Man',publish_date='1980',subject='Fiction',genre='Novel')
    return book

@pytest.fixture(scope = 'module')
def new_author():
    author = Author(author_id=1, first_name='Herman', last_name='Melville', middle_name='M')
    return author

@pytest.fixture(scope = 'module')
def new_book_copy():
    copy = BookCopy(book_copy_id=1, book_id= 1, is_checked_out=False)
    return copy

@pytest.fixture(scope = 'module')
def new_note():
    note = Note(note_title='Cool Book',note='Really enjoyed the book', book_id=1)
    return note


@pytest.fixture
def client():
    db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.app.config['TESTING'] = True
    client = app.app.test_client()

    with app.app.app_context():
        app.init_db()

    yield client

    os.close(db_fd)
    os.unlink(app.app.config['DATABASE'])


def test_assertion_works():
    assert 1 == 1

def test_empty_db(client):
    rv = client.get('/authors')
    assert b'No entries here so far' in rv.data
