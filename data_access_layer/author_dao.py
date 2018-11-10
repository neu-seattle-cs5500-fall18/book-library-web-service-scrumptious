from flask import abort
from library_webservice import db
from model.author import Author


def get_author(author_id):
    author = Author.query.get(author_id)
    author.all()
    return author.to_dict()


def author_exists(author_dict):
    print("author_dao.author_exists()")
    record = Author.query.filter_by(**author_dict).all()
    print(record)
    return record is None


def create(book, list_author):
    print("author_dao.create()")

    for author in list_author:
        if Author.query.filter_by(**author).all():
            existing_record = Author.query.filter_by(**author).first()
            print(existing_record)
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
