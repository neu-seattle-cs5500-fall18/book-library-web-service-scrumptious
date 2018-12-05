# from flask import jsonify
# # '/books'
#
# def test_get_books(client, book1, book2):
#     response = client.get('/books')
#
#     expected_result = jsonify([book1, book2])
#
#     assert response == expected_result
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
# # def test_post_book(client, test_db):
# #     response = client.post()
# #     return
# #
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