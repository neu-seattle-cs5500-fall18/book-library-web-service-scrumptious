from flask import abort
from library_webservice import db
from model.author import Author


def get_author(author_id):
    #this gets an author by its record number
    author = Author.query.get(author_id)

    if author is None:
        abort(400, 'Invalid input')
    else:
        return author


def get_author(**query_args):
    #this gets an author based on query parameters, in the form of a dict, returns a list of author dicts
    list_of_authors = []
    query_results = Author.query.filter_by(**query_args)

    for author in query_results:
        list_of_authors.append(author.to_dict())

    return list_of_authors


def create_author(**author_dict):
    #Creates a new author, returns id
    #need to check for author existing already.
    author = Author(**author_dict)
    db.session.add(author)
    db.session.commit()
    return author.author_id


def update_author(author_id, **author_dict):
    #updates an existing author by id and dict arguments
    author = Author.query.get(author_id)
    if author is None:
        abort(400, 'No such author id')
    else:
        for key, value in author_dict:
            author.key = value
        return author.author_id

