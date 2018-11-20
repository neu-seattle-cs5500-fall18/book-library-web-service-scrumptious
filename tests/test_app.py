import os
import tempfile

import pytest

import library_webservice


@pytest.fixture
def client():
    db_fd, library_webservice.app.config['DATABASE'] = tempfile.mkstemp()
    library_webservice.app.config['TESTING'] = True
    client = library_webservice.app.test_client()

    with library_webservice.app.app_context():
        library_webservice.init_db()

    yield client

    os.close(db_fd)
    os.unlink(library_webservice.app.config['DATABASE'])


