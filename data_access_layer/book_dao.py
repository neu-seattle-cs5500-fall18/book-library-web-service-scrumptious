from library_webservice import db
from data_access_layer import author_dao, book_copy_dao
from model.book import Book, authorship_table
from model.author import Author


def contains(book_id):
    """
    Function to determine if Books contains a given book_id.
    :param book_id: Record of book to search for.
    :return: True if present, false otherwise.
    """
    if Book.query.get(book_id) is None:
        return False
    else:
        return True


def create_list_dict(book_query):
    """
    Function to create a list of book dictionaries given a query object.
    :param book_query: results of Session.query(query parameters)
    :return: a List of book dictionaries.
    """
    new_list = []
    for book in book_query:
        new_list.append(book.to_dict())
    return new_list


def get(book_id):
    """
    Function to retrieve a book by book_id
    :param book_id: Record id of a book.
    :return: a Dictionary of the queried book.
    """
    a_book = Book.query.get(book_id)
    return a_book.to_dict()


def query_books(query_params_dict):
    """
    Function to query books by a dictionary of given query arguments.
    :param query_params_dict: Query arguments to filter by.
    :return: a List of book dictionaries based on query arguments.
    """
    print("book_dao.query_books()")

    results = db.session.query(Book).join(authorship_table).join(Author)

    if query_params_dict['first_name'] is not None:
        first = query_params_dict['first_name']
        results = results.filter(Author.first_name == first)
    if query_params_dict['middle_name'] is not None:
        middle = query_params_dict['middle_name']
        results = results.filter(Author.middle_name == middle)
    if query_params_dict['last_name'] is not None:
        last = query_params_dict['last_name']
        results = results.filter(Author.last_name==last)
    if query_params_dict['publish_date_start'] is not None:
        start = query_params_dict['publish_date_start']
        results = results.filter(Book.publish_date > start)
    if query_params_dict['publish_date_end'] is not None:
        end = query_params_dict['publish_date_end']
        results.filter(Book.publish_date < end)
    if query_params_dict['title'] is not None:
        title = query_params_dict['title']
        results = results.filter(Book.title == title)
    if query_params_dict['subject'] is not None:
        subject = query_params_dict['subject']
        results = results.filter(Book.subject == subject)
    if query_params_dict['genre'] is not None:
        genre = query_params_dict['genre']
        results = results.filter(Book.genre == genre)

    results.all()

    print("book_dao.create() ==> Complete")
    return create_list_dict(results)



def create(book_dict, list_authors):
    """
    Function to create a new Book record given a book dictionary and list of book author dictionaries.  Cascades to
    create a copies and creates new authors with foreign key references to the book_id
    :param book_dict: dictionary of book values for a new record.
    :param list_authors: list of dictionaries of author values for new author records.
    :return: a dictionary object of the created book.
    """
    print("book_dao.create()")
    new_book = Book(**book_dict)
    db.session.add(new_book)
    db.session.commit()
    author_dao.create(new_book, list_authors)
    book_copy_dao.create(new_book)
    print("book_dao.create() ==> Complete")
    return new_book.to_dict()


##Be Careful with this.
def update(book_id, **kwargs):
    """
    Function to update a book by book_id and provided attribute arguments
    :param book_id: the ID of the book to update.
    :param kwargs: Key value pairs of the book attributes to be updated.
    :return: a dictionary of the updated book.
    """
    book = Book.query.get(book_id).join(authorship_table).join(Author)
    book.update(**kwargs)
    db.session.commit()
    return book.to_dict()


def delete(book_id):
    """
    Function to delete a book record.  Has cascading effect on copies and authors.
    :param book_id: id of book record to be deleted.
    :return:
    """
    a_book = Book.query.get(book_id)

    Book.query.filter_by(book_id=book_id).delete()
    db.session.commit()
    return "Success"




