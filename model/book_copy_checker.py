from model import book_copy_dao


def create_copy(book):
    return book_copy_dao.create(book)

