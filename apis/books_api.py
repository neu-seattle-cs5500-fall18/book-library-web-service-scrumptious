from flask import request
from flask_restplus import abort, fields, inputs, Namespace, reqparse, Resource
from controller.author_checker import AuthorChecker
from controller.book_checker import BookChecker
from controller.book_copy_checker import BookCopyChecker
from controller.note_checker import NoteChecker

ns = Namespace('books', description='Book operations')

note_marshaller = ns.model('Note', {
    'note_title': fields.String(required=True, description = 'Unique title of note'),
    'note': fields.String(required=True, description='Note about a book.')
})

return_note_marshaller = ns.inherit('ReturnNote', note_marshaller, {
    'book_id': fields.Integer(description='Book id note is associated with.')
})

amend_note_marshaller = ns.model('AmendNote', {
    'note': fields.String(required=True, description='Text of note to be amended.')
})

author_marshaller = ns.model('Author', {
    'author_id': fields.Integer(required=False, description='Id for an author record'),
    'first_name': fields.String(required=True, description='First name of an author'),
    'last_name': fields.String(required=True, description='Last name of an author'),
    'middle_name': fields.String(required=True, description='Middle name of an author')
})

new_author_marshaller = ns.model('NewAuthor', {
    'first_name': fields.String(required=True, description='First name of an author'),
    'last_name': fields.String(required=True, description='Last name of an author'),
    'middle_name': fields.String(required=True, description='Middle name of an author')
})

book_copies_marshaller = ns.model('BookCopies', {
    'book_copy_id': fields.Integer(required=True, description='Id for a book copy'),
    'book_id': fields.Integer(required=True, description='Id for a book'),
    'is_checked_out' : fields.Boolean(required=True, description= 'Indicates whether a copy of a book is checked out'),
})

book_marshaller = ns.model('Book', {
    'book_id': fields.Integer(required=False, description='The book record'),
    'title': fields.String(required=True, description='The book title.'),
    'publish_date': fields.Date(required=True, description='The publish year of a book.'),
    'subject': fields.String(required=True, description='Subject for a book, such as "science", "Reference", "Non-Fiction"'),
    'genre': fields.String(required=True, description='Genre classification for a fiction book (i.e. horror, science fiction'),
    'notes': fields.List(fields.Nested(note_marshaller), description = 'List of notes for a book'),
    'authors': fields.List(fields.Nested(author_marshaller), required=True, description='List of authors for a book')
})

new_book_marshaller = ns.model('NewBook', {
    'title': fields.String(required=True, description='The book title.'),
    'publish_date': fields.Date(required=True, description='The publish year of a book.'),
    'subject': fields.String(required=True, description='Subject for a book, such as "science", "Reference", "Non-Fiction"'),
    'genre': fields.String(required=True, description='Genre classification for a fiction book (i.e. horror, science fiction'),
    'notes': fields.List(fields.Nested(note_marshaller), description = 'List of notes for a book'),
    'authors': fields.List(fields.Nested(new_author_marshaller), required=True, description='List of authors for a book')
})

full_book_marshaller = ns.inherit('FullBook', book_marshaller, {
    'copies': fields.List(fields.Nested(book_copies_marshaller))
})

