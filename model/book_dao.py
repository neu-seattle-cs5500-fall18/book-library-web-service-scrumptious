from flask import abort
from library_webservice import db
from model.book import Book
from model.book_copy import BookCopy

# Book querying actions.
# !!! use lower case db.session

def query_by_id(book_id):
    a_book = Book.query.get(book_id)

    if a_book is None:
        abort(400, 'Record not found')
    else:
        return a_book

def query_books(query_params):
    """
    Queries all books in library
    :return: Dict of books as book_db_model
    """
    if query_params is None:
        book_list = Book.query.getall()
        return book_list

def create_new_book(request_body):
    # does kwargs work here?
    new_book = Book(request_body)

    db.session.add(new_book)
    db.session.commit()

    return new_book.book_id


def update_book_record(book_id, json):
    book = Book.query.get(book_id)
    book = Book(json)
    book.book_id = book_id
    db.session.commit()
    return book

def delete_book(book_id):
    book = Book.query.get(book_id)
    book.deleted = True
    db.session.commit()
    return book


# Notes actions
def get_notes(book_id):
    book = Book.query.get(book_id)
    notes = book.notes
    return notes

def edit_note(book_id, json):
    book = query_by_id(book_id)
    book.notes = json
    db.session.commit()
    return book.book_id

def delete_note(book_id):
    book = query_by_id(book_id)
    book.notes = ""
    db.session.commit()
    return book.book_id


# Copies actions
def get_book_copies(book_id):
    book = query_by_id(book_id)
    copies = BookCopy.query.filter(BookCopy.book_id == book.book_id)
    return copies

def insert_book_copy(book_id):
    book = query_by_id(book_id)
    copy = BookCopy(book_id)
    db.session.add(copy)
    db.session.commit()
    return copy.book_copy_id

def delete_book_copy(book_id, book_copy_id):
    return


