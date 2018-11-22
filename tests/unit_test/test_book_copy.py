

def test_book_copy(new_book_copy):
    """

    :param new_book_copy:
    :return:
    """
    assert new_book_copy.book_copy_id == 1
    assert new_book_copy.book_id == 1
    assert new_book_copy.is_checked_out == False


def test_to_dict(new_book_copy):
    copy_to_dict = {'book_copy_id':1,'book_id':1,'is_checked_out':False}
    new_book_copy.to_dict()
    assert new_book_copy == copy_to_dict

