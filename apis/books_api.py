from flask import request
from flask_restplus import abort, fields, inputs, Namespace, reqparse, Resource
from controller.author_checker import AuthorChecker
from controller.book_checker import BookChecker
from controller.book_copy_checker import BookCopyChecker
from controller.note_checker import NoteChecker

api = Namespace('books', description='Book operations')


note_marshaller = api.model('Note', {
    'note_title': fields.String(required=True, description = 'Unique title of note'),
    'note': fields.String(required=True, description='Note about a book.')
})

return_note_marshaller = api.inherit('ReturnNote', note_marshaller, {
    'book_id': fields.Integer(description='Book id note is associated with.')
})

list_notes_marshaller = api.model('ListOfNotes', {
    'notes' : fields.List(fields.Nested(note_marshaller))
})

author_marshaller = api.model('Author', {
    'author_id': fields.Integer(required=False, description='Id for an author record'),
    'first_name': fields.String(required=True, description='First name of an author'),
    'last_name': fields.String(required=True, description='Last name of an author'),
    'middle_name': fields.String(required=True, description='Middle name of an author')
})

book_copies_marshaller = api.model('BookCopies', {
    'book_copy_id': fields.Integer(required=True, description='Id for a book copy'),
    'book_id': fields.Integer(required=True, description='Id for a book'),
    'is_checked_out' : fields.Boolean(required=True, description= 'Indicates whether a copy of a book is checked out'),
})

list_copies_marshaller = api.model('ListBooksMarshaller', {
    'copies': fields.List(fields.Nested(book_copies_marshaller))
})


# Response model, any other fields are considered private and not returned
book_marshaller = api.model('Book', {
    'book_id': fields.Integer(required=False, description='The book record'),
    'title': fields.String(required=True, description='The book title.'),
    'publish_date': fields.Date(required=True, description='The publish date of a book.'),
    'subject': fields.String(required=True, description='Subject for a book, such as "science", "Reference", "Non-Fiction"'),
    'genre': fields.String(required=True, description='Genre classification for a fiction book (i.e. horror, science fiction'),
    'notes': fields.List(fields.Nested(note_marshaller), description = 'List of notes for a book'),
    'authors': fields.List(fields.Nested(author_marshaller), required=True, description='List of authors for a book')
})

full_book_marshaller = api.inherit('FullBook', book_marshaller, {
    'copies': fields.List(fields.Nested(book_copies_marshaller))
})

edit_book_marshaller = api.model('EditBook', {
    'title': fields.String(required=False, description='The book title.'),
    'publish_date': fields.Date(required=False, description='The publish date of a book.'),
    'subject': fields.String(required=False,
                             description='Subject for a book, such as "science", "Reference", "Non-Fiction"'),
    'genre': fields.String(required=False,
                           description='Genre classification for a fiction book (i.e. horror, science fiction'),

})

query_parser = reqparse.RequestParser()
query_parser.add_argument('title', type=str, required=False)
query_parser.add_argument('first_name', type=str, required=False)
query_parser.add_argument('last_name', type=str, required=False)
query_parser.add_argument('middle_name', type=str, required=False)
query_parser.add_argument('publish_date_start', type=inputs.date, required=False)
query_parser.add_argument('publish_date_end', type=inputs.date, required=False)
query_parser.add_argument('subject', type=str, required=False)
query_parser.add_argument('genre', type=str, required=False)


@api.route('', endpoint='books')
@api.response(200, 'Success')
@api.response(400, 'Validation Error')
class Books(Resource):
    @api.doc(body=query_parser, validate=True)
    @api.marshal_with(book_marshaller, code=200)
    def get(self):
        """
        Queries the books resource based on URL query string parameters.
        :return: List of all books that match query parameters. If no query string is provided, all books are returned.
        """
        print('Received GET on resource /books')
        args = query_parser.parse_args()
        list_of_books = BookChecker.get_books(args)
        return list_of_books

    @api.expect(book_marshaller, validate=True)
    @api.response(201, 'Created')
    @api.marshal_with(full_book_marshaller, 201)
    def post(self):
        """
        Creates a new book record for a single book.
        :return: Book of the created record.
        """
        print('Received POST on resource /book')
        request_body = request.get_json()
        a_book = BookChecker.create_book(request_body)
        return a_book


@api.route('/<book_id>')
@api.doc(params={'book_id': 'Record of a book.'})
@api.response(200, 'Success')
@api.response(400, 'Invalid input received for book_id')
class BookRecord(Resource):
    @api.marshal_with(full_book_marshaller, 200)
    def get(self, book_id):
        """
        Gets a specific book record based on book_id.
        :param book_id: Record of a book.
        :return: JSON of requested book record.
        """
        print('Received GET on resource /books/<book_id>')
        if book_id.isdigit():
            a_book = BookChecker.get_book(book_id)
            return a_book
        else:
            abort(400, 'Invalid input received for book_id')

    @api.expect(edit_book_marshaller, validate=True)
    @api.marshal_with(book_marshaller, code=200)
    def put(self, book_id):
        """
        Updates an existing record  based on book_id, and according to fields fo the edit_book_marshaller model.
        :param book_id: Record number to be updated.
        :return: Book_id of updated record.
        """
        print('Received PUT on resource /books/<book_id>')
        if book_id.isdigit():
            request_body = request.get_json()
            book = BookChecker.update_book(book_id, request_body)
            return book
        else:
            abort(400, 'Invalid input received for book_id')

    @api.response(200, 'Deleted')
    @api.marshal_with(book_marshaller, code=200)
    def delete(self, book_id):
        """
        Delete a book record based on book_id.
        :param book_id: Record to be deleted.
        :return:
        """
        print('Received DELETE on resource /books/<book_id>')
        if book_id.isdigit():
            result = BookChecker.delete_book(book_id)
            return result
        else:
            abort(400)


