from flask import request
from flask_restplus import abort, fields, Namespace, reqparse, Resource
from model import book_checker


api = Namespace('books', description='Book operations')

note = api.model('Note', {
    'notes': fields.String(required=True, description='Note about a book.')
})


# Response model, any other fields are considered private and not returned
book_marshaller = api.model('Book', {
    'book_id': fields.Integer(required=True, description='The book record'),
    'title': fields.String(description='The book title.'),
    'publish_date': fields.Date(description='The publish date of a book.'),
    'subject': fields.String(description='Subject for a book, such as "science", "Reference", "Non-Fiction"'),
    'genre': fields.String(description='Genre classification for a fiction book (i.e. horror, science fiction'),
    'note': fields.String(description='Personal note about a book.')
})

query_parser = reqparse.RequestParser()
query_parser.add_argument('title', required=False)
query_parser.add_argument('author_first_name', required=False)
query_parser.add_argument('author_last_name', required=False)
query_parser.add_argument('publish_date', action='append', required=False)
query_parser.add_argument('subject', action='append', required=False)
query_parser.add_argument('genre', action='append', required=False)
query_parser.add_argument('is_deleted', default=False)


@api.route('', endpoint='books')
@api.response(200, 'Success')
@api.response(400, 'Validation Error')
class Books(Resource):
    # this ensures arguments are valid and get can receive appropriate query params.
    @api.doc(body=query_parser, validate=True)
    @api.marshal_with(book_marshaller, code=200)
    def get(self):
        """
        Queries the books resource based on URL query string parameters.
        :return: List of all books that match query parameters. If parameters are empty, all books are returned.
        """
        print('Received GET on resource /books')

        query_args = query_parser
        list_of_books = book_checker.get_books(query_args)
        return list_of_books

    # This ensures body of request matches book model
    #@api.expect(book_marshaller, validate=True)
    @api.response(201, 'Created')
    @api.marshal_with(book_marshaller, 201)
    def post(self):
        """
        Creates a new book record for a single book.
        :return: Book ID of the created record.
        """
        print('Received POST on resource /book')
        request_body = request.get_json()
        print(request_body)
        book_id = book_checker.create_book(request_body)
        return book_id


@api.route('/<book_id>')
@api.doc(params={'book_id': 'Record of a book.'})
@api.response(200, 'Success')
@api.response(400, 'Invalid input received for book_id')
class BookRecord(Resource):
    @api.marshal_with(book_marshaller, 200)
    def get(self, book_id):
        """
        Gets a specific book record based on book_id.
        :param book_id: Record of a book.
        :return: JSON of requested book record.
        """
        print('Received GET on resource /books/<book_id>')
        if book_id.isdigit():
            a_book = book_checker.get_book(book_id)
            return a_book
        else:
            abort(400, 'Invalid input received for book_id')

    @api.expect(book_marshaller, validate=True)
    @api.marshal_with(book_marshaller, code=200)
    def put(self, book_id):
        """
        Updates an existing record  based on book_id.
        :param book_id: Record number to be updated.
        :return: Book_id of updated record.
        """
        print('Received PUT on resource /books/<book_id>')

        if book_id.isdigit():
            request_body = request.get_json()
            updated_id = book_checker.update_book(book_id, request_body)
            return updated_id
        else:
            abort(400, 'Invalid input received for book_id')

    @api.response(200, 'Deleted')
    @api.marshal_with(book_marshaller, code=200)
    def delete(self, book_id):
        """
        Delete a book record based on book_id.
        :param book_id: Record to be deleted.
        :return: Json of book_id of deleted record.
        """
        #delete_book(book_id)
        return


# Need to decide how to handle this, probably by book name and author.
@api.route('/<book_id>/note')
@api.doc(params={'book_id': 'A record for a book.'})
@api.response(200, 'Success')
@api.response(400, 'Validation Error')
class BookNotes(Resource):

    def get(self, book_id):
        """
        Gets the book note for a specific book.
        :param book_id: Record for a book.
        :return: Note for a specific book.
        """
        if book_id.isdigit():
            note = book_checker.get_note(book_id)
            return note
        else:
            abort(400, 'invalid input for book_id')

    # Need checking here so existing notes aren't written over.
    @api.expect(note, validate=True)
    @api.response(201, 'Created Note')
    @api.marshal_with(book_marshaller, code=201)
    def post(self, book_id):
        """
        Creates a new note for a book.
        :param book_id: Record for a book.
        :return: Note_ID of created note.
        """
        if book_id.isdigit():
            id = book_checker.create_note(book_id, request.get_json())
            return id
        else:
            abort(400, 'Invalid input for book_id')

    @api.expect(note, validate=True)
    @api.marshal_with(book_marshaller, code=200)
    def put(self, book_id):
        """
        Edit a specific note for a book.
        :param book_id: Record for a book.
        :return: Book_id of edited record.
        """
        if book_id.isdigit():
            id = book_checker.edit_note(book_id, request.get_json())
            return id
        else:
            abort(400, 'Invalid input for book_id')

    @api.response(200, 'Deleted Note')
    @api.marshal_with(book_marshaller, code=200)
    def delete(self, book_id):
        """
        Delete a specific note for a book
        :param book_id: Record for a book.
        :return: Book_id of edited record.
        """
        if book_id.isdigit():
            id = book_checker.delete_note(book_id)
            return id
        else:
            abort(400, 'Invalid input for book_id')


@api.route('/<book_id>/copies')
class BookCopies(Resource):

    def get(self, book_id):

        if book_id.isdigit():
            list_of_copies = book_checker.get_copies(book_id)
            return list_of_copies
        else:
            abort(400, 'Invalid input for book_id')

    def post(self, book_id):

        if book_id.isdigit():
            id = book_checker.create_book_copy(book_id)
            return id
        else:
            abort(400, 'Invalid input for book_id')

#
# @api.route('/<book_id>/copies/<book_copy_id>')
# class BookCopy(Resource):
#
#     def get(self, book_id, book_copy_id):
#         if book_id.isdigit() and book_copy_id.isdigit():
#             book_copy = book_checker.get_book_copy(book_id, book_copy_id)
#             return book_copy
#         else:
#             abort(400, 'Invalid input for book_id or book_copy_id')
#
#     def delete(self, book_id, book_copy_id):
#         if book_id.isdigit() and book_copy_id.isdigit():
#             id = book_checker.delete_book_copy(book_id, book_copy_id)
#         else:
#             abort(400, 'Invalid input ofr book_id or book_copy_id')
#
#

