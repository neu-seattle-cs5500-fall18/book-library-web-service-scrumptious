from data_access_layer.author_dao import AuthorDao
from data_access_layer.book_dao import BookDao
from flask_restplus import abort


class AuthorChecker:

    @staticmethod
    def json_to_dict(author_json):
        """
        Helper method to create dictionary of author parameters from json object.
        :param author_json: Json object.
        :return: Dictionary of an author.
        """
        author = {
            'first_name': author_json['first_name'],
            'last_name': author_json['last_name'],
            'middle_name': author_json['middle_name']
        }
        return author

    @staticmethod
    def add_book_to_author(book_id, author_id):
        """
        Method to add an existing book to an existing author.
        :param book_id: id of existing book.
        :param author_id: id of existing author.
        :return: dictionary of updated author object.
        """
        if BookDao.contains(book_id):
            if AuthorDao.contains(author_id):
                author_dict = AuthorDao.add_book(book_id, author_id)
                return author_dict
            else:
                abort(404, 'Resource not found: author_id')
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def create_author(book_id, author_json):
        """
        Method to create a new author and attribute a book to author.  If author record already exists, book is added.
        to existing author record.
        :param book_id:  id of existing book.
        :param author_json: json of author information.
        :return: dictionary of created author.
        """
        print('author_checker.create_author()')
        if BookDao.contains(book_id):
            author_dict = AuthorChecker.json_to_dict(author_json)
            if AuthorDao.contains_author(author_dict):
                author_id = AuthorDao.get_author_ID(author_dict)
                results = AuthorChecker.add_book_to_author(book_id, author_id)
                return results
            else:
                an_author = AuthorDao.create(book_id, author_dict)
                return an_author
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def create_authors(book_id, list_authors):
        """
        Method to generate a list of authors. Depends on create_author() to create the correct author record.
        :param book_id: record of book to add to authors.
        :param list_authors: json list of authors to be created and book added to.
        :return: list of dictionary of created authors.
        """
        print('author_checker.create_authors()')
        list_new_authors = []

        if BookDao.contains(book_id):

            for author in list_authors:
                an_author = AuthorChecker.create_author(book_id, author)
                list_new_authors.append(an_author)
            return list_new_authors
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def get_author(author_id):
        """
        Method to get a specific author record based on author_id.
        :param author_id: Record of Author to get.
        :return: Dictionary of author.
        """
        print('Get author %r' % author_id)
        if AuthorDao.contains(author_id):
            an_author = AuthorDao.get_author(author_id)
            return an_author
        else:
            abort(404, 'Resource not found: author_id')

    @staticmethod
    def update_author(book_id, author_id, json_author_info):
        """
        Method to update an author record.
        :param book_id: record of a book.
        :param author_id: record of author.
        :param json_author_info: json of author information to be updated.
        :return: dictionary of updated author record.
        """
        if BookDao.contains(book_id):
            if AuthorDao.contains(author_id):
                author = AuthorChecker.json_to_dict(json_author_info)
                return AuthorDao.update(author_id, **author)
            else:
                abort(404, 'Resource not found: author_id')
        else:
            abort(404, 'Resource not found: author_id')

