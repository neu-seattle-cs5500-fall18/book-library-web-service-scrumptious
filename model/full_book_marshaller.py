from model import author_checker
from model import book_checker
from model.book import authorship


class FullBook:
    def __init__(self, title, publish_date, subject, genre, book_note, authors):
        self.title = title
        self.publish_date = publish_date
        self.subject = subject
        self.genre = genre
        self.book_note = book_note
        self.authors = authors


# return full_book object back for books_api?
def create_full_book(book_json, author_json):
    title = book_json['title']
    pub_date = book_json['publish_date']
    subj = book_json['subject']
    genre = book_json['genre']
    note = book_json['note']
    # can a list of authors be passed in as json?
    authors = author_json['']
    full_book = FullBook(title, pub_date, subj, genre, note, authors)
    return full_book

