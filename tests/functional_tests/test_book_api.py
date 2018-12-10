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

    # # """
    # # *
    # *
    # Testing query parameters
    # *
    # *
    # """
    #
    # """
    # title
    # """
    # expected_payload = []
    # expected_payload.append(book2_dict)
    # get_response = client.get("/books?title=Old Man and the Sea")
    # assert get_response == 200
    # payload = json.loads(get_response.data.decode('utf8'))
    # assert expected_payload == payload
    #
    #
    # """
    # first_name
    # """
    #
    # """
    # last_name
    # """
    #
    # """
    # middle_name
    # """
    #
    # """
    # publish_date_start
    # """
    #
    # """
    # publish_date_end
    # """
    #
    # """
    # subject
    # """
    #
    # """
    # genre
    # """
    #
    #
    #
    #

# #
# # def test_query_books(client):
# #     response = client.get('/books?=')
# #
# #     #actual result
# #
# #     #invalid query param
# #
# #     #each query param
# #
# #     return
# #
# def test_post_book(client):
#     response = client.post()
#     return
#






# # # '/books/<book_id>
# # def test_get_book(client):
# #     response = client.get('/books/1')
# #     #actual case
# #
# #     response2 = client.get('/books/3')
# #     #no such case
# #
# #     response3 = client.get('/books/l')
# #     # invalid input case return 400
# #     return
# #
# # def test_put_book(client):
# #
# #     return
# #
# # def test_delete_book(client):
# #     response = client.delete('/books/1')
# #
# #     response2 = client.delete('/books/4')
# #
# #     response3 = client.delete('/books/l')
# #
# #     return