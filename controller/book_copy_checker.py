from flask import abort
from data_access_layer.book_copy_dao import BookCopyDao
from data_access_layer.book_dao import BookDao


class BookCopyChecker:
    @staticmethod
    def create_copy(book_id):
        return BookCopyDao.create(book_id)

    @staticmethod
    def get_copy(book_copy_id):
        if BookCopyDao.contains(book_copy_id):
            return BookCopyDao.get_book_copy(book_copy_id)
        else:
            abort(404)

    @staticmethod
    def get_copies(book_id):
        if BookDao.contains(book_id):
            return BookCopyDao.get_book_copies(book_id)
        else:
            abort(404)



