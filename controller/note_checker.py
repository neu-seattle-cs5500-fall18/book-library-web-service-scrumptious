from flask import abort
from data_access_layer.book_dao import BookDao
from data_access_layer.note_dao import NoteDao


class NoteChecker:
    @staticmethod
    def get_note(book_id):
        if BookDao.contains(book_id):
            note = NoteDao.get(book_id)
            return note
        else:
            abort(404, 'Resource not found')

    @staticmethod
    def create_note(book_id, note):
        if BookDao.contains(book_id):
            note = NoteDao.create(book_id, note)
            return note
        else:
            abort(404,'Resource not found')

    @staticmethod
    def update_note(book_id, note):
        if BookDao.contains(book_id):
            return NoteDao.update(note)
        else:
            abort(404, 'Resource not found')

    @staticmethod
    def delete_note(note_title):
        if NoteDao.contains(note_title):
            return NoteDao.delete(note_title)
        else:
            abort(404, 'Resource not found')
