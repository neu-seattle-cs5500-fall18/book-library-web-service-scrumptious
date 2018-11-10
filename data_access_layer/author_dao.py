from flask import abort
from library_webservice import db
from model.author import Author


def get_author(author_id):
    author = Author.query.get(author_id)
    author.all()
    return author.to_dict()


def get_authors(args):
    #this gets an author based on query parameters, in the form of a dict,
    # returns a list of author dicts
    list_of_authors = []
    query_results = Author.query.get_all()

    if args['first_name']:
        first_name = args['first_name']
        query_results.filter_by(first_name = first_name)
    if args['last_name']:
        last_name = args['last_name']
        query_results.filter_by(last_name=last_name)
    if args['middle_name']:
        middle_name = args['middle_name']
        query_results.filter_by(middle_name=middle_name)

    query_results.all()

    for author in query_results:
        list_of_authors.append(author.to_dict())
    return list_of_authors

def author_exists(author_dict):
    print("author_dao.author_exists()")
    record = Author.query.filter_by(first_name=author_dict['first_name'], last_name=author_dict['last_name'],
                                    middle_name=author_dict['middle_name'])
    return record is None


def create(book, list_author):
    print("author_dao.create()")

    for author in list_author:
        if author_exists(author):
            print("here")
            existing_record = Author.query.filter_by(**author)
            existing_record.books.append(book)
            print("appended book to existing author")
        else:
            print("or here")
            new_author = Author(**author)
            new_author.books.append(book)
            db.session.add(new_author)
            print("added new author")
    db.session.commit()
    print("author_dao.create() ==> Complete")


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

