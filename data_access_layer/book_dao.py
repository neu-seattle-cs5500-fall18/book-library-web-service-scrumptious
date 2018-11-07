from flask import abort
from library_webservice import db
from data_access_layer import author_dao, book_copy_dao
from model.book import Book


def query_by_id(book_id):
    a_book = Book.query.get(book_id)
    if a_book is None:
        abort(400, 'Record not found')
    else:
        return a_book


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
    author_dao.create(new_book, list_authors)
    book_copy_dao.create(new_book)
    print("book_dao.create() ==> Complete")
    return new_book


##Be Careful with this.
def update(book_id, **kwargs):
    book = Book.query.get(book_id)
    book.update(**kwargs)
    db.session.commit()
    return book


def delete(book_id):
    book = Book.query.get(book_id)

    if book is None:
        abort(400, 'No such book record')
    else:
        book.deleted = True
        # book_copy_dao.delete()
        # author_dao.delete()
        db.session.commit()
        return book


# Notes actions
def get_note(book_id):
    book = Book.query_by_id(book_id)
    if book is None:
        abort(400, 'No such record')
    else:
        note = book.note
        return note


def edit_note(book_id, note):
    book = query_by_id(book_id)
    book.notes = note
    db.session.commit()
    return book


def delete_note(book_id):
    book = query_by_id(book_id)

    if book is None:
        abort(400, 'no such record')
    else:
        book.notes = 'None'
        db.session.commit()
        return book
