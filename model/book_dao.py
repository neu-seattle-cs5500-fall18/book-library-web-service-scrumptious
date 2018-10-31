from library_webservice import db
from model.book import Book


def get_all_books():
    book_list = Book.query.getall()

    return book_list

def create_new_book(request_body):
    new_book = Book(request_body)

    db.Session.add(new_book)
    db.Session.commit()

    return new_book.book_id

def get_book(book_id):
    book = Book.query.get(book_id)

    return book

def update_book(book_id, json):
    book = Book.query.get(book_id)
    book = Book(json)
    book.book_id = book_id
    db.Session.commit()
    return book

def delete_book(book_id):
    book = Book.query.get(book_id)
    book.deleted = True
    db.Session.commit()
    return book

def get_notes(book_id):
    book = Book.query.get(book_id)
    notes = book.notes
    return notes

def edit_note(book_id, json):
    book = book_id
    book.notes = json

def delete_note(book_id):
    #soft delete?
    return

def get_collections(book_id):
    book = Book.query.getall()
    collections = book.collections
    return collections