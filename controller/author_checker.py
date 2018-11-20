from data_access_layer.author_dao import AuthorDao
from data_access_layer.book_dao import BookDao
from flask_restplus import abort
import re


#pattern = re.compile('\A(\w\.)+')


class AuthorChecker:

    @staticmethod
    def add_new_author(book_id, author_json):
        # an_author = AuthorChecker.clean_author(author_json)

        if BookDao.contains(book_id):
            # AuthorDao.create(book_id, an_author)
            AuthorDao.create(book_id, author_json)
        else:
            abort(400)

    @staticmethod
    def add_book_to_author(book_id, author_id):

        if BookDao.contains(book_id) and AuthorDao.contains(author_id):
            AuthorDao.add_book(book_id, author_id)
        else:
            abort(400)

    @staticmethod
    def create_author(book_id, author_json):
        print('author_checker.create_author()')
        if BookDao.contains(book_id):
            # an_author = AuthorChecker.clean_author(author_json['first_name'], author_json['last_name'], author_json['middle_name'])
            # an_author = AuthorDao.create(book_id, an_author)
            an_author = AuthorDao.create(book_id, author_json)
            return an_author
        else:
            abort(404)

    @staticmethod
    def create_authors(book_id, list_authors):
        print('author_checker.create_authors()')
        list_new_authors = []

        if BookDao.contains(book_id):

            for author in list_authors:
                print(author)
                # an_author = AuthorChecker.clean_author(author['first_name',author['last_name'], author['middle_name']])
                an_author = AuthorDao.create(book_id, author)
                list_new_authors.append(an_author)
            return list_new_authors
        else:
            abort(404)

    @staticmethod
    def get_author(author_id):
        """
        Method to get a specific author record based on author_id.
        :param author_id: Record of Author to get.
        :return: Json of an Author Dict
        """
        print('Get author %r' % author_id)
        if AuthorDao.contains(author_id):
            an_author = AuthorDao.get_author(author_id)
            return an_author
        else:
            abort(404)

    @staticmethod
    def update_author(author_id, json_author_info):

        if AuthorDao.contains(author_id):
            f_name = json_author_info['first_name']
            l_name = json_author_info['last_name']
            m_name = json_author_info['middle_name']

            if AuthorChecker.valid_input(f_name, l_name, m_name):
                author = AuthorChecker.clean_author(f_name, l_name, m_name)
                return AuthorChecker.update_author(author_id, author)
            else:
                abort(400, 'Invalid input')
        else:
            abort(404)

    @staticmethod
    def delete_author_from_book(book_id, author_id):
        if BookDao.contains(book_id) and BookDao.contains(author_id):
            return None
