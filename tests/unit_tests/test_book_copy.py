from model.book_copy import BookCopy

def test_book_copy(new_book_copy):
    """
    Tests constructor for a BookCopy
    :param new_book_copy: fixture from conftest
    :return: true if tests pass.
    """
    assert new_book_copy.book_copy_id == 1
    assert new_book_copy.book_id == 1
    assert new_book_copy.is_checked_out == False


def test_to_dict(new_book_copy):
    """
    Tests to_dict() method
    :param new_book_copy: fixture from conftest
    :return: true if test passes
    """
    copy_to_dict = {'book_copy_id':1,'book_id':1,'is_checked_out':False}
    new_book_copy.to_dict()
    assert new_book_copy == copy_to_dict

def test_self_update(new_book_copy):

    expected_result = BookCopy(book_copy_id=1, book_id=1, is_checked_out=True)
    kwargs = {'is_checked_out': True}
    new_book_copy.update(**kwargs)
    assert new_book_copy == expected_result
