import os
import tempfile
import sqlite3
import pytest
from flask import Flask


# This file sets up fixtures to be used for scoped testing.


@pytest.fixture(scope='module')
def test_client():
    """
    Fixture to setup a new application for testing and database, and tear down application and database.
    :return: None
    """
    # Create new application and configure
    test_app = Flask(__name__)
    # Create temporary instance for db to go
    test_app.config['TESTING'] = True
    db_fd, test_app.config['DATABASE'] = tempfile.mkstemp()
    test_client = test_app.test_client()

    with test_app.app_context():
        sqlite3.connect(test_app.config['DATABASE'])

    yield test_client

    os.close(db_fd)
    os.unlink(test_app.config['DATABASE'])







