from src.app import app

client = app.test_client()

def test_correct_input():
    response = client.post("/recommend", json={"liked_titles": ["Naruto", "Death Note"]})
    assert response.status_code == 200
    data = response.get_json()
    assert "recommendation" in data

def test_missing_liked_titles():
    response = client.post("/recommend", json={})
    assert response.status_code == 400

def test_wrong_type():
    response = client.post("/recommend", json = {"liked_titles": "Naruto, Death Note"})
    assert response.status_code == 400
    response = client.post("/recommend", json = {"liked_titles": 4})
    assert response.status_code == 400
    response = client.post("/recommend", json = {"liked_titles": 4.5})
    assert response.status_code == 400

def test_empty_list():
    response = client.post("/recommend", json={"liked_titles":[]})
    assert response.status_code == 400

def test_bad_item():
    response = client.post("/recommend", json = {"liked_titles": ["Naruto", 25]})
    assert response.status_code == 400
    response = client.post("/recommend", json = {"liked_titles": ["Naruto", ""]})
    assert response.status_code == 400

def test_fake_anime():
    response = client.post("/recommend", json = {"liked_titles": ["Naruto", "Fake Anime"]})
    assert response.status_code == 404

def test_invalid_data():
    response = client.post("/recommend", json = None)
    assert response.status_code == 400