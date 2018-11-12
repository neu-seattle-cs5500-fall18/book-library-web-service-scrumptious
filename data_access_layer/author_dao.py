from library_webservice import db
from model.author import Author
from model.book import Book


class AuthorDao:

    @staticmethod
    def contains(author_id):
        print('AuthorDao.contains()')
        an_author = Author.query.get(author_id)
        if an_author is None:
            return False
        else:
            return True

    @staticmethod
    def get_author(author_id):
        print("AuthorDao.get_author()")
        author = Author.query.get(author_id)
        return author.to_dict()

    @staticmethod
    def create(book_id, author_dict):
        print("AuthorDao.create()")
        book = Book.query.get(book_id)
        new_author = Author(**author_dict)
        new_author.books.append(book)
        db.session.add(new_author)
        db.session.commit()
        print("author_dao.create() ==> Complete")
        return new_author.to_dict()

    @staticmethod
    def add_book(book_id, author_id):
        print("AuthorDao.add_book()")
        book = Book.query.get(book_id)
        existing_author = Author.query.get(author_id)
        existing_author.books.append(book)
        db.session.commit()
        return existing_author.to_dict()

    @staticmethod
    def update(author_id, **kwargs):
        author = Author.query.get(author_id)
        author.update(**kwargs)
        db.session.commit()
        return author.to_dict()

    @staticmethod
    def delete(author_id):
        db.session.get(author_id).delete()
        db.session.commit()
        return None
