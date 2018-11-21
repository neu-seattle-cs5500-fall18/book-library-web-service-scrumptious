from model.collection import BookCollection
from flask_restplus import abort
from model import db


def query_by_id(collections_id):
    a_collection = BookCollection.query.get(collections_id)
    return a_collection.to_dict()


def query_by_title(title):
    a_collection = BookCollection.query.filter_by(title=title)
    return a_collection.to_dict


def create(collection_dict):
    print("collection_dao.create()")
    new_collection = BookCollection(**collection_dict)
    db.session.add(new_collection)
    print("collection_dao.create() ==> Complete")
    db.session.commit()
    return new_collection


def update(collection_id, **kwargs):
    collection = BookCollection.query.get(collection_id)
    collection.update(**kwargs)
    db.session.commit()
    return collection


def insert_book(collection_id, a_book):
    collection = BookCollection.query.get(collection_id)
    collection.books.append(a_book)
    db.session.commit()
    return collection.to_dict()


def delete_book(collection_id, a_book):
    collection = BookCollection.query.get(collection_id)
    collection.books.remove(a_book)
    db.session.commit()
    return collection.to_dict()


def get_collection(collection_id):
    print('Get collection')

    a_collection = BookCollection.query.get(collection_id)

    if a_collection is None:
        abort(400, 'Collection not found')
    else:
        return a_collection


def delete_collection(collection_id):
    print('Delete collection')

    a_collection = BookCollection.query.get(collection_id)

    if a_collection is None:
        abort(400, 'Record not found')
    else:
        a_collection.is_deleted = True
        db.session.commit()
        return a_collection.collection_id
