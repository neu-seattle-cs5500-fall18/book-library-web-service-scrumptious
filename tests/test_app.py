import os
import tempfile

import pytest

from library_webservice import app


@pytest.fixture
def client():
    db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.app.config['TESTING'] = True
    client = app.app.test_client()

    with app.app.app_context():
        app.init_db()

    yield client

    os.close(db_fd)
    os.unlink(app.app.config['DATABASE'])


def test_assertion_works():
    assert 1 == 1