

def test_checkout(new_checkout1):
    """
    Test default constructor for a checkout.
    :param new_checkout1: Fixture from conftest.
    :return: True if tests pass
    """
    assert new_checkout1.checkout_id is None
    assert new_checkout1.user_id == 1
    assert new_checkout1.book_id == 1
    assert new_checkout1.book_copy_id == 1
    assert new_checkout1.checkout_date == "2018-10-10"
    assert new_checkout1.due_date == "2018-10-20"
    assert new_checkout1.return_date is None


def test_to_dict(new_checkout1):
    """
    Tests to_dict method for a checkout.
    :param new_checkout1:  Fixture from conftest
    :return: true if test passes
    """
    user = new_checkout1.to_dict()
    expected_dict = {
        'checkout_id': None,
        'user_id': 1,
        'book_id': 1,
        'book_copy_id': 1,
        'checkout_date': '2018-10-10',
        'due_date': '2018-10-20',
        'return_date': None

    }

    assert expected_dict == user


def test_self_update(new_checkout1):
    """
    Test method to update fields
    :param new_checkout1: fixture from conftest
    :return: True if test passes
    """

    kwargs = {
        'checkout_id': None,
        'user_id': 1,
        'book_id': 1,
        'book_copy_id': 1,
        'checkout_date': '2018-10-10',
        'due_date': '2018-10-20',
        'return_date': '2018-10-15',
    }

    new_checkout1.update(**kwargs)
    assert new_checkout1.checkout_id is None
    assert 1 == new_checkout1.user_id
    assert 1 == new_checkout1.book_id
    assert 1 == new_checkout1.book_copy_id
    assert '2018-10-10' == new_checkout1.checkout_date
    assert '2018-10-20' == new_checkout1.due_date
    assert '2018-10-15' == new_checkout1.return_date

