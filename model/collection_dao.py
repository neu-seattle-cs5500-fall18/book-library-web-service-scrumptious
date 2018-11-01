from model.collection import BookCollection
from flask_restplus import abort
from library_webservice import db


def get_all_collections():
    print('Get all collections')
    list_of_collections = BookCollection.query.all()
    return list_of_collections


def create_new_collection(collection_info):
    print('Creating new collection')

    collection_id = collection_info['collection_id']
    book_ids = collection_info['book_ids']
    title = collection_info['collection_title']

    new_collection = BookCollection(collection_id=collection_id, book_ids=book_ids, title=title)

    db.session.add(new_collection)
    db.session.commit()

    return new_collection.collection_id


def add_book_to_collection_id(collection_id, book_id):
    list_of_collections = BookCollection.query.all()
    a_collection = BookCollection.query.get(collection_id)
    # not sure if this will work (check if book id exists in library)
    if str(book_id) in list_of_collections.book_ids:
        current_book_ids_list = a_collection.book_ids.split(",")
        current_book_ids_list.append(str(book_id))
        a_collection.book_ids = ''.join(current_book_ids_list)

    else:
        return "Book id " + str(book_id) + " doesn't exist in library " + str(collection_id)
    db.session.commit()
    return "Added Book id " + str(book_id) + " to collection id " + str(collection_id)


def delete_book_from_collection_id(collection_id, book_id):
    a_collection = BookCollection.query.get(collection_id)
    current_book_ids_list = a_collection.book_ids.split(",")
    if str(book_id) in current_book_ids_list:
        current_book_ids_list.remove(str(book_id))
        a_collection.book_ids = ''.join(current_book_ids_list)

    else:
        return "Cant delete! Book id " + str(book_id) + " doesn't exist in collection id " + str(collection_id)

    db.session.commit()
    return "Book id " + str(book_id) + " deleted from collection id " + str(collection_id)


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
