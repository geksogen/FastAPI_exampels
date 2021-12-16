from app import application

with application.test_client() as c:
    response = c.get("/check")
    assert response.data == b'Hello World'
    assert response.status_code == 200