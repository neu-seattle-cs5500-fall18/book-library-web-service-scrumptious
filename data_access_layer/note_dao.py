from model import db
from model.note import Note


class NoteDao:

    @staticmethod
    def contains(note_title):
        """
        Method to determine if Note exists.
        :param note_title: Record of Note.
        :return: True if Note exists, False otherwise.
        """
        if Note.query.get(note_title) is None:
            return False
        else:
            return True

    @staticmethod
    def contains_relationship(book_id, note_title):
        """
        Method to determine if a record with book id and note title exists.
        :param book_id: record of a book.
        :param note_title: record of a note.
        :return: true if exists, false otherwise.
        """
        print('NoteDao.contains_relationship()')
        results = Note.query.filter_by(book_id=book_id, note_title=note_title).first()
        print(results)
        if results is None:
            return False
        else:
            return True

    @staticmethod
    def create(book_id, note_dict):
        """
        Method to create a Note and associate it to a Book.
        :param book_id: Record of Book to associate the note to.
        :param note_dict: Attributes of note to create a new Note.
        :return: Dictionary of created Note.
        """
        print("NoteDao.create()")
        note = Note(**note_dict)
        db.session.add(note)
        note.book_id = book_id
        print(note)
        db.session.commit()
        return note.to_dict()

    @staticmethod
    def get(note_title):
        """
        Method to get a Note.
        :param note_title: Record of a Note.
        :return: Dictionary of Note.
        """
        print('NoteDao.get()')
        note = Note.query.get(note_title)
        return note.to_dict()

    @staticmethod
    def get_notes(book_id):
        """
        Method to get all notes associated with a Book.
        :param book_id: Record of a Book.
        :return: List of Notes as Dictionary objects.
        """
        print('NoteDao.get_notes()')
        list_notes = []
        notes = Note.query.filter_by(book_id=book_id).all()

        for note in notes:
            list_notes.append(note.to_dict())
        return list_notes

    @staticmethod
    def update(note_title, note):
        """
        Method to update a Note.
        :param note_title: Key for a note.
        :param note: Attributes of a Note to be updated.
        :return: Dictionary of updated Note.
        """
        print('NoteDao.update()')
        a_note = Note.query.get(note_title)
        print(a_note)
        print(note)
        a_note.update(**note)
        db.session.commit()
        return a_note.to_dict()

    @staticmethod
    def delete(note_title):
        """
        Method to delete a Note.
        :param note_title: Note to be deleted.
        :return: null.
        """
        note = Note.query.get(note_title)
        db.session.delete(note)
        db.session.commit()
        return None



