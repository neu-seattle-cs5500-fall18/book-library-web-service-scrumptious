

def test_book(new_book1):
    """
    Test default constructor for a book
    :param new_book1: Fixture from conftest
    :return: true if tests pass
    """
    assert new_book1.book_id is None
    assert new_book1.genre == 'Novel'
    assert new_book1.subject == 'Fiction'
    assert new_book1.title == 'Old Man'
    assert new_book1.publish_date == '1980'
    assert new_book1.authors == []
    assert new_book1.notes == []
    assert new_book1.copies == []


def test_to_dict(new_book1):
    """
    Tests if to dict works for Book.
    :param new_book1: fixture from conftest
    :return: true if test passes
    """

    book = new_book1.to_dict()

    expected_dict = {
        'book_id': None,
        'title': 'Old Man',
        'publish_date': '1980',
        'subject': 'Fiction',
        'genre': 'Novel',
        'notes': [],
        'authors': [],
        'copies': []
    }

    assert expected_dict == book


def test_self_update(new_book1):
    """
    Tests update method for a book
    :param new_book1: fixture from conftest
    :return: true if tests pass
    """
    kwargs = {'title': 'The Old Man and the Sea',
              'publish_date': 1981,
              'genre': 'Literature',
              'subject': 'Still Fiction'}

    new_book1.update(**kwargs)

    assert new_book1.book_id is None
    assert new_book1.title == 'The Old Man and the Sea'
    assert new_book1.publish_date == 1981
    assert new_book1.genre == 'Literature'
    assert new_book1.subject == 'Still Fiction'
    assert new_book1.authors == []
    assert new_book1.notes == []
    assert new_book1.copies == []

