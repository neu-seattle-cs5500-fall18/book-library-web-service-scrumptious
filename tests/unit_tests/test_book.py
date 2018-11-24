from model.book import Book


def test_book(new_book):
    """

    :param new_book: Fixture from conftest
    :return: true if tests pass
    """
    assert new_book.book_id == 1
    assert new_book.genre == 'Novel'
    assert new_book.subject == 'Fiction'
    assert new_book.title == 'Old Man'
    assert new_book.publish_date == '1980'
    assert new_book.authors == []
    assert new_book.notes == []
    assert new_book.copies == []


def test_to_dict(new_book):
    """
    Tests if to dict works for Book.
    :param new_book: fixture from conftest
    :return: true if test passes
    """
    book_dict = {
        'book_id': 1,
        'title': 'Old Man',
        'publish_date': '1980',
        'genre': 'Novel',
        'subject': 'Fiction',
        'authors': [],
        'notes': [],
        'copies': []
    }
    book = new_book.to_dict()
    assert book == book_dict


def test_self_update(new_book):
    """
    Tests update method for a book
    :param new_book: fixture from conftest
    :return: true if tests pass
    """
    update = {'title':'The Old Man and the Sea'}
    book_result = Book(book_id=1,title='The Old Man and the Sea',publish_date='1980',genre='Novel',subject='Fiction',
                       authors=[],notes=[],copies=[])
    new_book.update(**update)
    print(new_book)
    print(book_result)
    assert new_book == book_result

