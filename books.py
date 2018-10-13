from flask import Flask
from flask_restplus import Api, fields, Resource, reqparse

from books_queries import query_book_params

app = Flask(__name__)
api = Api(app)


# Need Parameter Checking, where to store valid parameters, error list.
# restplus automatically returns json object type.
# cann annotate fields with readable info
# response model, any other fields are considered private and not returned
book_model = api.model('BookModel', {
    'book_id': fields.Integer('The book record'),
    'title': fields.String('The book title.'),
    'author_first_name': fields.String('The author\'s first name.'),
    'author_last_name': fields.String('The author\'s last name.'),
    #Author needs updateed to accomodate several authors
    'publish_date': fields.String('The publish date of a book'),
    'subject': fields.String('Subject, such as "science", "Reference", "Non-Fiction"'),
    'genre': fields.String('Genre classification for a fiction book (i.e. horror, science fiction'),
    'loaned_out': bool('If a book is on loan true, false otherwise'),
    'notes': list('List of personal notes about a book'),
    'collections': list('List of collections book belongs to')
})

query_parser = reqparse.RequestParser()
query_parser.add_argument('title', 'author_first_name', 'author_last_name', 'publish_date', 'subject', 'genre')


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


@api.route('/books', endpoint='books')
class Books(Resource):
    @api.response(400, 'Invalid query')
    @api.response(200, 'Resource gotten')
    #parser = api.parser()
    #parser.add_argument()

    def get(self):
        """
        Gets all books within resource Books.
        :return: Json object of all books within Resource Books.
        """
        books = []
        book = Book(
            4, "The Old Man and the Sea", "George r.r.", "Martin"
        )
        books.append(book)
        args = query_parser.parse_args()
        result = query_book_params(args)
        return books



    @api.response(400, 'Validation error')
    @api.marshal_with(book_model, code=201, description='Object created')
    def post(self):
        """
        Creates a new book record for a single book.
        :return: JSON of created record.
        """
        books = []
        books.append(self)

        # Query routing function here
        # set response code 201
        return "Successfully Created ID " + books.pop()


@api.route('/books/<book_id>', endpoint='books', doc = {'params':{'book_id': 'Record identifier for a book'}})
class BookRecord(Resource):
    @api.response(404, 'Incorrect record ')
    @api.response(200, 'Resource gotten')
    def get(self, book_id):
        """
        Gets a specific book record based on book_id.
        :param book_id: Record of a book.
        :return: JSON of requested book record.
        """
        return "Successfully got %s " %book_id

    @api.response(404, "Incorrect record")
    @api.marshal_with(book_model, code='200', description='Object amended')
    def put(self, book_id):
        """
        Updates an existing record  based on book_id.
        :param book_id: Record number to be updated.
        :return: Json with book_id of updated record.
        """
        return "Successfully updated %s " %book_id

    @api.response(200, 'Objected deleted')
    @api.response(404, "No such record")
    def delete(self, book_id):
        """
        Delete a book record based on book_id.
        :param book_id: Record to be deleted.
        :return: Json of book_id of deleted record.
        """
        return "Successfully deleted %s " %book_id


@api.route('/books/notes', endpoint='books')
@api.doc(params={'book_id': 'A record for a book'})
class BookNotes(Resource):
        def get(self):
            return



@api.route('/books/collections', endpoint='books')
@api.doc(params={'epoch_start': 'Earliest publish date', 'epoch_end': 'Latest publish date'})
class BookCollections(Resource):
    def get(self, epoch_start, epoch_end):
        """
        Query books by publish date after start date and before end date.
        :param epoch_start: Earliest publish date to query by.
        :param epoch_end: Latest publish date to query by.
        :return: JSON list of books
        """
        # query by start and end dates
        return "Books between" + epoch_start + epoch_end, 200


if __name__ == '__main__':
    app.run(debug=True)
