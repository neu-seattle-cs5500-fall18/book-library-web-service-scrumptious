import json


def test_get_copies(session, client, book1_dict, expected_copies1):
    """Add data to db"""
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    """test incorrect id"""
    get_response = client.get("/books/2/copies")
    assert 404 == get_response.status_code

    """test nonexistent id"""
    get_response = client.get("/books/L/copies")
    assert 400 == get_response.status_code

    """test actual id"""
    get_response = client.get("/books/1/copies")
    assert 200 == get_response.status_code

    expected_payload= [expected_copies1]
    payload = get_response.get_json()
    assert expected_payload== payload


def test_post_copies(session, client, book1_dict, expected_copies1, expected_copies2):
    """Add data to db"""
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code


    """test incorrect id"""
    get_response = client.post("/books/2/copies")
    assert 404 == get_response.status_code

    """test nonexistent id"""
    get_response = client.post("/books/L/copies")
    assert 400 == get_response.status_code

    """test posting to actual id"""
    get_response = client.post("/books/1/copies")
    assert 201 == get_response.status_code

    payload = get_response.get_json()
    assert expected_copies2 == payload

    """test retrieving all copies"""
    get_response = client.get("/books/1/copies")
    assert 200 == get_response.status_code

    payload = get_response.get_json()
    expected_payload = [expected_copies1, expected_copies2]
    assert expected_payload == payload

