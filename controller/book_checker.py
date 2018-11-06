from data_access_layer import book_dao
from controller import author_checker
from flask_restplus import abort

# functions that interact with a books record.


def valid_input(book_dict):
    # Assumes subject and genre are required inputs
    return None not in book_dict['title'] and None not in book_dict['publish_date'] and None not in book_dict['subject']


# gets dict of query params, returns a list of book dicts.
def clean_book(book_dict):
    book_dict['title'] = book_dict.title.lower().title()
    # how do we want to store publish date???
    book_dict['subject'] = book_dict.subject.lower().title()
    book_dict['genre'] = book_dict.genre.lower().title()

    return book_dict



def get_books(**query_params):

    list_books = []
    results = book_dao.query_books(**query_params)
    for book in results:
        list_books.append(book.to_dict())
    return list_books


def create_book(book_json):
    print("book_checker.create_book()")
    title = book_json['title']
    publish_date = book_json['publish_date']
    subject = book_json['subject']
    genre = book_json['genre']
    book_note = book_json['book_note']
    authors = book_json['authors']
    a_book = {'title': title, 'publish_date': publish_date, 'subject': subject, 'genre': genre, 'book_note': book_note}

    if valid_input(a_book):
        a_book = clean_book(a_book)
    else:
        abort(400, 'Invalid input')
    # author_checker validates input
    authors = author_checker.create_authors(authors)
    new_book = book_dao.create(a_book, authors)

    print("book_checker.create_book() ==> Complete")
    print(new_book)
    return new_book.to_dict()


def get_book(book_id):

    if book_id.isdigit():
        book = book_dao.query_book_id(book_id)
        return book.to_dict()
    else:
        abort(400, 'Invalid input for book_id')


def update_book(book_id, book_json):
    if book_id.isdigit():
        book_dao.update(book_id, **book_json)
    else:
        abort(400, 'invalid input for book_id')


def delete_book(book_id):
    return
    #delete all instances of book
    #how to update authorship?
    #how to update collections?
    # how to update instances?


def get_note(book_id):
    if book_id.isdigit():
        note = book_dao.get_note(book_id)
        return {'note': note}
    else:
        abort(400, 'Invalid input for book_id')



def create_note(book_id, note):
    if book_id.isdigit():
        id = book_dao.add_note(book_id, note)
        return {'note':note}


def update_note(book_id, note):
    if book_id.isdigit():
        note = book_dao.edit_note(book_id, note)
        return {'note': note}
    else:
        abort(400, 'Invalid input for book_id')


def delete_note(book_id):
    if book_id.isdigit():
        id = book_dao.delete_note(book_id)
        return id
    else:
        abort(400, 'Invalid input for book_id')


## functions that handle copies of books.

def get_copies(book_id):
    copies = book_dao.query_copies(book_id)
    return copies


def delete_book_copy(book_id, book_copy_id):

    return