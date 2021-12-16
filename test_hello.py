from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_valid_id():
    response = client.get("/check")
    assert response.status_code == 200
