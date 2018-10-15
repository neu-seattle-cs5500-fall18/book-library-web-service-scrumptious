from flask import request
from flask_restplus import Namespace, fields, Resource, reqparse

api = Namespace('books', description='Book operations')

# Response model, any other fields are considered private and not returned
# Need to double check that this is the best perhaps hide some
book = api.model('Book', {
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

note = api.model('Note', {
    'notes': fields.String(required=True, description='Note about a book.')
})

query_parser = reqparse.RequestParser()
query_parser.add_argument('title', required=False)
query_parser.add_argument('author_first_name', required=False)
query_parser.add_argument('author_last_name', required=False)
query_parser.add_argument('publish_date', action='append', required=False)
query_parser.add_argument('subject', action='append', required=False)
query_parser.add_argument('genre', action='append', required=False)
query_parser.add_argument('is_deleted', default=False)


class Book(object):
    def __init__(self, book_id, title, author_first_name, author_last_name, publish_date, subject, genre, loaned_out,
                 notes, collections, is_deleted):
        self.book_id = book_id
        self.title = title
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.publish_date = publish_date
        self.subject = subject
        self.genre = genre
        self.loaned_out = loaned_out
        self.notes = notes
        self.collections = collections
        self.is_deleted = is_deleted

        self.status = 'active'


library = []
book1 = Book('0','The Great Gatsby', 'Frances Scott', 'Fitzgerald', '1930-07-15', 'Fiction', 'Novel', False,
             'A book about a Young Millionaire', [1], False)
book2 = Book('1','1984','George', 'Orwell', '1949-07-08', 'Fiction', 'Novel', False, 'A love story', [4,1], False)
book3 = Book('2','Software Engineering, 10th Edition', 'Ian', 'Sommerville', '2004-05-06', 'Reference', 'None', False, 'Reference for software engineering', [3,8,4], False)
book4 = Book('4','Animal Farm','George', 'Orwell', '1952-10-16', 'Fiction', 'Novel', False, 'Really enjoyed the pigs',
             [4,1], False)
book5 = Book('4','Burma Days','George', 'Orwell', '1960-06-08', 'Fiction', 'Novel', False, '',
             [4,2], False)


@api.route('/', endpoint='books')
@api.response(code=400, description='Validation Error')
class Books(Resource):
    # this ensures arguments are valid and get can receive appropriate query params.
    @api.doc(body=query_parser, validate=True)
    # this generates json object based on same fields specified in model
    @api.marshal_with(book, code=200, description='Success')
    def get(self):
        """
        Queries the books resource based on URL query string parameters.
        :return: Json object of all books that match query parameters. If parameters are empty, all books are returned.
        """
        library.append(book1)
        library.append(book2)
        library.append(book3)

        return library

    # This ensures body of request matches book model
    @api.doc(body=book, validate=True)
    @api.marshal_with(book, code=201, description='Success')
    def post(self):
        """
        Creates a new book record for a single book.
        :return: Book ID of the created record.
        """
        new_book = request.json
        library.append(book1)
        library.append(book2)
        library.append(new_book)
        return library


@api.route('/<book_id>')
@api.doc(params={'book_id': 'Record of a book.'})
@api.response(code=400, description='Validation error')
class BookRecord(Resource):
    @api.marshal_with(book, code=200, description='Success')
    def get(self, book_id):
        """
        Gets a specific book record based on book_id.
        :param book_id: Record of a book.
        :return: JSON of requested book record.
        """
        library.append(book1)
        library.append(book2)
        library.append(book3)
        for element in library:
            if element.book_id == book_id:
                return element

    @api.doc(body=book, validate=True)
    @api.response(code=200, description='Success')
    def put(self, book_id):
        """
        Updates an existing record  based on book_id.
        :param book_id: Record number to be updated.
        :return: Json with book_id of updated record.
        """

        return "Successfully updated %s " % book_id

    @api.marshal_with(book, code=200, description='Book deleted')
    def delete(self, book_id):
        """
        Delete a book record based on book_id.
        :param book_id: Record to be deleted.
        :return: Json of book_id of deleted record.
        """
        library.append(book1)
        library.append(book2)
        library.append(book3)

        for element in library:
            if element.book_id == book_id:
                element.is_deleted = True
                return element


@api.route('/<book_id>/notes')
@api.doc(params={'book_id': 'A record for a book.'})
@api.response(code=400, description='Validation Error')
class BookNotes(Resource):
    @api.response(code=200, description='Success')
    def get(self, book_id):
        """
        Gets all the book notes for a specific book.
        :param book_id: Record for a book.
        :return: Notes for a specific book.
        """
        library.append(book1)
        library.append(book2)
        library.append(book3)

        for element in library:
            if element.book_id == book_id:
                return element.notes


    # Need checking here so existing notes aren't written over.
    @api.doc(body=note, code=200, description = 'Success')
    @api.marshal_with(book, code=201, description='Created')
    def post(self, book_id):
        """
        Creates a new note for a book.
        :param book_id: Record for a book.
        :return: Note_ID of created note.
        """
        library.append(book1)
        library.append(book2)
        library.append(book3)
        library.append(book4)
        library.append(book5)

        received_record = request.json

        for element in library:
            if element.book_id == book_id:
                element.notes = received_record.get('notes')
                return element

    @api.doc(body=note, code=200, description='Success')
    @api.marshal_with(book, code=200, description='Success')
    def put(self, book_id):
        """
        Edit a specific note for a book.
        :param book_id: Record for a book.
        :return: Book_id of edited record.
        """

        library.append(book1)
        library.append(book2)

        received = request.json

        for element in library:
            if element.book_id == book_id:
                element.notes = received.get('notes')
        return element

    @api.doc(code=200, description="Deleted")
    @api.marshal_with(book, code=200, description='Deleted')
    def delete(self, book_id):
        """
        Delete a specific note for a book
        :param book_id: Record for a book.
        :return: Book_id of edited record.
        """
        library.append(book1)
        library.append(book2)
        library.append(book3)

        for element in library:
            if element.book_id == book_id:
                element.notes = ""
                return element


@api.route('/<book_id>/collections')
@api.doc(parameters={'book_id': 'Record for a book'})
class BookCollections(Resource):
    def get(self, book_id):
        """
        Gets a list of the collections a book belongs to.
        :param book_id: Record for a book.
        :return: Json list of the collections a book is part of.
        """

        library.append(book1)
        library.append(book2)
        library.append(book3)

        for element in library:
            if element.book_id == book_id:
                return element.collections



