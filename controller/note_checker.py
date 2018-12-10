from flask import abort
from data_access_layer.book_dao import BookDao
from data_access_layer.note_dao import NoteDao


class NoteChecker:
    @staticmethod
    def get_notes(book_id):
        if BookDao.contains(book_id):
            list_notes = NoteDao.get_notes(book_id)
            return list_notes
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def create_note(book_id, note):
        if BookDao.contains(book_id):
            if NoteDao.contains(note['note_title']):
                abort(400, 'Duplicate key violates unique constraint: note_title')
            else:
                note = NoteDao.create(book_id, note)
                return note
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def update_note(book_id, note):
        if BookDao.contains(book_id):
            return NoteDao.update(note)
        else:
            abort(404, 'Resource not found: book_id')

    @staticmethod
    def delete_note(note_title):
        if NoteDao.contains(note_title):
            return NoteDao.delete(note_title)
        else:
            abort(404, 'Resource not found: note_title')
