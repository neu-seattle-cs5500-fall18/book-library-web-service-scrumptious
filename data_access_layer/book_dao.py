from model import db
from model.book import Book, authorship_table
from model.author import Author


#make sure query handles wildcard
#make sure authors can be added if existing
#update publish datae.

class BookDao:
    @staticmethod
    def contains(book_id):
        """
        Method to determine if Books contains a given book_id.
        :param book_id: Record of book to search for.
        :return: True if present, false otherwise.
        """
        if Book.query.get(book_id) is None:
            return False
        else:
            return True

    @staticmethod
    def create_list_dict(book_query):
        """
        Method to create a list of book dictionaries given a query object. Used internally to BookDao only.
        :param book_query: results of Session.query(query parameters)
        :return: a List of book dictionaries.
        """
        new_list = []
        for book in book_query:
            new_list.append(book.to_dict())
        return new_list

    @staticmethod
    def get(book_id):
        """
        Method to retrieve a book by book_id
        :param book_id: Record id of a book.
        :return: a Dictionary of the queried book.
        """
        a_book = Book.query.get(book_id)
        return a_book.to_dict()

    @staticmethod
    def get_all():
        results = Book.query.all()
        return results

    @staticmethod
    def query_books(query_params_dict):
        """
        Method to query books by a dictionary of given query arguments. If all query arguments are none, then all book
        records are returned.
        :param query_params_dict: Query arguments to filter by.  Limited to those of the books_api query_parser.
        :return: a List of book dictionaries based on query arguments.
        """
        print("book_dao.query_books()")

        results = db.session.query(Book)

        if query_params_dict['publish_date_start'] is not None:
            start = query_params_dict['publish_date_start']
            results = results.filter(Book.publish_date >= start)
        if query_params_dict['publish_date_end'] is not None:
            end = query_params_dict['publish_date_end']
            results.filter(Book.publish_date <= end)
        if query_params_dict['title'] is not None:
            title = query_params_dict['title']
            results = results.filter(Book.title.contains(title))
        if query_params_dict['subject'] is not None:
            subject = query_params_dict['subject']
            results = results.filter(Book.subject.contains(subject))
        if query_params_dict['genre'] is not None:
            genre = query_params_dict['genre']
            results = results.filter(Book.genre.contains(genre))

        results.join(authorship_table).join(Author)

        if query_params_dict['first_name'] is not None:
            first = query_params_dict['first_name']
            results = results.filter(Author.first_name.contains(first))
        if query_params_dict['middle_name'] is not None:
            middle = query_params_dict['middle_name']
            results = results.filter(Author.middle_name.contains(middle))
        if query_params_dict['last_name'] is not None:
            last = query_params_dict['last_name']
            results = results.filter(Author.last_name.contains(last))

        results.all()

        print("book_dao.create() ==> Complete")
        return BookDao.create_list_dict(results)

    @staticmethod
    def create(book_dict):
        """
        Method to create a new Book record given a book dictionary. Does NOT create associated Author or BookCopy
        records.
        :param book_dict: dictionary of book values for a new record.
        :return: a dictionary object of the created book.
        """
        print("BookDao.create()")
        from dateutil import parser
        new_book = Book(**book_dict)
        new_book.publish_date = parser.parse(new_book.publish_date)
        db.session.add(new_book)
        db.session.commit()
        print("book_dao.create() ==> Complete")
        return new_book.to_dict()

    @staticmethod
    def update(book_id, **kwargs):
        """
        Method to update a book record by book_id and provided attribute arguments.
        :param book_id: the ID of the book to update.
        :param kwargs: Key value pairs of the book attributes to be updated.
        :return: a dictionary of the updated book.
        """
        print('BookDao.update()')
        book = Book.query.get(book_id)
        book.update(**kwargs)
        db.session.commit()
        return book.to_dict()

    @staticmethod
    def delete(a_book_id):
        """
        Method to delete a book record.  Has cascading effect on copies and authors.
        :param a_book_id: id of book record to be deleted.
        :return: null.
        """
        b = Book.query.filter_by(book_id=a_book_id).first()
        b.authors = []
        db.session.commit()
        db.session.delete(b)
        db.session.commit()
        return None




