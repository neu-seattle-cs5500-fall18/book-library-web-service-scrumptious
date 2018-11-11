from library_webservice import db
from model.note import Note


def contains(note_title, book_id):
    a_note = Note.query.filter_by(note_title=note_title, book_id=book_id)
    if a_note is None:
        return False
    else:
        return True


def create(note):
    db.session.add(note)
    db.session.commit()
    return note


def get_notes(book_id):
    list_notes = []
    notes = Note.query.filter_by(book_id=book_id)

    for note in notes:
        list_notes.append(note.to_dict())
    return list_notes


def update(note):
    a_note = Note.query.get(note.note_title)
    a_note.update(**note)
    db.session.commit()
    return a_note.to_dict()


def delete(note):
    a_note = db.session.get(note.note_title).delete()
    db.session.commit()
    return a_note



