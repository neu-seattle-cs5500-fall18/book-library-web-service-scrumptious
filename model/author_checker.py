from model import author_dao
from flask_restplus import abort
import re


pattern = re.compile('\A(\w\.)+')


def valid_input(first_name, last_name, middle_name):
    return (first_name.isalpha() or pattern.match(first_name) or first_name is None) and \
           (middle_name.isalpha() or pattern.match(middle_name) or middle_name is None) and \
           (last_name.isalpha() or pattern.match(last_name))


def clean_author(first_name, last_name, middle_name):
    print('Clean Author Info')

    if first_name is not None:
        first_name = first_name.lower().title()

    if middle_name is not None:
        if middle_name.len() == 1 and middle_name.isalpha():
            middle_name.append(".")
        elif pattern.match(middle_name):
            middle_name = middle_name[0].upper() + '.'
        else:
            middle_name.lower().title()

    formatted_author = {
        'author_first_name': first_name.lower().title(),
        'author_last_name': last_name,
        'author_middle_name': middle_name
    }
    print(formatted_author)
    return formatted_author


def create_author(json_author_info):
    """
    Method to verify the integrity of the body of a POST request to create a new author.
    :param json_author_info: Json body of HTTP request.
    :return: Json of the id of the newly created Author.
    """
    print('Create author')

    f_name = json_author_info['first_name']
    l_name = json_author_info['last_name']
    m_name = json_author_info['middle_name']

    if valid_input(f_name, l_name, m_name):
        author_dict = clean_author(f_name, l_name, m_name)
        return author_dao.create_author(author_dict)
    else:
        abort(400, 'Invalid input')

def create(book, list_authors):
    temp_list = []
    for e in list_authors:
        author = author_dao.create(book, e)
        temp_list.append(author)
        return temp_list

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

