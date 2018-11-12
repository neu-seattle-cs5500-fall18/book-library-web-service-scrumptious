from data_access_layer import book_dao, collection_dao
from flask_restplus import abort
from model.collection import BookCollection


def get_collections(**query_params):
    list_collections = []
    results = collection_dao.query_collections(**query_params)
    for collection in results:
        list_collections.append(collection.to_dict())

    return list_collections


def create_collection(collection_json):
    print("collection_checker.create_collection()")
    title = collection_json['title']
    collection_id = collection_json['collection_id']
    book_ids = collection_json['books'] #TODO:
    a_collection = {'title': title, 'collection_id': collection_id, 'book_ids': book_ids}
    new_collection = collection_dao.create(a_collection)
    print("collection_checker.create_collection() ==> Complete")
    print(new_collection)
    return new_collection.to_dict()


def get_collection(collection_id):
    collection = collection_dao.get_collection(collection_id)
    if collection is None:
        abort(400, 'Collection does not exist')
    else:
        collection = collection_dao.query_book_id(collection_id)
        return collection


def update_collection(collection_id, collection_json):
    collection = collection_dao.get_collection(collection_id)
    if collection is None:
        abort(400, 'Collection does not exist')
    else:
        clean_collection = {}
        for key, value in collection_json:
            clean_collection[key]=value
        collection_dao.update(collection_id, **clean_collection)
        return collection


def delete_collection(collection_id):
    collection = collection_dao.get_collection(collection_id)
    if collection is None:
        abort(400, 'Collection does not exist')
    else:
        id = collection_dao.delete_collection(collection_id) #TODO:
        return id


def add_book_to_collection_id(collection_id, book_id):
    a_collection = BookCollection.query.get(collection_id)
    a_book = book_dao.query_by_id(book_id)
    if a_collection is None:
        abort(404, 'Collection is empty')
    elif a_book is None:
        abort(404, 'This book does not exist in the collection.')
    else:
        updated_collection = collection_dao.insert_book(a_book)
        return update_collection()


def delete_book_from_collection_id(collection_id, book_id):
    a_collection = BookCollection.query.get(collection_id)
    a_book = book_dao.query_by_id(book_id)
    if a_collection is None:
        abort(404, 'Cannot remove a book from empty collection.')
    elif a_book is None:
        abort(404, 'This book does not exist in the collection.')
    else:
        collection_dao.insert_book(a_book)
        return a_collection
