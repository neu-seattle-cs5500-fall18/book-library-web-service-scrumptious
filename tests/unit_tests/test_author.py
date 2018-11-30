from model.author import Author


def test_author(new_author):
    """
    Tests if constructor for Author works as expected
    :param new_author: fixture from conftest
    :return: true if tests pass
    """
    assert new_author.author_id == 1
    assert new_author.first_name == 'Herman'
    assert new_author.last_name == 'Melville'
    assert new_author.middle_name == 'M'


def test_to_dict(new_author):
    """
    Tests if to_dict method works for Author
    :param new_author: fixture from conftest
    :return: true if tests pass
    """
    author_to_dict = {
        'author_id':1,'first_name':'Herman','last_name':'Melville','middle_name':'M'
    }
    new_author.to_dict()
    print(author_to_dict)
    print(new_author)
    assert new_author == author_to_dict


def test_self_update(new_author):
    """
    Tests if update() mehtod works for Author.
    :param new_author: fixture from conftest.
    :return: true if tests pass
    """

    expected_result = Author(author_id=1, first_name='Herman', last_name='Melville', middle_name='M')
    assert new_author == expected_result

    expected_result = Author(author_id=1, first_name='Henry', last_name='Melville', middle_name='M')
    kwargs = {'first_name': 'Henry'}
    new_author.update(**kwargs)
    assert new_author == expected_result

    expected_result = Author(author_id=1, first_name='Henry', last_name='Mel', middle_name='M')
    kwargs = {'last_name' : 'Mel'}
    new_author.update(**kwargs)
    assert new_author == expected_result

    expected_result = Author(author_id=1, first_name='Henry', last_name='Mel', middle_name='New')
    kwargs = {'middle_name' : 'New'}
    new_author.update(**kwargs)
    assert new_author == expected_result




