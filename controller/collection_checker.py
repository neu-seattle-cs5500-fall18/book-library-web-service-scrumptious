from data_access_layer import collection_dao
from data_access_layer.book_dao import BookDao
from flask_restplus import abort
from model.collection import BookCollection


def create_collection(collection_json):
    """
    Function to create a collection from collection Json object.
    :param collection_json: Json collection object.
    :return: the new collection ID
    """
    print("collection_checker.create_collection()")
    title = collection_json['title']
    collection_id = collection_dao.create_collection(title)

    list_book_ids = collection_json['book_ids']
    for book_id in list_book_ids:
        if BookDao.contains(book_id):
            continue
        else:
            abort(404, 'Invalid book ID')

    for book_id in list_book_ids:
        book = BookDao.get_book_object(book_id)
        collection_dao.append_collection(collection_id, book)
    return collection_dao.get_collection(collection_id)


def get_collection(collection_id):
    """
    Gets a collection by ID.
    :param collection_id: ID of collection.
    :return: The collection.
    """
    print('collection_checker.get_collection()')
    collection = collection_dao.get_collection(collection_id)
    if collection is None:
        abort(404, 'Collection does not exist')
    else:
        collection = collection_dao.get_collection(collection_id)
        print(collection)
        return collection


def delete_collection(collection_id):
    """
    Deletes a collection by ID.
    :param collection_id: ID of collection.
    :return: None.
    """
    if collection_dao.contains(collection_id):
        return collection_dao.delete_collection(collection_id)
    else:
        abort(400, 'Collection does not exist')


def add_book_to_collection_id(collection_id, book_id):
    """
    Adds a book to a collection by ID name.
    :param collection_id: ID of collection.
    :param book_id: ID of book to be added.
    :return: The updated collection.
    """
    a_collection = BookCollection.query.get(collection_id)
    a_book = BookDao.get_book_object(book_id)
    if a_collection is None:
        abort(404, 'Collection is empty')
    elif a_book is None:
        abort(404, 'This book does not exist in the collection.')
    else:
        updated_collection = collection_dao.append_collection(collection_id, a_book)
        return updated_collection


def delete_book_from_collection_id(collection_id, book_id):
    """
    Deletes a book from a collection by ID name.
    :param collection_id: ID of collection.
    :param book_id: ID of book to be removed.
    :return: The updated collection.
    """
    a_collection = BookCollection.query.get(collection_id)
    a_book = BookDao.get_book_object(book_id)
    if a_collection is None:
        abort(404, 'Cannot remove a book from empty collection.')
    elif a_book is None:
        abort(404, 'This book does not exist in the collection.')
    else:
        updated_collection = collection_dao.delete_book(collection_id, book_id)
        return updated_collection
