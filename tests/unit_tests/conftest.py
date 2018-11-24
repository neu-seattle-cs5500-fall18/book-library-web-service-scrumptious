import pytest
from model.author import Author
from model.book import Book
from model.book_copy import BookCopy
from model.note import Note

# this file sets up fixtures for scoped testing

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

