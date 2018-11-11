from flask import abort
from library_webservice import db
from model.book_copy import BookCopy


def create(a_book):
    print("book_copy_dao.create()")
    book_copy = BookCopy(book_id=a_book.book_id)
    db.session.add(book_copy)
    db.session.commit()
    print("book_copy_dao.create() ==> Complete")
    return book_copy.to_dict()


def get_book_copy(book_copy_id):
    book_copy = BookCopy.query.get(book_copy_id)
    return book_copy.to_dict


def get_book_copies(book_id):
    list_of_copies = []
    db_results = BookCopy.query.filter(BookCopy.book_id == book_id)
    db_results.all()
    for book in db_results:
        list_of_copies.append(book.to_dict())

    return list_of_copies


def delete_copy(copy_id):
    BookCopy.get(copy_id).delete()
    db.session.commit()
    return


# def insert_book_copy(book_id):
#     copy = BookCopy(book_id)
#     db.session.add(copy)
#     db.session.commit()
#     return copy.book_copy_id


# def delete_book_copy(book_copy_id):
#     copy = BookCopy.query.get(book_copy_id)
#     copy.is_deleted = True
#     return copy.book_copy_id


