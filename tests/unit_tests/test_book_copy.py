

def test_book_copy(new_book_copy1):
    """
    Tests constructor for a BookCopy
    :param new_book_copy: fixture from conftest
    :return: true if tests pass.
    """
    assert new_book_copy1.book_copy_id is None
    assert new_book_copy1.book_id == 1
    assert new_book_copy1.is_checked_out is False


def test_to_dict(new_book_copy1):
    """
    Tests to_dict() method
    :param new_book_copy: fixture from conftest
    :return: true if test passes
    """
    expected_result = {'book_copy_id':None,'book_id':1,'is_checked_out':False}
    assert expected_result == new_book_copy1.to_dict()


def test_self_update(new_book_copy1):

    kwargs = dict(book_copy_id=1,book_id=2,is_checked_out=True)
    new_book_copy1.update(**kwargs)
    assert new_book_copy1.book_copy_id == 1
    assert new_book_copy1.book_id == 2
    assert new_book_copy1.is_checked_out is True
