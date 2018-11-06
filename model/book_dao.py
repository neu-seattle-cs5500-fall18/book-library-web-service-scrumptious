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
#takes query args and values as a dict
def query_books(**kwargs):
    """
    Queries all books in library
    :return: List of Book
    """
    if kwargs is None:
        book_list = Book.query.getall()
        return book_list
    #else filter by kwargs


def create(book_dict):
    print("book_dao.create()")
    print(book_dict)
    new_book = Book(**book_dict)
    print(new_book)
    print("new book created")
    db.session.add(new_book)
    print("added to session")
    db.session.commit()
    print("commited to session")
    return new_book


def update(book_id, **kwargs):
    book = Book.query.get(book_id)
    book.update(kwargs)
    db.session.commit()
    return book.to_dict()


def delete(book_id):
    book = Book.query.get(book_id)
    book.deleted = True
    db.session.commit()
    return book.to_dict()


# Notes actions
def get_note(book_id):
    book = Book.query_by_id(book_id)
    note = book.note
    return note


def edit_note(book_id, note):
    book = query_by_id(book_id)
    book.notes = note
    db.session.commit()
    return book.to_dict()


def delete_note(book_id):
    book = query_by_id(book_id)
    book.notes = ""
    db.session.commit()
    return book.to_dict()
