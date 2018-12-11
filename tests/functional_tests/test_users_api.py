import json


def test_post_users(session, client, user_dict1, user_dict2, expected_user1, expected_user2):

    """missing body"""
    post_response = client.post("/users", headers={"Content-Type": "application/json"})
    assert 400 == post_response.status_code

    """missing fields in json"""
    user = {
        'user_last_name': 'Doe'
    }
    json_data = json.dumps(user)
    post_response = client.post("/users", data=json_data, headers={"Content-Type": "application/json"})
    assert 500 == post_response.status_code

    """Actual case"""
    json_data = json.dumps(user_dict1)
    post_response = client.post("/users", data=json_data, headers={"Content-Type": "application/json"})

    assert 201 == post_response.status_code

    payload = post_response.get_json()
    print(payload)
    print (expected_user1)
    assert expected_user1 == payload

    """Actual case 2"""
    json_data = json.dumps(user_dict2)
    post_response = client.post("/users", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    payload = post_response.get_json()
    assert expected_user2 == payload

    """Duplicate case"""
    json_data = json.dumps(user_dict1)
    post_response = client.post("/users", data=json_data, headers={"Content-Type": "application/json"})
    assert 400 == post_response.status_code


def test_get_users(session, client, user_dict1, user_dict2, expected_user1, expected_user2):
    """Load data to db"""
    json_data = json.dumps(user_dict1)
    post_response = client.post("/users", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(user_dict2)
    post_response = client.post("/users", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code


    """test get all"""
    expected_payload= [expected_user1, expected_user2]
    get_response = client.get("/users")
    assert 200 == get_response.status_code

    payload = get_response.get_json()
    assert expected_payload == payload


def test_get_user(session, client, user_dict1, user_dict2, expected_user1, expected_user2):
    """Load data to db"""
    json_data = json.dumps(user_dict1)
    post_response = client.post("/users", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(user_dict2)
    post_response = client.post("/users", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    """Invalid id"""
    get_response = client.get("/users/L")
    assert 400 == get_response.status_code

    """Out of range ID"""
    get_response = client.get("/users/4")
    assert 404 == get_response.status_code

    """Valid ID"""
    get_response = client.get("/users/1")
    assert 200 == get_response.status_code

    payload = get_response.get_json()
    assert expected_user1 == payload

    """Valid ID"""
    get_response = client.get("/users/2")
    assert 200 == get_response.status_code

    payload = get_response.get_json()
    assert expected_user2 == payload


def test_put_user(session, client, user_dict1, user_dict2):
    """Load data to db"""
    json_data = json.dumps(user_dict1)
    post_response = client.post("/users", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(user_dict2)
    post_response = client.post("/users", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    record = {
        'user_first_name': 'John',
        'user_last_name': 'Doe',
        'user_email': 'aChangedEmail@something.com'
    }
    expected_record = {
        'user_id': 1,
        'user_first_name': 'John',
        'user_last_name': 'Doe',
        'user_email': 'aChangedEmail@something.com'
    }

    """Missing json"""
    get_response = client.put("/users/1", headers={"Content-Type": "application/json"})
    assert 400 == get_response

    """incomplete json"""
    incomplete_record = {
        'user_last_name': 'Doe',
        'user_email': 'aChangedEmail@something.com'
    }
    json_data = json.dumps(incomplete_record)
    get_response = client.put("/users/1", data=json_data, headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """invalid ID"""
    json_data = json.dumps(record)
    get_response = client.put("/users/L", data = json_data, headers={"Content-Type": "application/json"})
    assert 400 == get_response.status_code

    """Out of range id"""
    get_response = client.put("/users/6", data = json_data, headers={"Content-Type": "application/json"})
    assert 404 == get_response.status_code

    """Correct case"""
    json_data = json.dumps(record)
    get_response = client.put("/users/1", data = json_data, headers={"Content-Type": "application/json"})
    assert 200 == get_response.status_code

    payload = get_response.get_json()
    assert expected_record == payload


def test_delete_user(session, client, user_dict1, user_dict2, expected_user2):
    """Load data to db"""
    json_data = json.dumps(user_dict1)
    post_response = client.post("/users", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    json_data = json.dumps(user_dict2)
    post_response = client.post("/users", data=json_data, headers={"Content-Type": "application/json"})
    assert 201 == post_response.status_code

    """delete invalid id"""
    get_response = client.delete("/users/L")
    assert 400 == get_response.status_code

    """delete out of range id"""
    get_response = client.delete("/users/80")
    assert 404 == get_response.status_code

    """delete correct"""
    get_response = client.delete("/users/1")
    assert 204 == get_response.status_code

    get_response = client.get("/users")
    assert 200 == get_response.status_code

    payload = get_response.get_json()
    expected_payload = [expected_user2]
    assert expected_payload == payload

    """re-delete resource"""
    get_response = client.delete("/users/1")
    assert 404 == get_response.status_code


