from model import db
from model.author import Author
from model.book import Book


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
    def contains_author(author_dict):
        """
        Method to determine if an author exists based on parameters
        :param author_json: json of Author parameters and values (first_name, last_name, middle_name)
        :return: True if database contains a record that matches, false otherwise.
        """
        print('AuthorDao.contains_author()')
        results = Author.query.filter_by(first_name=author_dict['first_name'], last_name=author_dict['last_name'], middle_name=author_dict['middle_name']).first()
        print(results)
        if results is None:
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
    def get_author_ID(author_dict):
        """
        Method to get the ID of an author based on the author's information. Requires exact match of fields
        :param author_dict: Dictionary of author information to filter by.
        :return: the ID of an author if present.  None otherwise.
        """
        results = Author.query.filter_by(**author_dict).first()
        return results.author_id

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

        db.session.add(new_author)
        db.session.commit()
        print(new_author)
        new_author.books.append(book)
        db.session.commit()
        print(new_author)
        print("author_dao.create() ==> Complete")
        return new_author.to_dict()

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
        print('AuthorDao.update()')
        author = Author.query.get(author_id)
        author.update(**kwargs)
        db.session.commit()
        return author.to_dict()


