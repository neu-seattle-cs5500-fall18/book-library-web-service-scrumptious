from model import author_dao
from flask_restplus import abort
import re


pattern = re.compile('\A(\w\.)+')


def valid_input(first_name, last_name, middle_name):
    print("author_checker.valid_input()")
    return True
    # return (first_name.isalpha() or pattern.match(first_name) or first_name is None) and \
    #        (middle_name.isalpha() or pattern.match(middle_name) or middle_name is None) and \
    #        (last_name.isalpha() or pattern.match(last_name))


def clean_author(first_name, last_name, middle_name):
    print('author_checker.clean_author')

    if first_name is not None:
        first_name = first_name.lower().title()

    if middle_name is not None:
        if len(middle_name) == 1 and middle_name.isalpha():
            middle_name.append(".")
        elif pattern.match(middle_name):
            middle_name = middle_name[0].upper() + '.'
        else:
            middle_name.lower().title()

    formatted_author = {
        'first_name': first_name.lower().title(),
        'last_name': last_name,
        'middle_name': middle_name
    }
    print(formatted_author)
    return formatted_author


def create_author(list_json_authors):
    """
    Method to verify the integrity of the body of a POST request to create a new author.
    Returns results back to book checker.
    :param list: Json body of HTTP request.
    :return:
    """
    print('author_checker.create_author()')

    cleaned_list = []

    for e in list_json_authors:
        f_name = e['first_name']
        l_name = e['last_name']
        m_name = e['middle_name']

        if valid_input(f_name, l_name, m_name):
            author_dict = clean_author(f_name, l_name, m_name)
            cleaned_list.append(author_dict)
        else:
            abort(400, 'Invalid input')

    return cleaned_list


def get_author(author_id):
    """
    Method to get a specific author record based on author_id.
    :param author_id: Record of Author to get.
    :return: Json of an Author Dict
    """
    print('Get author %r' % author_id)
    an_author = author_dao.get_author(author_id)
    return an_author


def update_author(author_id, json_author_info):
    f_name = json_author_info['first_name']
    l_name = json_author_info['last_name']
    m_name = json_author_info['middle_name']

    if valid_input(f_name, l_name, m_name):
        author = clean_author(f_name, l_name, m_name)
        return update_author(author_id, author)
    else:
        abort(400, 'Invalid input')

