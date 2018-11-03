from model import author
import re


def valid_input(first_name):
    return first_name.isalpha()


def clean_author(first_name, last_name, middle_name):
    print('Clean Author Info')

    pattern = re.compile('\A(\w\.)+')

    if last_name is not None:
        last_name = last_name.lower().title()

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

