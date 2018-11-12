from library_webservice import db
from model.note import Note


class NoteDao:

    @staticmethod
    def contains(note_title):
        if Note.query.get(note_title) is None:
            return False
        else:
            return True

    @staticmethod
    def create(book_id, note_dict):
        note = Note(**note_dict)
        note['book_id'] = book_id

        db.session.add(note)
        db.session.commit()
        return note.to_dict()

    @staticmethod
    def get(note_title):
        print('NoteDao.get()')
        note = Note.query.get(note_title)
        return note.to_dict()

    @staticmethod
    def get_notes(book_id):
        print('NoteDao.get_notes()')
        list_notes = []
        notes = Note.query.filter_by(book_id=book_id).all()

        for note in notes:
            list_notes.append(note.to_dict())
        return list_notes

    @staticmethod
    def update(note_dict):
        a_note = Note.query.get(note_dict.note_title)
        a_note.update(**note_dict)
        db.session.commit()
        return a_note.to_dict()

    @staticmethod
    def delete(note):
        db.session.get(note.note_title).delete()
        db.session.commit()
        return None



