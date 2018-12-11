from model import db
from model.book_copy import BookCopy


class BookCopyDao:
    @staticmethod
    def contains(book_copy_id):
        """
        Method to determine if a BookCopy of a Book exists.
        :param book_copy_id: Record of a BookCopy.
        :return: True if record exists, false otherwise.
        """
        if BookCopy.query.get(book_copy_id) is None:
            return False
        else:
            return True

    @staticmethod
    def create(book_id):
        """
        Method to create a BookCopy of a Book given a valid book_id of an existing book record.
        :param book_id: Record of a book.
        :return: Dictionary of created BookCopy.
        """
        print("book_copy_dao.create()")
        book_copy = BookCopy(book_id=book_id)
        db.session.add(book_copy)
        db.session.commit()
        print("book_copy_dao.create() ==> Complete")
        return book_copy.to_dict()

    @staticmethod
    def get_next_available(book_id):
        """
        Method to retrieve the next copy of a book that is not checked out.
        :param book_id: record of book to get a copy of
        :return: dictionary of next copy where is_checked_out is false.  None otherwise.
        """
        print('get_next_avaiable')    
        results = BookCopy.query.filter(BookCopy.book_id == book_id);
        copy = results.filter(BookCopy.is_checked_out is False).first()
        if copy is None:
            return None
        else:
            return copy.to_dict()

    @staticmethod
    def get_book_copy(book_copy_id):
        """
        Method to retrieve a BookCopy.
        :param book_copy_id: Record of a BookCopy
        :return: Dictionary of BookCopy
        """
        book_copy = BookCopy.query.get(book_copy_id)
        return book_copy

    @staticmethod
    def get_book_copies(book_id):
        """
        Method to get all BookCopies of a Book
        :param book_id: Record of Book
        :return: List of Dictionaries of BookCopies
        """
        print('BookCopyDao.get_book_copies()')
        list_of_copies = []
        db_results = BookCopy.query.filter(BookCopy.book_id == book_id).all()

        for book in db_results:
            list_of_copies.append(book.to_dict())

        print(list_of_copies)
        return list_of_copies

    @staticmethod
    def delete_copy(copy_id):
        """
        Method to delete a BookCopy from a Book.
        :param copy_id: Record of a BookCopy to delete.
        :return: Null.
        """
        BookCopy.get(copy_id).delete()
        db.session.commit()
        return None

