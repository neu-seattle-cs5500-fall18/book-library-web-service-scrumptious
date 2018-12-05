import datetime
import json
import pytest
from model.author import Author
from model.book import Book
from model.book_copy import BookCopy
from model.note import Note
from model.user import User


@pytest.fixture(scope='module')
def book1_dict():
    book = {
        'title': 'Old Man',
        'publish_date': '1980-05-12',
        'subject': 'Fiction',
        'genre': 'Novel',
        'notes': [],
        'authors': [
            {
                'first_name': 'Herman',
                'last_name': 'Melville',
                'middle_name': 'M'
            }
        ]
    }
    return book


def book2_dict():
    book = dict(book_id=2,title='The Left Hand of Darkness', publish_date='1975', subject='Fiction', genre='Science Fiction')
    return book


@pytest.fixture(scope='module')
def new_book1():
    book = Book(title='Old Man', publish_date='1980-05-12', subject='Fiction', genre='Novel', authors=[])
    return book


@pytest.fixture(scope='module')
def new_book2():
    book = Book(title='The Left Hand of Darkness', publish_date='1975', subject='Fiction', genre='Science Fiction')
    return book


@pytest.fixture(scope='module')
def book1():
    author = Author(author_id=1, first_name='Herman', last_name='Melville', middle_name='M')
    book = Book(book_id=1, title='Old Man', publish_date='1980-05-12', subject='Fiction', genre='Novel', authors=[author])
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
def expect_book1_dict():
    book = {
        'book_id' : 1,
        'title': 'Old Man',
        'publish_date': '1980-05-12',
        'subject': 'Fiction',
        'genre': 'Novel',
        'notes': [],
        'authors': [
            {'author_id': 1,
             'first_name': 'Herman',
             'last_name': 'Melville',
             'middle_name': 'M'
             }
        ]
    }
    return book


@pytest.fixture(scope='module')
def expected_post_book1():
    copies = {'copies': [
            {
                'book_copy_id': 1,
                'book_id': 1,
                'is_checked_out': False
            }
        ]}
    authors = {'authors': [
            {
               'first_name': 'Herman',
               'last_name': 'Melville',
               'middle_name': 'M'
            }
        ]}
    book = [{
        'copies': copies,
        'title': 'Old Man',
        'publish_date': '1980-05-12',
        'subject': 'Fiction',
        'genre': 'Novel',
        'notes': [],
        'authors': authors
    }]

    book = json.dumps(book)
    return book

