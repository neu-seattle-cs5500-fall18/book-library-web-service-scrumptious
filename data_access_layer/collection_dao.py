from model.collection import BookCollection
from model.book import Book
from flask_restplus import abort
from model import db


# def query_by_id(collections_id):
#     a_collection = BookCollection.query.get(collections_id)
#     return a_collection.to_dict()


# def query_by_title(title):
#     a_collection = BookCollection.query.filter_by(title=title)
#     return a_collection.to_dict


def contains(collection_id):
    result = BookCollection.query.get(collection_id)
    if result is None:
        return False
    return True


def create_collection(collection_title):
    """
    Instantiates a BookCollectiona and creates new record in database to attribute books to
    :param collection_title: The title of the collection.
    :return: Id of the created book collection
    """
    print('CollectionDao.create_collection')
    collection = BookCollection(title=collection_title)
    db.session.add(collection)
    db.session.commit()
    return collection.collection_id


def append_collection(collection_id, book):
    """
    Appends a book to a collection
    :param collection_id: id of collection to update
    :param book: instance of Book class to add to collection
    :return: dict of collection.
    """

    collection = BookCollection.query.get(collection_id)
    collection.book_ids.append(book)
    db.session.commit()
    return collection


# def create(collection_dict):
#     print("collection_dao.create()")
#     new_collection = BookCollection(**collection_dict)
#     db.session.add(new_collection)
#     print("collection_dao.create() ==> Complete")
#     db.session.commit()
#     return new_collection


# def update(collection_id, **kwargs):
#     collection = BookCollection.query.get(collection_id)
#     collection.update(**kwargs)
#     db.session.commit()
#     return collection


# def insert_book(collection_id, a_book):
#     collection = BookCollection.query.get(collection_id)
#     collection.books.append(a_book)
#     db.session.commit()
#     return collection.to_dict()


def delete_book(collection_id, a_book_id):
    collection = BookCollection.query.get(collection_id)
    books = collection.book_ids
    ind = 0
    for i, book in enumerate(books):
        if book['book_id'] == a_book_id:
            ind = i
    new_list = books.pop(ind)
    collection.book_ids = new_list
    db.session.commit()
    return collection.to_dict()


def get_collection(collection_id):
    print('Get collection')

    a_collection = BookCollection.query.get(collection_id)

    if a_collection is None:
        abort(404, 'Collection not found')
    else:
        return a_collection.to_dict()


def delete_collection(collection_id):
    print('Delete collection')
    a_collection = BookCollection.query.get(collection_id)
    a_collection.book_ids = []
    db.session.commit()
    db.session.delete(a_collection)
    db.session.commit()
    return
