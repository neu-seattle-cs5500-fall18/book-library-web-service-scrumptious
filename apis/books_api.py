from flask import request
from flask_restplus import Namespace, fields, Resource, reqparse
from model.book_marshaller import BookMarshaller

api = Namespace('books', description='Book operations')

note = api.model('Note', {
    'notes': fields.String(required=True, description='Note about a book.')
})


# Response model, any other fields are considered private and not returned
book_marshaller = api.model('Book', {
    'book_id': fields.Integer(required=True, description='The book record'),
    'title': fields.String(description='The book title.'),
    'author_first_name': fields.String(description='The author\'s first name.'),
    'author_last_name': fields.String(description='The author\'s last name.'),
    'publish_date': fields.Date(description='The publish date of a book.'),
    'subject': fields.String(description='Subject for a book, such as "science", "Reference", "Non-Fiction"'),
    'genre': fields.String(description='Genre classification for a fiction book (i.e. horror, science fiction'),
    'loaned_out': fields.Boolean(description='Indicates if a book is on loan true, false otherwise.'),
    'notes': fields.String(description='Personal notes about a book.'),
    'collections': fields.List(fields.Integer, descritpion='List of Collections a book belongs to.'),
    'is_deleted': fields.Boolean(description='Field to indicate of a book is deleted or not, for soft delete.')
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
        print('working')
        #get_all_books()
        return 'this worked'

    # This ensures body of request matches book model
    @api.expect(book_marshaller, validate=True)
    @api.response(201, 'Created')
    @api.marshal_with(book_marshaller, code=201)
    def post(self):
        """
        Creates a new book record for a single book.
        :return: Book ID of the created record.
        """
        print('posting')
        #create_new_book(json)
        return 'post worked'


@api.route('/<book_id>')
@api.doc(params={'book_id': 'Record of a book.'})
@api.response(200, 'Success')
@api.response(400, 'Validation error')
class BookRecord(Resource):
    @api.marshal_with(book_marshaller, code=200)
    def get(self, book_id):
        """
        Gets a specific book record based on book_id.
        :param book_id: Record of a book.
        :return: JSON of requested book record.
        """
        #get_book(book_id)
        return

    @api.expect(book_marshaller, validate=True)
    @api.marshal_with(book_marshaller, code=200)
    def put(self, book_id):
        """
        Updates an existing record  based on book_id.
        :param book_id: Record number to be updated.
        :return: Book_id of updated record.
        """
        #update_book(book_id, json)
        return

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


@api.route('/<book_id>/notes')
@api.doc(params={'book_id': 'A record for a book.'})
@api.response(200, 'Success')
@api.response(400, 'Validation Error')
class BookNotes(Resource):

    def get(self, book_id):
        """
        Gets all the book notes for a specific book.
        :param book_id: Record for a book.
        :return: Notes for a specific book.
        """
        #get_notes(book_id)
        return

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
        #create_note(book_id, json)
        return

    @api.expect(note, validate=True)
    @api.marshal_with(book_marshaller, code=200)
    def put(self, book_id):
        """
        Edit a specific note for a book.
        :param book_id: Record for a book.
        :return: Book_id of edited record.
        """
        #edit_note(book_id, json)
        return

    @api.response(200, 'Deleted Note')
    @api.marshal_with(book_marshaller, code=200)
    def delete(self, book_id):
        """
        Delete a specific note for a book
        :param book_id: Record for a book.
        :return: Book_id of edited record.
        """
        #delete_note(book_id)
        return


@api.route('/<book_id>/collections')
@api.doc(parameters={'book_id': 'Record for a book'})
@api.response(200, 'Success')
@api.response(400, 'Invalid input')
class BookCollections(Resource):

    def get(self, book_id):
        """
        Gets a list of the collections a book belongs to.
        :param book_id: Record for a book.
        :return: Json list of the collections a book is part of.
        """
        #get_collections(book_id)
        return



