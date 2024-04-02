from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_password():
    response = client.post("/generate-password", json={"length": 12})
    assert response.status_code == 200
    data = response.json()
    assert len(data['password']) == 12

def test_invalid_length():
    response = client.post("/generate-password", json={"length": -1})
    assert response.status_code == 400

    response = client.post("/generate-password", json={"length": 0})
    assert response.status_code == 400
