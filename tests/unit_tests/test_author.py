

def test_author(new_author1):
    """
    Tests if constructor for Author works as expected
    :param new_author: fixture from conftest
    :return: true if tests pass
    """
    assert new_author1.author_id is None
    assert new_author1.first_name == 'Herman'
    assert new_author1.last_name == 'Melville'
    assert new_author1.middle_name == 'M'


def test_to_dict(new_author1):
    """
    Tests if to_dict method works for Author
    :param new_author: fixture from conftest
    :return: true if tests pass
    """
    expected_result = dict(author_id=None,first_name='Herman',last_name='Melville',middle_name='M')

    assert expected_result == new_author1.to_dict()


def test_self_update(new_author1):
    """
    Tests if update() mehtod works for Author.
    :param new_author: fixture from conftest.
    :return: true if tests pass
    """

    updates = {
        'author_id': 1,
        'first_name': 'Hermie',
        'last_name': 'Mel',
        'middle_name': 'K'
    }

    new_author1.update(**updates)

    assert new_author1.author_id == 1
    assert new_author1.first_name == 'Hermie'
    assert new_author1.last_name == 'Mel'
    assert new_author1.middle_name == 'K'



