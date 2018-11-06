from flask import abort
from library_webservice import db
from model.author import Author


def get_author(author_id):
    #this gets an author by its record number
    author = Author.query.get(author_id)
    if author is None:
        abort(400, 'Invalid input')
    else:
        return author.to_dict()


def get_author(**kwargs):
    #this gets an author based on query parameters, in the form of a dict,
    # returns a list of author dicts
    list_of_authors = []
    query_results = Author.query.filter_by(**kwargs)

    for author in kwargs:
        list_of_authors.append(author.to_dict())
    return list_of_authors


def create_authors(book, list_authors):

    for author in list_authors:
        record = Author(**author)
        db.session.add(record)
        db.session.commit()
        record.books.append(book)
        db.session.commit()
    return book.authors


def update_author(author_id, **kwargs):
    #updates an existing author by id and dict arguments, returns dict
    author = Author.query.get(author_id)
    if author is None:
        abort(400, 'No such author id')
    else:
        for key, value in kwargs:
            author[key] = value
        db.session.commit(author)
        return author.to_dict()

