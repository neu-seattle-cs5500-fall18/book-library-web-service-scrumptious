

def test_empty_db(client):
    rv = client.get('/')
    assert None in rv.data
