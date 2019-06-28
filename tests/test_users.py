from tests.general_fixtures.app import client



def test_create_user(client):
    result = client.post("/user", json={"username": "test"})
    assert result.status_code == 201

def test_create_user_bad_req(client):
    result = client.post("/user", json={"bad": "json"})
    assert result.status_code == 400

def test_get_user(client):
    result = client.get("/user/example_username")
    assert result.status_code == 200
    # print(result.data)

def test_get_user_non_existent(client):
    pass

