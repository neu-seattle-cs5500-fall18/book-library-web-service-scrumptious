from flask import abort
from data_access_layer.book_dao import BookDao
from data_access_layer.note_dao import NoteDao


class NoteChecker:
    @staticmethod
    def get_notes(book_id):
        """
        Method to retrieve a list of notes about a book
        :param book_id: the unique book identifier
        :return: list of notes for a book
        """
        print('NoteChecker.get_notes()')
        if BookDao.contains(book_id):
            list_notes = NoteDao.get_notes(book_id)
            return list_notes
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def create_note(book_id, note):
        """
        Method to create a note about a particular book
        :param book_id: the unique book identifier
        :param note: String representation of the note
        :return: The book note
        """
        print('NoteChecker.create_note()')
        if BookDao.contains(book_id):
            if NoteDao.contains(note.get('note_title')):
                abort(400, 'Duplicate key violates unique constraint: note_title')
            else:
                note = NoteDao.create(book_id, note)
                return note
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def create_notes(book_id, notes_array):
        """
        Method to create a list of notes about a particular book
        :param book_id: the unique book identifier
        :param notes_array: list of Strings representing the notes to add
        :return: a list of notes
        """
        print('NoteChecker.create_notes()')
        list_notes = []
        if BookDao.contains(book_id):
            for note in notes_array:
                print(note)
                created_note = NoteChecker.create_note(book_id, note)
                list_notes.append(created_note)
            return list_notes
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def update_note(book_id, note_title, note):
        """
        Method to update a note record if book id, note title are valid and there is a relationship between them.
        :param book_id: record of a book.
        :param note_title: record of a note.
        :param note: the amended note text.
        :return: dictionary of note object.
        """
        print('NoteChecker.update_note()')
        if BookDao.contains(book_id):
            if NoteDao.contains_relationship(book_id, note_title):
                return NoteDao.update(note_title, note)
            else:
                abort(404, 'Resource not found: note_title & book_id do not share a record')
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def delete_note(book_id, note_title):
        """
        Method to delete a note if book id, note title are valid and there is a relationship between them.
        :param book_id: record of a book.
        :param note_title: record of a note.
        :return: None
        """
        print('NoteChecker.delete()')
        if BookDao.contains(book_id):
            if NoteDao.contains_relationship(book_id, note_title):
                return NoteDao.delete(note_title)
            else:
                abort(404, 'Resource not found: note_title & book_id do not share a record')
        else:
            abort(404, 'Resource not found: book_id')
