from flask import abort
from data_access_layer.book_copy_dao import BookCopyDao
from data_access_layer.book_dao import BookDao


class BookCopyChecker:
    @staticmethod
    def create_copy(book_id):
        """
        Method to create a new copy for a book.
        :param book_id: Book record to create a copy for.
        :return: Dictionary of created Copy.
        """
        print('BookCopyChecker.create_copy()')
        if BookDao.contains(book_id):
            return BookCopyDao.create(book_id)
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def get_copy(book_copy_id):
        """
        Method to get a copy of a book by copy id.
        :param book_copy_id: Integer of record for a copy.
        :return: Dictionary of book copy.
        """
        if BookCopyDao.contains(book_copy_id):
            return BookCopyDao.get_book_copy(book_copy_id)
        else:
            abort(404, 'Resource not found: book_copy_id')

    @staticmethod
    def get_copies(book_id):
        """
        Method to get all copies of a book.
        :param book_id: Integer record of a book.
        :return: List of dictionaries of copies.
        """
        if BookDao.contains(book_id):
            return BookCopyDao.get_book_copies(book_id)
        else:
            abort(404, 'Resource not found: book_id')



