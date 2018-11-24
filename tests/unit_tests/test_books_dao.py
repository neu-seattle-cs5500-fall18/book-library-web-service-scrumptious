from data_access_layer.book_dao import BookDao


def test_get_book():
    results = BookDao.get_all()
    print(results)
    assert results is not None

