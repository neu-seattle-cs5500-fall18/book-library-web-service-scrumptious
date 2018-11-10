from library_webservice import db
from data_access_layer import author_dao, book_copy_dao
from model.book import Book


def create_list_dict(book_query):
    new_list = []
    for book in book_query:
        new_list.append(book.to_dict())
    return new_list


def query_book_id(book_id):
    a_book = Book.query.get(book_id)
    return a_book.all()


def query_books(book_dict):
    """
    Queries all books in library
    :return: List of Book
    """
    print("book_dao.query_books()")

    query_results = Book.query
    #
    # if book_dict['AuthorName'] is not None:
    #     author_name = book_dict['AuthorName']
    #     query_results.filter_by(author_name=author_name)
    if book_dict['publish_date_start'] is not None:
        start = book_dict['publish_date_start']
        query_results.filter_by(Book.publish_date > start)
    if book_dict['publish_date_end'] is not None:
        end = book_dict['publish_date_end']
        query_results.filter(Book.publish_date < end)
    if book_dict['title'] is not None:
        title = book_dict['title']
        query_results.filter_by(title=title)
    if book_dict['subject'] is not None:
        subject = book_dict['subject']
        query_results.filter_by(subject=subject)
    if book_dict['genre'] is not None:
        genre = book_dict['genre']
        query_results.filter_by(genre=genre)

    query_results.all()

    print("book_dao.create() ==> Complete")
    return create_list_dict(query_results)



def create(book_dict, list_authors):
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
    book = Book.query.get(book_id)
    book.update(**kwargs)
    db.session.commit()
    return book.to_dict()


# Notes actions
def get_note(book_id):
    book = Book.query_by_id(book_id)
    note = book.note
    return note


def edit_note(book_id, note):
    book = Book.query_by_id(book_id)
    book.notes = note
    db.session.commit()
    return book


def delete_note(book_id):
    book = Book.query_by_id(book_id)
    book.notes = 'None'
    db.session.commit()
    return book


def delete(book_id):
    book = Book.query.get(book_id)
    book.deleted = True
    db.session.commit()
    return book.to_dict()

