from data_access_layer import author_dao
from flask_restplus import abort
import re


pattern = re.compile('\A(\w\.)+')


def valid_input(first_name, last_name, middle_name):
    print("author_checker.valid_input()")
    return (first_name is None or first_name.isalpha() or pattern.match(first_name)) and \
           (middle_name is None or middle_name.isalpha() or pattern.match(middle_name)) and \
           (last_name.isalpha() or pattern.match(last_name))


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


def create_authors(list_authors):
    """
    Method to verify the integrity of the body of a POST request to create a new author.
    Returns results back to book checker.
    :param list_json_authors: Json body of HTTP request.
    :return:
    """
    print('author_checker.create_author()')

    cleaned_list = []

    for author in list_authors:
        author_dict= {}
        author_dict['first_name'] = author['first_name']
        author_dict['last_name'] = author['last_name']
        author_dict['middle_name'] = author['middle_name']
        cleaned_list.append(author_dict)
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

