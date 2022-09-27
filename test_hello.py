from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_valid_id():
    response = client.get("/checks")
    assert response.status_code == 200
