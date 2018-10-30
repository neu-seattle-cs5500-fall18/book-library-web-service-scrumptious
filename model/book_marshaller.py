



class BookMarshaller(object):
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
