# Third Party Libraries
from fastapi.testclient import TestClient

# Our Libraries
from strava_gsheet.server import app

client = TestClient(app)


def test_read_status():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
