

def test_author(new_author):
    """
    Given a User model, when a User is created
    Test the ID, First Name, Last Name Middle Name.
    """
    assert new_author.author_id == 1
    assert new_author.first_name == 'Herman'
    assert new_author.last_name == 'Melville'
    assert new_author.middle_name == 'M'


