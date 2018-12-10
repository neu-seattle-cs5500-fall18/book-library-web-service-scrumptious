import json


def test_get_books(client, book1_dict, expect_book1_dict):
    """
    Test query books via a get request.
    case1: empty resource
    case2: resource with book
    :param client: Instance of application
    :param book1_dict: Dictionary of a book to be loaded into application via a post request
    :param expect_book1_dict: the expected resulting dictionary from a get request on resource
    :return: passed if all tests are valid
    """
    """
    Test case for resource that contains no records
    """
    response = client.get('/books')
    assert response.status_code == 200

    response = json.loads(response.data.decode('utf8'))
    assert [] == response

    """
    Test case for resource that contains records.
    """
    # case with data loaded
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    response = client.get('/books')
    assert response.status_code == 200

    response = json.loads(response.data.decode('utf8'))
    book = response[0]
    assert expect_book1_dict == book




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