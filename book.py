from flask import Flask


# Book class
class Book:
    def __init__(self, book_id, author_first, author_last, title, publish_date, genre, subject, loaned, due_date):
        self.book_id = book_id
        self.author_first = author_first
        self.author_last = author_last
        self.title = title
        self.publish_date = publish_date
        self.genre = genre
        self.subject = subject
        self.loaned = loaned
        self.due_date = due_date

