# Third Party Libraries
from fastapi.testclient import TestClient

# Our Libraries
from api.v1 import app

client = TestClient(app)


def test_read_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_post_webhook():
    response = client.post(
        "/",
        headers={},
        json={"id": "foobar"},
    )
    #  assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
    }
