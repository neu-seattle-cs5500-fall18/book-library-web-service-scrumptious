from flask import Flask
from flask_restplus import Api, fields, Resource

app = Flask(__name__)
api = Api(app)

# restplus automatically returns json object type.
# cann annotate fields with readable info
# response model, any other fields are considered private and not returned
book_model = api.model('BookModel', {
    'book_id': fields.Integer('The book record'),
    'title': fields.String('The book title.'),
    'author_first_name': fields.String('The author\'s first name.'),
    'author_last_name': fields.String('The author\'s last name.'),
})


class BooksDao(object):
    def __init__(self, book_id, title, author_first_name, author_last_name):
        self.book_id = book_id
        self.title = title
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name

        self.status = 'active'


@api.route('/books', endpoint='books')
class Books(Resource):
    @api.marshal_with(book_model)
    @api.response(200, 'Resource successfully gotten')
    # Returns all objects of resource
    def get(self):
        """
        Gets all books within resource Books.
        :return: Json object of all books within Resource Books.
        """
        return "Success", 200

    # Add new record to resource- require json receipt
    # 201 status for created
    @api.expect(book_model)
    @api.response(201, 'Resource created')
    def post(self):
        """
        Creates a new book record.
        :return: JSON of created record.
        """
        # Query routing function here
        # set response code 201
        return "Success", 200


@api.route('/books/<book_id>')
@api.doc(params={'book_id': 'A record for a book'})
class BookRecord(Resource):
    @api.response(404, "Incorrect record")
    def get(self, book_id):
        """
        Gets a specific book record based on book_id.
        :param book_id: Record of a book.
        :return: JSON of record.
        """
        return "success", 200

    @api.marshal_with(book_model)
    @api.response(404, "Incorrect record")
    def put(self, book_id):
        """
        Updates an existing record.
        :param book_id: Record number to be updated.
        :return: Json of updated record.
        """
        return "success again", 200

    @api.response(404, "No such record")
    def delete(self, book_id):
        """
        Delete a book record based on book_id
        :param book_id: Record to be deleted.
        :return:
        """
        return "Successfully Deleted", 200


@api.route('/books/<epoch_start>/<epoch_end>')
@api.doc(params={'epoch_start': 'Earliest publish date', 'epoch_end': 'Latest publish date'})
class TimeFrame(Resource):
    def get(self, epoch_start, epoch_end):
        """
        Query books by publish date after start date and before end date.
        :param epoch_start: Earliest publish date to query by.
        :param epoch_end: Latest publish date to query by.
        :return: JSON list of books
        """
        #query by start and end dates
        return "Books between" + epoch_start + epoch_end, 200


@api.route('/books/<subject>')
@api.doc(params={'subject': 'Subject to search by'})
class BookSubject(Resource):
    def get(self, subject):
        """
        Query books by subject.
        :param subject: String value to query by
        :return: JSON list of books
        """
        # query by subject
        return "Subject: %s" %subject, 200


@api.route('/books/<genre>')
@api.doc(params={'genre': 'Genre to search by'})
class BooksGenre(Resource):
    def get(self, genre):
        """
        Query books by genre.
        :param genre: String value to query by
        :return:  JSON list of books
        """
        #query by genre
        return "Genre %s" %genre, 200



if __name__ == '__main__':
    app.run(debug=True)
