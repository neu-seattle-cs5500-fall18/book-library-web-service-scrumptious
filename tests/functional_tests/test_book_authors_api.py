import json


def test_post_authors(session, client, book1_dict, author_dict, expected_author):
    """Add data to db"""
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(author_dict)

    """test incorrect id"""
    get_response = client.post("/books/L/authors", data=json_data, headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """test non-existent id"""
    get_response = client.post("/books/2/authors", data=json_data, headers={"Content-Type": "application/json"})
    assert 404 == get_response.status_code

    """test empty body"""
    get_response = client.post("/books/1/authors", headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """test incomplete body fields"""
    author = {'first_name': 'Shadow'}
    json_data = json.dumps(author)

    get_response = client.post("/books/1/authors", data=json_data, headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """Test actual case"""
    json_data = json.dumps(author_dict)
    get_response = client.post("/books/1/authors", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == get_response.status_code

    payload = get_response.get_json()

    assert expected_author == payload


def test_put_authors(session, client, book1_dict, author_dict2, expected_author2):
    """Add data to db"""
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(author_dict2)

    """test incorrect id"""
    get_response = client.put("/books/L/authors/1", data=json_data, headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """test incorrect id"""
    get_response = client.put("/books/1/authors/L", data=json_data, headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code


    """test non-existent id"""
    get_response = client.put("/books/2/authors/1", data=json_data, headers={"Content-Type": "application/json"})
    assert 404 == get_response.status_code

    """test non-existent id"""
    get_response = client.put("/books/1/authors/2", data=json_data, headers={"Content-Type": "application/json"})
    assert 404 == get_response.status_code

    """test empty body"""
    get_response = client.put("/books/1/authors/1", headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """test incomplete body fields"""
    author = {'first_name': 'Shadow'}
    json_data = json.dumps(author)

    get_response = client.put("/books/1/authors/1", data=json_data, headers={"Content-Type": "application/json"})
    assert 500 == get_response.status_code

    """Test actual case"""
    json_data = json.dumps(author_dict2)
    get_response = client.put("/books/1/authors/1", data=json_data, headers={"Content-Type": "application/json"})
    assert 200 == get_response.status_code

    payload = get_response.get_json()
    assert expected_author2 == payload

