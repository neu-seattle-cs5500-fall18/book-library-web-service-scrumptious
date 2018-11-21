# import os
# import tempfile
from model.author import Author
import pytest

# from library_webservice import app


@pytest.fixture(scope = 'module')
def new_author():
    author = Author(author_id=1, first_name='Herman', last_name='Melville', middle_name='M')
    return author




#
# @pytest.fixture
# def client():
#     db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
#     app.app.config['TESTING'] = True
#     client = app.app.test_client()
#
#     with app.app.app_context():
#         app.init_db()
#
#     yield client
#
#     os.close(db_fd)
#     os.unlink(app.app.config['DATABASE'])
#
#
# def test_assertion_works():
#     assert 1 == 1
#
# def test_empty_db(client):
#     rv = client.get('/authors')
#     assert b'No entries here so far' in rv.data
