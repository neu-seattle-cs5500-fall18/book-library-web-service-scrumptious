from flask import abort
from library_webservice import db
from model import author_dao
from model.book import Book
from model import book_copy_dao


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
        query_results = Book.query.getall()
        return query_results
    else:
        query_results = Book.query.filter_by(**kwargs)
        return query_results


def create(book_dict, list_authors):
    print("book_dao.create()")
    new_book = Book(**book_dict)
    db.session.add(new_book)
    db.session.commit()
    print(new_book)
    author_dao.create(new_book, list_authors)
    book_copy_dao.create(new_book)
    print("book_dao.create() ==> Complete")
    print(new_book)
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
