from library_webservice import db
from data_access_layer import book_dao
from model.author import Author


class AuthorDao:
    @staticmethod
    def get_author(author_id):
        author = Author.query.get(author_id)
        return author.to_dict()

    @staticmethod
    def create(book_id, list_author):
        print("author_dao.create()")

        book = book_dao.get(book_id)

        for author in list_author:
            if Author.query.filter_by(**author).all():
                existing_record = Author.query.filter_by(**author).first()
                print(existing_record)
                existing_record.books.append(book)
                print("appended book to existing author")
            else:
                print("or here")
                new_author = Author(**author)
                new_author.books.append(book)
                db.session.add(new_author)
                print("added new author")
        db.session.commit()
        print("author_dao.create() ==> Complete")

    @staticmethod
    def delete(author_id):
        db.session.get(author_id).delete()
        db.session.commit
        return
