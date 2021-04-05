# Third Party Libraries
from fastapi.testclient import TestClient

# Our Libraries
from api.v1 import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
