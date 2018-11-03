from flask import abort
from library_webservice import db
from model.book import Book

# Book querying actions.
# !!! use lower case db.session
def query_by_id(book_id):
    a_book = Book.query.get(book_id)
    if a_book is None:
        abort(400, 'Record not found')
    else:
        return a_book


# Does this need to not accept everything upstream?
def query_books(**query_params):
    """
    Queries all books in library
    :return: List of Book
    """
    if query_params is None:
        book_list = Book.query.getall()
        return book_list


#trying **kwargs here.
def create_new_book(**book_dict):
    new_book = Book(**book_dict)
    db.session.add(new_book)
    db.session.commit()
    return new_book.book_id


def update_book_record(book_id, **book_dict):
    book = Book.query.get(book_id)
    book = Book(**book_dict)
    db.session.commit()
    return book


def delete_book(book_id):
    book = Book.query.get(book_id)
    book.deleted = True
    db.session.commit()
    return book


# Notes actions
def get_note(book_id):
    book = Book.query_by_id(book_id)
    note = book.note
    return note

def edit_note(book_id, note):
    book = query_by_id(book_id)
    book.notes = note
    db.session.commit()
    return book.book_id


def delete_note(book_id):
    book = query_by_id(book_id)
    book.notes = ""
    db.session.commit()
    return book.book_id
