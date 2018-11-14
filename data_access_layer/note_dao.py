from library_webservice import db
from model.note import Note


class NoteDao:

    @staticmethod
    def contains(note_title):
        """
        Method to determine if Note exists.
        :param note_title: Record of Note
        :return: True if Note exists, False otherwise.
        """
        if Note.query.get(note_title) is None:
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
    def update(note_dict):
        """
        Method to update a Note.
        :param note_dict: Attributes of a Note to be updated.
        :return: Dictionary of updated Note.
        """
        a_note = Note.query.get(note_dict['note_title'])
        a_note.update(**note_dict)
        db.session.commit()
        return a_note.to_dict()

    @staticmethod
    def delete(note):
        """
        Method to delete a Note.
        :param note: Note to be deleted.
        :return: Null.
        """
        db.session.get(note.note_title).delete()
        db.session.commit()
        return None



