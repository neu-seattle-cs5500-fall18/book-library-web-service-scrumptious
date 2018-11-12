from data_access_layer.author_dao import AuthorDao
from data_access_layer.book_dao import BookDao
from flask_restplus import abort
import re


pattern = re.compile('\A(\w\.)+')

class AuthorChecker:
    @staticmethod
    #Move this to the marshaller?
    def valid_input(first_name, last_name, middle_name):
        print("author_checker.valid_input()")
        return (first_name is None or first_name.isalpha() or pattern.match(first_name)) and \
               (middle_name is None or middle_name.isalpha() or pattern.match(middle_name)) and \
               (last_name.isalpha() or pattern.match(last_name))

    @staticmethod
    def clean_author(first_name, last_name, middle_name):
        print('author_checker.clean_author')

        if first_name is not None:
            first_name = first_name.lower().title()

        if middle_name is not None:
            if len(middle_name) == 1 and middle_name.isalpha():
                middle_name.append(".")
            elif pattern.match(middle_name):
                middle_name = middle_name[0].upper() + '.'
            else:
                middle_name.lower().title()

        formatted_author = {
            'first_name': first_name.lower().title(),
            'last_name': last_name,
            'middle_name': middle_name
        }
        print(formatted_author)
        return formatted_author


    @staticmethod
    def add_new_author(book_id, author_json):
        an_author = AuthorChecker.clean_author(author_json)

        if BookDao.contains(book_id):
            AuthorDao.create(book_id, an_author)
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
            an_author = AuthorChecker.clean_author(author_json['first_name'], author_json['last_name'], author_json['middle_name'])
            an_author = AuthorDao.create(book_id, an_author)
            return an_author
        else:
            abort(404)

    @staticmethod
    def create_authors(book_id, list_authors):
        print('author_checker.create_authors()')

        if BookDao.contains(book_id):
            list_new_authors = []

            for author in list_authors:
                an_author = AuthorChecker.clean_author(author['first_name'], author['last_name'],author['middle_name'])
                list_authors.append(AuthorDao.create(book_id, an_author))
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