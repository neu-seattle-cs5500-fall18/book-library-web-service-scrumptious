from flask import Flask
from flask_restplus import Api, fields, Resource, reqparse

app = Flask(__name__)
api = Api(app)

ns = api.namespace('books', description='Operations involving books resource')

# Need Parameter Checking, where to store valid parameters, error list.
# restplus automatically returns json object type.
# cann annotate fields with readable info
# response model, any other fields are considered private and not returned
book_model = api.model('BookModel', {
    'book_id': fields.Integer(required=True, description='The book record'),
    'title': fields.String(description='The book title.'),
    'author_first_name': fields.String(description='The author\'s first name.'),
    'author_last_name': fields.String(description='The author\'s last name.'),
    # Author needs updateed to accomodate several authors
    'publish_date': fields.DateTime(description='The publish date of a book'),
    'subject': fields.String(description='Subject, such as "science", "Reference", "Non-Fiction"'),
    'genre': fields.String(description='Genre classification for a fiction book (i.e. horror, science fiction'),
    'loaned_out': fields.Boolean(description='Indicates if a book is on loan true, false otherwise'),
    #nested json object?
    'notes': fields.List(fields.String, description='List of personal notes about a book'),
    'collections': fields.List(fields.Integer, descritpiont='List of collections book belongs to')
})

query_parser = reqparse.RequestParser()
query_parser.add_argument('title', required=False)
query_parser.add_argument('author_first_name', required=False)
query_parser.add_argument('author_last_name', required=False)
query_parser.add_argument('publish_date', action='append', required=False)
query_parser.add_argument('subject', action='append', required=False)
query_parser.add_argument('genre', action='append', required=False)
query_parser.add_argument('loaned_out', required=False)


class Book(object):
    def __init__(self, book_id, title, author_first_name, author_last_name, publish_date, subject, genre, loaned_out,
                 notes, collections):
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

        self.status = 'active'


@ns.route('/', endpoint='books')
class Books(Resource):
    # this ensures arguments are valid and get can receive query params.
    @api.expect(query_parser, validate=True)
    # this generates json object based on same fields specified in model
    @api.marshal_with(book_model, code=200, description='Successful query.')
    def get(self):
        """
        Queries the books resource based on URL query string parameters.
        :return: Json object of all books that match query parameters. If parameters are empty, all books are returned.
        """
        return "got a book"

    @api.expect(book_model)
    @api.response(400, 'Validation error')
    def post(self):
        """
        Creates a new book record for a single book.
        :return: JSON of ID of the created record.
        """
        books = [self]

        # Query routing function here
        # set response code 201
        return "Successfully Created ID " + books.pop()


@ns.route('/<book_id>')
@api.doc(params={'book_id': 'Record identifier for a book'})
class BookRecord(Resource):
    def get(self, book_id):
        """
        Gets a specific book record based on book_id.
        :param book_id: Record of a book.
        :return: JSON of requested book record.
        """
        return "Successfully got %s " % book_id

    @api.expect(book_model)
    @api.response(code=404, description="Incorrect record")
    @api.marshal_with(book_model, code='200', description='Object amended')
    def put(self, book_id):
        """
        Updates an existing record  based on book_id.
        :param book_id: Record number to be updated.
        :return: Json with book_id of updated record.
        """
        return "Successfully updated %s " % book_id

    @api.response(code=200, description='Objected deleted')
    @api.response(code=404, description="No such record")
    def delete(self, book_id):
        """
        Delete a book record based on book_id.
        :param book_id: Record to be deleted.
        :return: Json of book_id of deleted record.
        """
        return "Successfully deleted %s " % book_id


# will need to update this to account for multiple copies of a book.
@ns.route('/<book_id>/notes')
@api.doc(params={'book_id': 'A record for a book'})
class BookNotes(Resource):
    @api.response(code=200, description='Record gotten')
    @api.response(code=404, description='No such record')
    def get(self, book_id):
        """
        Get the book notes for a specific book
        :param book_id: Record for a book
        :return: Json of the book notes for a book.
        """
        return "Successfully retrieved notes for %s" % book_id

    def post(self,book_id):
        """
        Create new note for a book
        :param book_id: Record for a book.
        :return: Note_ID of created note.
        """

        return "Successfully edited note for %s" % book_id


@ns.route('/<book_id>/notes')
@api.doc(params={'book_id': 'A record for a book.'})
class BookNotes(Resource):
    def get(self, book_id):
        """
        Gets all notes for a given book.
        :param book_id: Record for a book.
        :return: Josn of list of book notes.
        """
        return "Got list of book notes"

    #@marshall resources
    def post(self,book_id):
        """
        Creates new note for a book.
        :param book_id:  Record for a book.
        :return: Json of created book note id.
        """

@ns.route('/<book_id>/notes/<note_id>')
@api.doc(params={'book_id': 'A record for a book', 'note_id': 'A record for a note about a book'})
class Note(Resource):
    def get(self, book_id, note_id):
        """
        Get specific note for a given book.
        :param book_id: Record for a book.
        :param note_id: Record for a book note.
        :return: Json of note for a book.
        """
        return "Successfully requested notes"

    #@marshalresource
    def put(self, book_id, note_id):
        """
        Edit a specific note for a book.
        :param book_id: Record for a book.
        :param note_id: Record for a book note.
        :return: Json of Note_ID for edited note.
        """
        return " Edited Note ID: "

    def delete(self, book_id, note_id):
        """
        Delete a specific note for a book
        :param book_id: Record for a book.
        :param note_id: Record for a book note.
        :return: Json of Note_ID for deleted note.
        """
        return "Deleted book note"


# probably break this out into its own class.

@ns.route('/<book_id>/collections')
@api.doc(parameters={'book_id': 'Record for a book'})
class BookCollections(Resource):
    def get(self, book_id):
        """
        Gets a list of the collections a book belongs to.
        :param book_id: Record for a book.
        :return: Json list of the collections a book is part of.
        """
        return "List of collections"

@ns.route('/<book_id>/collections/<collection_id>')
@api.doc(parameters={'book_id': 'Record for a book', 'collection_id': 'Record for a collection'})
class Collection(Resource):
    def post(self, book_id, collection_id):
        """
        Add collection to book.
        :param book_id: Record for a book.
        :param collection_id: Record for a collection
        :return: ID of newly added collection?
        """
        return

    def delete(self,book_id,collection_id):
        """
        Removes a collection from book.
        :param book_id: Record for a book.
        :param collection_id: Record for a collection.
        :return: ID of deleted collection record.
        """


if __name__ == '__main__':
    app.run(debug=True)
