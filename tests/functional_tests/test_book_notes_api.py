import json


def test_get_notes(session, client, book1_dict, book4_dict):

    """Add data to db"""
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(book4_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    """Nonexistent id"""
    get_response = client.get("books/5/notes")
    assert 404 == get_response.status_code

    """Invalid id"""
    get_response = client.get("books/L/notes")
    assert 400 == get_response.status_code

    """No notes"""
    get_response = client.get("books/1/notes")
    assert 200 == get_response.status_code
    payload = get_response.get_json()
    assert [] == payload

    """Notes"""
    get = client.get("/books/2")
    print(get.get_json())
    expected_payload = [
        {
            'note_title': 'Dystopia',
            'note': 'THE dystopian novel.',
            'book_id': 2
        }]
    get_response = client.get("books/2/notes")
    assert 200 == get_response.status_code
    payload = get_response.get_json()
    assert expected_payload == payload


def test_post_notes(session, client, book1_dict):
    """Add data to db"""
    json_data = json.dumps(book1_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    """Notes"""
    note1 = {'note_title': 'A Note','note': 'A note Note note'}
    note2 = {'note_title': 'noteAtitle', 'note': 'another note note notie note'}

    """expected results"""
    expected_note1 = {'note_title': 'A Note', 'note': 'A note Note note', 'book_id': 1}
    expected_note2 = {'note_title': 'noteAtitle', 'note': 'another note note notie note', 'book_id': 1}

    """test out of range id"""
    json_data = json.dumps(note1)
    get_response = client.post("/books/2/notes", data=json_data, headers={"Content-Type": "application/json"})
    assert 404 == get_response.status_code

    """test invalid id"""
    get_response = client.post("/books/L/notes", data=json_data, headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """test post with no body to request"""
    get_response = client.post("/books/1/notes", headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """test post with missing params"""
    incomplete_note = {'note_title':'title'}
    json_data = json.dumps(incomplete_note)
    get_response = client.post("books/1/notes", data=json_data, headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """test post with complete body"""
    json_data = json.dumps(note1)
    get_response = client.post("books/1/notes", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == get_response.status_code
    payload = get_response.get_json()
    assert expected_note1 == payload

    """test post with same note title"""
    get_response = client.post("books/1/notes", data=json_data, headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """test second post with complete body"""
    json_data = json.dumps(note2)
    get_response = client.post("books/1/notes", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == get_response.status_code
    payload = get_response.get_json()
    assert expected_note2 == payload


def test_put_notes(session, client, book4_dict):
    """Add data to db, book that has existing notes"""
    json_data = json.dumps(book4_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    new_note= {
        'note': 'THE dystopian novel of all time- apart from Brave New World.'
    }

    """test invalid id"""
    json_data = json.dumps(new_note)
    get_response = client.put("/books/L/notes/Dystopia", data=json_data, headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """"test out of range id"""
    get_response = client.put("books/2/notes/Dystopia", data=json_data, headers={"Content-Type": "application/json"})
    assert 404 == get_response.status_code

    """"test incomplete notes"""
    incomplete_note = {"note_title": "title"}
    json_data = json.dumps(incomplete_note)
    get_response = client.put("books/1/notes/Dystopia", data=json_data, headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """test request with no body"""
    get_response = client.put("/books/1/notes/Dystopia", headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """"test note with non-existant key"""
    json_data = json.dumps(new_note)
    get_response = client.put("/books/1/notes/Dys", data=json_data, headers={"Content-Type": "application/json"})
    assert 404 == get_response.status_code

    """test correct note"""
    json_data = json.dumps(new_note)
    get_response = client.put("books/1/notes/Dystopia", data= json_data, headers={"Content-Type": "application/json"})
    assert 200 == get_response.status_code

    expected_payload = {
        'note_title': 'Dystopia',
        'note': 'THE dystopian novel of all time- apart from Brave New World.',
        'book_id' : 1
    }

    payload = get_response.get_json()
    assert expected_payload == payload


def test_delete_notes(session, client, book4_dict):
    """Add data to db, book that has existing notes"""
    json_data = json.dumps(book4_dict)
    post_response = client.post("/books", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    """Test delete incorrect id"""
    get_response = client.delete("/books/L/notes/Dystopia")
    assert 400 == get_response.status_code

    """test delete non-existent id"""
    get_response = client.delete("/books/2/notes/Dystopia")
    assert 404 == get_response.status_code

    """test delete non-existent note key"""
    get_response = client.delete("/books/1/notes/Note")
    assert 404 == get_response.status_code

    """delete actual note"""
    get_response = client.delete("/books/1/notes/Dystopia")
    assert 204 == get_response.status_code

    get_response = client.get("/books/1/notes")
    payload = get_response.get_json()
    assert [] == payload

