

def test_author(new_author):
    """

    :param new_author:
    :return:
    """
    assert new_author.author_id == 1
    assert new_author.first_name == 'Herman'
    assert new_author.last_name == 'Melville'
    assert new_author.middle_name == 'M'


def test_to_dict(new_author):
    author_to_dict = {
        'author_id':1,'first_name':'Herman','last_name':'Melville','middle_name':'M'
    }
    new_author.to_dict()
    print(author_to_dict)
    print(new_author)
    assert new_author == author_to_dict


