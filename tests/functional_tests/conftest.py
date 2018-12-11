import pytest
from model.author import Author
from model.book_copy import BookCopy
from model.note import Note
from model.user import User


@pytest.fixture(scope='module')
def book1_dict():
    book = {
        'title': 'Old Man',
        'publish_date': '1980-05-12',
        'subject': 'Non-Fiction',
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


@pytest.fixture(scope='module')
def book2_dict():
    book = {
        'title': 'Old Man and the Sea',
        'publish_date': '1910-05-12',
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


@pytest.fixture(scope='module')
def book3_dict():
    book = {
        'title': 'Travels With Charlie',
        'publish_date': '1970-05-12',
        'subject': 'Fiction',
        'genre': 'Literary Fiction',
        'notes': [],
        'authors': [
            {
                'first_name': 'John',
                'last_name': 'Steinbeck',
                'middle_name': ''
            }
        ]
    }
    return book


@pytest.fixture(scope='module')
def book4_dict():
    book = {
        'title': '1984',
        'publish_date': '1940-05-12',
        'subject': 'Fiction',
        'genre': 'Literary Fiction',
        'notes': [
            {
                'note_title': 'Dystopia',
                'note': 'THE dystopian novel.'
            }
        ],
        'authors': [
            {
                'first_name': 'George',
                'last_name': 'Orwell',
                'middle_name': ''
            }
        ]
    }
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
def expect_book1_dict():
    book = {
        "book_id" : 1,
        "title": "Old Man",
        "publish_date": "1980-05-12",
        "subject": "Non-Fiction",
        "genre": "Novel",
        "notes": [],
        "authors": [
            {"author_id": 1,
             "first_name": "Herman",
             "last_name": "Melville",
             "middle_name": "M"
             }
        ]
    }
    return book

@pytest.fixture(scope='module')
def expect_book2_dict():
    book = {
        'book_id' : 2,
        'title': 'Old Man and the Sea',
        'publish_date': '1910-05-12',
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
def expect_book3_dict():
    book = {
        'book_id' : 3,
        'title': 'Travels With Charlie',
        'publish_date': '1970-05-12',
        'subject': 'Fiction',
        'genre': 'Literary Fiction',
        'notes': [],
        'authors': [
            {
                'author_id' : 2,
                'first_name': 'John',
                'last_name': 'Steinbeck',
                'middle_name': ''
            }
        ]
    }
    return book



@pytest.fixture(scope='module')
def expected_book3_fulldict():
    book = {'copies': [
            {
                'book_copy_id': 3,
                'book_id': 3,
                'is_checked_out': False
            }],
            'book_id': 3,
            'title': 'Travels With Charlie',
            'publish_date': '1970-05-12',
            'subject': 'Fiction',
            'genre': 'Literary Fiction',
            'notes': [],
            'authors': [
                {
                    'author_id': 2,
                    'first_name': 'John',
                    'last_name': 'Steinbeck',
                    'middle_name': ''
                }
            ]

        }
    return book


@pytest.fixture(scope= 'module')
def expected_copies1():
    copy = {
            'book_copy_id': 1,
            'book_id': 1,
            'is_checked_out' : False,
        }

    return copy


@pytest.fixture(scope= 'module')
def expected_copies2():
    copy = {
            'book_copy_id': 2,
            'book_id': 1,
            'is_checked_out' : False,
    }


    return copy

