from model.collection import BookCollection
from model.collection import Book


def test_collection(new_collection):
    """

    :param new_collection: Fixture from conftest
    :return: true if tests pass
    """
    assert new_collection.collection_id == 1


def test_to_dict(new_collection):
    """
    Tests if to dict works for Collection.
    :param new_collection: fixture from conftest
    :return: true if test passes
    """
    book1 = Book(book_id=1, title='The Old Man and the Sea', publish_date='1980', genre='Novel', subject='Fiction',
                 authors=[], notes=[], copies=[])

    collection_dict = {
        'collection_id': 1,
        'book_ids': [book1],
        'title': 'New collection',
    }
    collection = new_collection.to_dict()
    assert collection == collection_dict


def test_self_update(new_collection):
    """
    Tests update method for a collection
    :param new_collection: fixture from conftest
    :return: true if tests pass
    """
    update = {'title':'Old collection'}
    book1 = Book(book_id=1,title='The Old Man and the Sea',publish_date='1980',genre='Novel',subject='Fiction',
                       authors=[],notes=[],copies=[])

    collection_result = BookCollection(collection_id=1, book_ids=[book1], title='Old collection')
    new_collection.update(**update)
    assert new_collection == collection_result
