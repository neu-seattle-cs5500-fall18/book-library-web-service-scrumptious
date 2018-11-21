from model import db
from model.author import Author
from model.book import Book
from flask_restplus import abort


class AuthorDao:

    @staticmethod
    def contains(author_id):
        """
        Method to determine if an author exists.
        :param author_id: Record of an Author.
        :return: True if Author is present, false otherwise.
        """
        print('AuthorDao.contains()')
        an_author = Author.query.get(author_id)
        if an_author is None:
            return False
        else:
            return True

    @staticmethod
    def get_author(author_id):
        """
        Method to get an Author based on id.
        :param author_id: Record of an existing Author.
        :return: Dictionary of Author.
        """
        print("AuthorDao.get_author()")
        author = Author.query.get(author_id)
        return author.to_dict()

    @staticmethod
    def create(book_id, author_dict):
        """
        Method to create an Author based on dictionary of author attributes and an existing Book_id.
        :param book_id: Record of Book to add new Author to.
        :param author_dict: Dictionary of Author attributes to create a new Author.
        :return: Dictionary of created Author.
        """
        print("AuthorDao.create()")
        book = Book.query.get(book_id)
        new_author = Author(**author_dict)
        if new_author.valid_input(new_author.first_name, new_author.last_name, new_author.middle_name):
            db.session.add(new_author)
            db.session.commit()
            print(new_author)
            new_author.books.append(book)
            db.session.commit()
            print(new_author)
            print("author_dao.create() ==> Complete")
            return new_author.to_dict()
        else:
            abort(400)

    @staticmethod
    def add_book(book_id, author_id):
        """
        Method to add a Book to an Author.
        :param book_id: Record of Book
        :param author_id: Record of Author
        :return: Dictionary of Author.
        """
        print("AuthorDao.add_book()")
        book = Book.query.get(book_id)
        existing_author = Author.query.get(author_id)
        existing_author.books.append(book)
        db.session.commit()
        return existing_author.to_dict()

    @staticmethod
    def update(author_id, **kwargs):
        """
        Method to update an Author record.
        :param author_id: Record of an Author.
        :param kwargs: Author attributes to be updated.
        :return: Dictionary of updated Author.
        """
        author = Author.query.get(author_id)
        author.update(**kwargs)
        db.session.commit()
        return author.to_dict()

    @staticmethod
    def delete(author_id):
        """
        Method to delete an Author.
        :param author_id: Record of Author.
        :return: Null.
        """
        db.session.get(author_id).delete()
        db.session.commit()
        return None
