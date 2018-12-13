from controller.note_checker import NoteChecker
from data_access_layer.book_dao import BookDao
from controller.author_checker import AuthorChecker
from controller.book_copy_checker import BookCopyChecker
from flask_restplus import abort


class BookChecker:
    @staticmethod
    def valid_input(book_dict):
        """
        Function to check if a book object is being create with the right params.
        :param book_dict: Dictionary of a book.
        :return: boolean: True or False.
        """
        return None not in book_dict['title'] and None not in book_dict['publish_date'] and \
               None not in book_dict['subject']

    @staticmethod
    def clean_book(book_dict):
        """
        Function that converts all properties of a book into desirable properties.
        :param book_dict: Old Dictionary of a book.
        :return: New Dictionary of a book.
        """
        book_dict['title'] = book_dict.title.lower().title()
        book_dict['subject'] = book_dict.subject.lower().title()
        book_dict['genre'] = book_dict.genre.lower().title()
        title = book_dict['title'].lower().title()
        subject = book_dict['subject'].lower().title()
        genre = book_dict['genre'].lower().title()
        book_dict['title'] = title
        book_dict['subject'] = subject
        book_dict['genre'] = genre

        return book_dict

    @staticmethod
    def create_book(book_json):
        """
        Creates a book from Json object.
        :param book_json: Json book object.
        :return: A new book.
        """
        print("book_checker.create_book()")
        title = book_json['title']
        publish_date = book_json['publish_date']
        subject = book_json['subject']
        genre = book_json['genre']
        notes = book_json['notes']
        authors = book_json['authors']

        a_book = {'title': title, 'publish_date': publish_date, 'subject': subject, 'genre': genre}

        if BookDao.contains_by_params(a_book):
            abort(400, 'Book already exists')
        else:
            new_book = BookDao.create(a_book)
            book_copy = BookCopyChecker.create_copy(new_book['book_id'])
            created_notes = NoteChecker.create_notes(new_book['book_id'], notes)
            new_authors = AuthorChecker.create_authors(new_book['book_id'], authors)

            print("book_checker.create_book() ==> Complete")
            return BookDao.get(new_book['book_id'])

    @staticmethod
    def get_book(book_id):
        """
        Gets a book.
        :param book_id: Book ID.
        :return: The book.
        """
        if BookDao.contains(book_id):
            a_book = BookDao.get(book_id)
            return a_book
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def get_books(dict_query_params):
        """
        Gets multiple books.
        :param dict_query_params: Dictionary params for these books.
        :return: list of these queried books.
        """
        print('get books')
        list_books = BookDao.query_books(dict_query_params)
        return list_books

    @staticmethod
    def update_book(book_id, book_json):
        """
        Updates a books information.
        :param book_id: ID of the book that needs to be updated.
        :param book_json: Book Json object.
        :return: Updated book.
        """
        print('BookChecker.update_book()')

        if BookDao.contains(book_id):
            a_book = BookDao.update(book_id, **book_json)
            return a_book
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def delete_book(book_id):
        """
        Deletes a book.
        :param book_id: ID of the book that needs to be deleted.
        :return: an operation for BookDAO to delete the book.
        """
        if BookDao.contains(book_id):

            return BookDao.delete(book_id)
        else:
            abort(404, 'Resource not found: book_id')
