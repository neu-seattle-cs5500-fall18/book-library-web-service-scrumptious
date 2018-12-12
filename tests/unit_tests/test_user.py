
def test_user(new_user1):
    """
    Test default constructor for a user.
    :param new_user1: Fixture from conftest.
    :return: True if tests pass
    """
    assert new_user1.user_id is None
    assert new_user1.user_first_name == 'FirstName'
    assert new_user1.user_last_name == 'LastName'
    assert new_user1.email == 'asdf@some.com'


def test_to_dict(new_user1):
    """
    Tests to_dict method for a user.
    :param new_user1:  Fixture from conftest
    :return: true if test passes
    """
    user = new_user1.to_dict()
    expected_dict ={
        'user_id' : None,
        'user_first_name': 'FirstName',
        'user_last_name' : 'LastName',
        'user_email' : 'asdf@some.com'
    }

    assert expected_dict == user


def test_self_update(new_user1):
    """
    Test method to update fields
    :param new_user1: fixture from conftest
    :return: True if test passes
    """

    kwargs = {
        'user_first_name' : 'John',
        'user_last_name' : 'Does',
        'email' : 'updated@gmail.com'
    }

    new_user1.update(**kwargs)
    assert new_user1.user_id is None
    assert  'John' == new_user1.user_first_name
    assert 'Does' == new_user1.user_last_name
    assert 'updated@gmail.com' == new_user1.email