edit_book_marshaller = ns.model('EditBook', {
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


@ns.route('', endpoint='books')
@ns.response(400, 'Validation Error')
class Books(Resource):
    @ns.doc(body=query_parser, validate=True)
    @ns.response(200, 'Success')
    @ns.marshal_with(book_marshaller, code=200)
    def get(self):
        """
        Queries the books resource based on URL query string parameters. Valid query arguments are:
        title, first_name, last_name, middle_name, publish_date_start, publish_date_end, subject, genre.
        If no query string is provided all books are returned.
        :return: JSON List of books that match query parameters, in the format according to the book_marshaller.
        """
        print('Received GET on resource /books')
        args = query_parser.parse_args()
        list_of_books = BookChecker.get_books(args)
        return list_of_books, 200


    @ns.response(201, 'Created')
    @ns.expect(new_book_marshaller, validate=True)
    @ns.marshal_with(full_book_marshaller, code=201)
    def post(self):
        """
        Creates a new book record for a single book.
        :return: JSON of the created Book record in the format specified by the full_book_marshaller.
        """
        print('Received POST on resource /book')
        request_body = request.get_json()
        a_book = BookChecker.create_book(request_body)
        return a_book, 201


@ns.route('/<book_id>')
@ns.doc(params={'book_id': 'Record of a book.'})
@ns.response(200, 'Success')
@ns.response(400, 'Invalid input received for book_id')
@ns.response(404, 'Resource Not Found')
class BookRecord(Resource):
    @ns.marshal_with(full_book_marshaller, 200)
    def get(self, book_id):
        """
        Gets a specific book record based on book_id.
        :param book_id: Record of a book.
        :return: JSON of requested book record according to model full_book_marshaller.
        """
        print('Received GET on resource /books/<book_id>')
        if book_id.isdigit():
            a_book = BookChecker.get_book(book_id)
            return a_book, 200
        else:
            abort(400, 'Invalid input received for book_id')

    @ns.expect(edit_book_marshaller, validate=True)
    @ns.marshal_with(book_marshaller, code=200)
    def put(self, book_id):
        """
        Updates an existing Book record based on book_id and JSON. The edit_book_marshaller model holds the fields that
        are valid to include within the json of the put request.
        :param book_id: Book record to be updated.
        :return: JSON of updated book record according to book_marshaller model.
        """
        print('Received PUT on resource /books/<book_id>')
        if book_id.isdigit():
            request_body = request.get_json()
            book = BookChecker.update_book(book_id, request_body)
            return book, 200
        else:
            abort(400, 'Invalid input received for book_id')

    @ns.response(204, 'Deleted')
    @ns.marshal_with(book_marshaller, code=204)
    def delete(self, book_id):
        """
        Delete a book record based on book_id.
        :param book_id: Record to be deleted.
        :return: null.
        """
        print('Received DELETE on resource /books/<book_id>')
        if book_id.isdigit():
            result = BookChecker.delete_book(book_id)
            return result, 204
        else:
            abort(400, 'Invalid input received for book_id')


@ns.route('/<book_id>/notes')
@ns.doc(params={'book_id': 'A record for a book.'})
@ns.response(200, 'Success')
@ns.response(400, 'Invalid input for book_id')
@ns.response(404, 'Resource Not Found')
class BookNotes(Resource):
    def get(self, book_id):
        """
        Gets the book notes for a specific book.
        :param book_id: Record of book.
        :return: JSON List of notes for a specific book.
        """
        print('Received GET on resource /books/<book_id>/notes')
        if book_id.isdigit():
            list_notes = NoteChecker.get_notes(book_id)
            return list_notes, 200
        else:
            abort(400, 'Invalid input for book_id')

    @ns.expect(note_marshaller, validate=True)
    @ns.response(201, 'Created Note')
    @ns.marshal_with(return_note_marshaller, code=201)
    def post(self, book_id):
        """
        Creates a new note for a book.
        :param book_id: Record for a book.
        :return: JSON of created note according to return_note_marshaller model.
        """
        print('Received POST on resource /books/<book_id>/notes')
        if book_id.isdigit():
            note = NoteChecker.create_note(book_id, request.get_json())
            return note, 201
        else:
            abort(400, 'Invalid input for book_id')


@ns.route('/<book_id>/notes/<note_title>')
@ns.doc(params={'book_id': 'A record for a book.','note_title': 'Title of a note in the book.'})
@ns.response(200, 'Success')
@ns.response(400, 'Invalid input for book_id')
@ns.response(404, 'Resource not found')
class BookNotes(Resource):
    @ns.expect(amend_note_marshaller, validate=True)
    @ns.marshal_with(return_note_marshaller, code=200)
    def put(self, book_id, note_title):
        """
        Edit a specific note for a book. Valid input for JSON are fields in the amend_note_marshaller model.
        :param book_id: Record for a book.
        :param note_title: Record for a note.
        :return: JSON of note according to return_note_marshaller.
        """
        print('Received PUT on resource /books/<book_id>/notes/<note_title>')
        if book_id.isdigit():
            note = NoteChecker.update_note(book_id,note_title, request.get_json())
            return note, 200
        else:
            abort(400, 'Invalid input for book_id')

    @ns.response(204, 'Deleted')
    @ns.marshal_with(return_note_marshaller, code=204)
    def delete(self, book_id, note_title):
        """
        Delete a specific note for a book.
        :param book_id: Record for a book.
        :param note_title: Record for a note.
        :return: null.
        """
        print('Received DELETE on resource /books/<book_id>/notes/<note_title>')
        if book_id.isdigit():
            result = NoteChecker.delete_note(book_id, note_title)
            return result, 204
        else:
            abort(400, 'Invalid input for book_id')


@ns.route('/<book_id>/copies')
@ns.response(200, 'Success')
@ns.response(201, 'Created')
@ns.response(400, 'Invalid input for book_id')
@ns.response(404, 'Resource not found book_id')
@ns.doc(params={'book_id': 'A record for a book.'})
class BookCopies(Resource):
    def get(self, book_id):
        """
        Gets the copies of a given book.
        :param book_id: Record of a book.
        :return: JSON of a list of book copies according to list_copies_marshaller model.
        """
        print('Received GET on resource /books/<book_id>/copies')
        if book_id.isdigit():
            list_of_copies = BookCopyChecker.get_copies(book_id)
            print(list_of_copies)
            return list_of_copies, 200
        else:
            abort(400, 'Invalid input for book_id')

    @ns.marshal_with(book_copies_marshaller, code=201)
    def post(self, book_id):
        """
        Create a new copy for an existing book.
        :param book_id: Record of a book.
        :return: JSON of a books copies according to book_copies_marshaller.
        """
        print('Received POST on resource /books/<book_id>/copies')
        if book_id.isdigit():
            book = BookCopyChecker.create_copy(book_id)
            return book, 201
        else:
            abort(400, 'Invalid input for book_id')


@ns.route('/<book_id>/authors')
@ns.response(201, 'Created')
@ns.response(400, 'Invalid input for book_id')
@ns.response(404, 'Resource not found: book_id')
@ns.doc(params={'book_id': 'A record for a book.'})
class BookAuthors(Resource):
    @ns.expect(new_author_marshaller, validate=True)
    @ns.marshal_with(author_marshaller, code=201)
    def post(self, book_id):
        """
        Adds new author to an existing book, given a JSON of author attributes according to author_marshaller.
        :param book_id: Record of a book.
        :return: JSON of new author according to author_marshaller model.
        """
        print('Received POST on resource /books/<book_id>/authors')
        if book_id.isdigit():
            author_json = request.get_json()
            author = AuthorChecker.create_author(book_id, author_json)
            return author, 201
        else:
            abort(400, 'Invalid input for book_id')


@ns.route('/<book_id>/authors/<author_id>')
@ns.response(200, 'Success')
@ns.response(400, 'Invalid input for url parameters book_id and/or author_id')
@ns.response(404, 'Resource not found')
@ns.doc(params={'book_id': 'A record for a book.','author_id': 'Id of an Author record.'})
class BookAuthor(Resource):
    @ns.marshal_with(author_marshaller, code=200)
    def put(self, book_id, author_id):
        """
        Edits an existing Author record.
        :param book_id: Record of a Book.
        :param author_id: Record of an Author
        :return: JSON of author record according to author_marshaller model.
        """
        print('Received PUT on resource /books/<book_id>/authors/<author_id>')
        if book_id.isdigit() and author_id.isdigit():
            author_json = request.get_json()
            result = AuthorChecker.update_author(book_id, author_id, author_json)
            return result, 200
        else:
            abort(400, 'Invalid input for url parameters book_id and/or author_id')

