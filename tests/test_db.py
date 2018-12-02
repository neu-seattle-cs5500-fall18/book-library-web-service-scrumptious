

def test_empty_db(client):
    rv = client.get('/')
    return rv