@api.route('/<book_id>/notes')
@api.doc(params={'book_id': 'A record for a book.'})
@api.response(200, 'Success')
@api.response(400, 'Validation Error')
class BookNotes(Resource):
    @api.marshal_with(list_notes_marshaller, code=200)
    def get(self, book_id):
        """
        Gets the book notes for a specific book.
        :param book_id: Record for a book.
        :return: List of notes for a specific book.
        """
        print('Received GET on resource /books/<book_id>/notes')
        if book_id.isdigit():
            list_notes = NoteChecker.get_notes(book_id)
            return list_notes
        else:
            abort(400, 'invalid input for book_id')

    @api.expect(note_marshaller, validate=True)
    @api.response(201, 'Created Note')
    @api.marshal_with(return_note_marshaller, code=201)
    def post(self, book_id):
        """
        Creates a new note for a book.
        :param book_id: Record for a book.
        :return: Note_ID of created note.
        """
        print('Received POST on resource /books/<book_id>/notes')
        if book_id.isdigit():
            note = NoteChecker.create_note(book_id, request.get_json())
            return note
        else:
            abort(400, 'Invalid input for book_id')


@api.route('/<book_id>/notes/<note_title>')
@api.doc(params={'book_id': 'A record for a book.','note_title': 'Title of a note in the book.'})
@api.response(200, 'Success')
@api.response(400, 'Validation Error')
class BookNotes(Resource):
    @api.expect(note_marshaller, validate=True)
    @api.marshal_with(return_note_marshaller, code=200)
    def put(self, book_id, note_title):
        """
        Edit a specific note for a book.
        :param book_id: Record for a book.
        :return: Book_id of edited record.
        """
        print('Recieved PUT on resource /books/<book_id>/notes/<note_title>')
        if book_id.isdigit():
            note = NoteChecker.update_note(book_id, request.get_json())
            return note
        else:
            abort(400, 'Invalid input for book_id')

    @api.response(200, 'Deleted Note')
    def delete(self, book_id, note_title):
        """
        Delete a specific note for a book
        :param book_id: Record for a book.
        :return: Book_id of edited record.
        """
        print('Received DELETE on resource /books/<book_id>/notes/<note_title>')
        if book_id.isdigit():
            result = NoteChecker.delete_note(book_id)
            return result
        else:
            abort(400, 'Invalid input for book_id')


@api.route('/<book_id>/copies')
class BookCopies(Resource):
    @api.marshal_with(list_copies_marshaller)
    def get(self, book_id):
        print('Received GET on resource /books/<book_id>/copies')
        if book_id.isdigit():
            list_of_copies = BookCopyChecker.get_copies(book_id)
            return list_of_copies
        else:
            abort(400, 'Invalid input for book_id')

    @api.marshal_with(book_copies_marshaller)
    def post(self, book_id):
        print('Received POST on resource /books/<book_id>/copies')
        if book_id.isdigit():
            book = BookCopyChecker.create_copy(book_id)
            return book
        else:
            abort(400, 'Invalid input for book_id')


@api.route('/<book_id>/authors')
class BookAuthors(Resource):
    @api.expect(author_marshaller, validate=True)
    @api.marshal_with(author_marshaller)
    def post(self, book_id):
        """
        adds new author to an existing book.
        :param book_id:
        :return:
        """
        print('Received POST on resource /books/<book_id>/authors')
        if book_id.isdigit():
            author_json = request.get_json()
            author = AuthorChecker.create_author(book_id, author_json)
            return author
        else:
            abort(400)


@api.route('/<book_id>/authors/<author_id>')
class BookAuthor(Resource):
    @api.marshal_with(author_marshaller)
    def put(self, book_id, author_id):
        """
        adds existing author to book.
        :param book_id:
        :param author_id:
        :return:
        """
        print('Received PUT on resource /books/<book_id>/authors/<author_id>')
        if book_id.isdigit() and author_id.isdigit():
            result = AuthorChecker.add_book_to_author(book_id, author_id)
            return result
        else:
            abort(400)

    def delete(self, book_id, author_id):
        """
        deletes an author from a book.
        :param book_id:
        :param author_id:
        :return:
        """
        print('Received DELETE on resource /books/<book_id>/authors/<author_id>')
        if book_id.isdigit() and author_id.isdigit():
            result = AuthorChecker.delete_author_from_book(book_id, author_id)
            return result
        else:
            abort(400)



