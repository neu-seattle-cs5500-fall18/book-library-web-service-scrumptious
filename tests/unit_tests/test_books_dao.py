from data_access_layer.book_dao import BookDao


def test_contains(function_test, book1, new_book_dao):
    id = book1.book_id
    result = new_book_dao.contains(id)
    assert result is True

    id = 6
    result = new_book_dao.contains(id)
    assert result is False

#
# def test_create_list_dict(new_book_dao, book1, book2):
#     query = new_book_dao.query.get_all()
#     results = new_book_dao.create_list_dict(query)
#     expected_result = [book1, book2]
#     assert results == expected_result
#
#
# def test_get(book1, new_book_dao):
#     id = book1.book_id
#     result = new_book_dao.get(id)
#
#     assert result == book1
#
#
# def test_get_all(new_book_dao):
#     results = new_book_dao.get_all()
#     expected_results = new_book_dao.query.all()
#     assert results == expected_results
#

# def test_query_books(new_book_dao):
#     #{query params}
#     # all params
#     # each single param
#     # no params
#     # crap values
#     return None
#
#
# def test_create(book_dict, new_book_dao):
#     #valid params
#     # non valid params
#     return None
#
#
# def test_update(book_id, **kwargs):
#     # valid params
#     # none valid params
#     return None
#
#
# def test_delete(a_book_id, new_book_dao):
#     #valid id
#     # non valid id
#     return None