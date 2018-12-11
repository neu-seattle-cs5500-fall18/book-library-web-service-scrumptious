import json


def test_post_book(session, client, book1_dict,  book2_dict, book3_dict):

    """New Resource"""
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert  201 == post_response.status_code

    """Re-posting resource"""
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert post_response.status_code == 400
    assert b"Book already exists" in post_response.data

    """Post book two same author"""
    json_data = json.dumps(book2_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    """Post with missing required fields in body"""
    test_dict = {
        'publish_date': '1980-05-12',
        'subject': 'Fiction',
        'genre': 'Novel',
        'notes': [],
        'authors': [
            {
                'first_name': 'Herman',
                'last_name': 'Melville',
                'middle_name': 'M'
            }
        ]
    }
    json_data = json.dumps(test_dict)
    post_response = client.post("/books", data=json_data, headers = {"Content-Type": "application/json"})
    assert 400 == post_response.status_code


def test_get_books(session, client, book1_dict, book2_dict, book3_dict, expect_book1_dict, expect_book2_dict,
                   expect_book3_dict):
    """
    Test query of books resource via a get request on /books
    case1: empty resource
    case2: resource with book, no query string.
    case3: resource with books, query strings.
    """
    expected_payload = []

    """
    Test case for resource that contains no records
    """
    response = client.get('/books')
    assert response.status_code == 200
    response = json.loads(response.data.decode('utf8'))
    assert expected_payload == response


    """
    Test case for resource that contains records.
    """
    """Add book to database"""
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    get_response = client.get('/books')
    assert get_response.status_code == 200
    expected_payload.append(expect_book1_dict)
    payload = get_response.get_json()
    assert expected_payload == payload

    """
    adding Second book
    """
    json_data = json.dumps(book2_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    get_response = client.get('/books')
    assert get_response.status_code == 200
    expected_payload.append(expect_book2_dict)
    payload = get_response.get_json()
    assert expected_payload == payload


def test_query_books(session, client, book1_dict, book2_dict, book3_dict, expect_book1_dict, expect_book2_dict,
                     expect_book3_dict):
    expected_payload = []

    """Empty db case"""
    get_response = client.get('/books?title=1984')
    assert get_response.status_code == 200
    payload = get_response.get_json()
    assert expected_payload == payload


    """Add data to db"""
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(book2_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(book3_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    """get title"""
    expected_payload = []
    expected_payload.append(expect_book2_dict)
    get_response = client.get("/books?title=Old Man and the Sea")
    assert get_response == 200
    payload = get_response.get_json()
    assert expected_payload == payload

    """get by first_name"""
    expected_payload = []
    expected_payload.append(expect_book1_dict)
    expected_payload.append(expect_book2_dict)

    get_response = client.get("/books?first_name=Herman")
    assert get_response == 200
    payload = get_response.get_json()
    assert expected_payload == payload

    """get by last_name"""
    expected_payload = []
    expected_payload.append(expect_book3_dict)

    get_response = client.get("/books?last_name=Steinbeck")
    assert 200 == get_response.status_code
    payload = get_response.get_json()
    assert expected_payload == payload

    """get by middle_name"""
    expected_payload = []
    expected_payload.append(expect_book1_dict)
    expected_payload.append(expect_book2_dict)

    get_response = client.get("/books?middle_name=M")
    assert 200 == get_response.status_code
    payload = get_response.get_json()
    assert expected_payload == payload


    """get by publish_date_start"""
    expected_payload = []
    expected_payload.append(expect_book1_dict)
    expected_payload.append(expect_book3_dict)
    get_response = client.get("/books?publish_date_start=1910-05-13")
    assert 200 == get_response.status_code
    payload = get_response.get_json()
    print(payload)
    print(expected_payload)
    assert expected_payload == payload

    # """get by publish_date_end"""
    # expected_payload = []
    # expected_payload.append(expect_book2_dict)
    # get_response = client.get("/books?publish_date_end=1910-05-13")
    # assert 200 == get_response.status_code
    # payload = get_response.get_json()
    # assert  expected_payload == payload

    """get by subject"""
    expected_payload = []
    expected_payload.append(expect_book1_dict)
    get_response = client.get("/books?subject=Non-Fiction")
    assert 200 == get_response.status_code
    payload = get_response.get_json()
    assert expected_payload == payload

    """get by genre"""
    expected_payload = []
    expected_payload.append(expect_book3_dict)
    get_response = client.get("/books?genre=Literary Fiction")
    assert 200 == get_response.status_code
    payload = get_response.get_json()
    assert expected_payload == payload


# # # '/books/<book_id>
def test_get_book(session, client, book1_dict, book2_dict, book3_dict, expected_book3_fulldict):
    """get on empty resource"""
    get_response = client.get("/books/1")
    assert 404 == get_response.status_code

    """Add data to db"""
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(book2_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(book3_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    """get on non-empy resource"""
    get_response = client.get("/books/3")
    assert 200 == get_response.status_code
    payload = get_response.get_json()
    assert expected_book3_fulldict == payload

    """get with invalid input"""
    get_response = client.get("/books/L")
    assert 400 == get_response.status_code

    """get with non-existant resource"""
    get_response = client.get("books/7")
    assert 404 == get_response.status_code

    """get with out of range"""
    get_response = client.get("books/-1")
    assert 400 == get_response.status_code


def test_put_book(session, client, book1_dict):
    """Add data to db"""
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    change_dict = {
            "title": "Another Title2",
            "publish_date": "2010-01-10",
            "subject": "Subject",
            "genre": "Scifi Horror"
        }

    json_data = json.dumps(change_dict)

    expected_payload = {
        "book_id": 1,
        "title": "DifferentTitle2",
        "publish_date": "1900-01-01",
        "subject": "Reference",
        "genre": "Scifi Horror",
        "notes": [],
        "authors": [
            {
                "author_id": 1,
                "first_name": "Herman",
                "last_name": "Melville",
                "middle_name": "M"
             }
        ]
    }

    """put with non-existant resource"""
    get_response = client.put("/books/8", data=json_data, headers={"Content-Type": "application/json"})
    assert 404 == get_response.status_code

    """put with invalid id"""
    get_response = client.put("/books/L", data=json_data, headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """put with no content"""
    get_response = client.put("books/1", headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    # """put with correct info."""
    # get_response = client.put("/books/1", data=json_data, headers={"Content-Type": "application/json"})
    # # print('here!!!!!!')
    # # print(get_response)
    # # print(get_response.status_code)
    # # print(get_response.get_json)
    # assert 200 == get_response.status_code
    #




def test_delete_book(session, client, book1_dict, book2_dict, book3_dict, expect_book2_dict, expect_book3_dict):
    """Add data to db"""
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(book2_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(book3_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    """delete on non-existant resource"""
    get_response = client.delete("/books/20")
    assert 404 == get_response.status_code

    """delete on invalid id"""
    get_response = client.delete("/books/L")
    assert 400 == get_response.status_code

    """Valid delete"""
    get_response = client.delete('/books/1')
    assert 204 == get_response.status_code

    """test state of db after valid delete"""
    expected_payload = []
    expected_payload.append(expect_book2_dict)
    expected_payload.append(expect_book3_dict)
    get_response = client.get("/books")
    assert 200 == get_response.status_code
    payload = get_response.get_json()
    assert expected_payload == payload

    """test re-deleting resource"""
    get_response = client.delete("/books/1")
    assert 404 == get_response.status_code
