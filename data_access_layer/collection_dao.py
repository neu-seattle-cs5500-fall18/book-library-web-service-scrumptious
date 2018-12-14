from model.collection import BookCollection
from flask_restplus import abort
from model import db


def contains(collection_id):
    """
    Checks if a collection is present in the database using ID.
    :param collection_id: ID of the collection being searched for.
    :return: Boolean True or False.
    """
    result = BookCollection.query.get(collection_id)
    if result is None:
        return False
    return True


def create_collection(collection_title):
    """
    Instantiates a BookCollectiona and creates new record in database to attribute books to.
    :param collection_title: The title of the collection.
    :return: ID of the created book collection.
    """
    print('CollectionDao.create_collection')
    collection = BookCollection(title=collection_title)
    db.session.add(collection)
    db.session.commit()
    return collection.collection_id


def append_collection(collection_id, book):
    """
    Appends a book to a collection.
    :param collection_id: ID of collection to update.
    :param book: instance of Book class to add to collection.
    :return: dict of collection.
    """

    collection = BookCollection.query.get(collection_id)
    collection.book_ids.append(book)
    db.session.commit()
    return collection


def delete_book(collection_id, a_book_id):
    """
    Deletes a book from a collection by ID name.
    :param collection_id: ID of collection.
    :param a_book_id: ID of book to be removed.
    :return: Dictionary object of updated collection.
    """
    print('delete book from list')
    collection = BookCollection.query.get(collection_id)
    books = collection.book_ids
    print(books)
    print(type(books))
    ind = 0

    for i, book in enumerate(books):

        if book.book_id == a_book_id:
            ind = i

    del books[ind]

    collection.book_ids = books
    db.session.commit()
    return collection.to_dict()


def get_collection(collection_id):
    """
    Gets a collection by ID name.
    :param collection_id: ID of collection.
    :return: Dictionary object of the collection.
    """
    print('Get collection')

    a_collection = BookCollection.query.get(collection_id)

    if a_collection is None:
        abort(404, 'Collection not found')
    else:
        return a_collection.to_dict()


def delete_collection(collection_id):
    """
    Deletes a collection by ID name.
    :param collection_id: ID of collection.
    :return: None.
    """
    print('Delete collection')
    a_collection = BookCollection.query.get(collection_id)
    a_collection.book_ids = []
    db.session.commit()
    db.session.delete(a_collection)
    db.session.commit()
    return
