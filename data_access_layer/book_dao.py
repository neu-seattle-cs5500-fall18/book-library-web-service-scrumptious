from library_webservice import db
from data_access_layer import author_dao, book_copy_dao
from model.book import Book, authorship_table
from model.author import Author


def create_list_dict(book_query):
    new_list = []
    for book in book_query:
        new_list.append(book.to_dict())
    return new_list


def query_book_id(book_id):
    a_book = Book.query.get(book_id)
    return a_book.all()

#this needs to be able to handle multidict
def query_books(book_dict):
    """
    Queries all books in library
    :return: List of Book
    """
    print("book_dao.query_books()")

    results = db.session.query(Book).join(authorship_table).join(Author)

    if book_dict['first_name'] is not None:
        first = book_dict['first_name']
        results = results.filter(Author.first_name==first)
    if book_dict['middle_name'] is not None:
        middle = book_dict['middle_name']
        results = results.filter(Author.middle_name == middle)
    if book_dict['last_name'] is not None:
        last = book_dict['last_name']
        results = results.filter(Author.last_name==last)

    if book_dict['publish_date_start'] is not None:
        start = book_dict['publish_date_start']
        results = results.filter(Book.publish_date > start)

    if book_dict['publish_date_end'] is not None:
        end = book_dict['publish_date_end']
        results.filter(Book.publish_date < end)

    if book_dict['title'] is not None:
        title = book_dict['title']
        results = results.filter(Book.title==title)

    if book_dict['subject'] is not None:
        subject = book_dict['subject']
        results = results.filter(Book.subject==subject)

    if book_dict['genre'] is not None:
        genre = book_dict['genre']
        results = results.filter(Book.genre==genre)

    results.all()

    print("book_dao.create() ==> Complete")
    return create_list_dict(results)



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

