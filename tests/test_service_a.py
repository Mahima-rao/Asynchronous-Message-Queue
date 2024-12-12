import pytest
from fastapi.testclient import TestClient
from service_a.main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_publish_message(client):
    # Send a POST request to publish a message
    response = client.post("/publish/", json={"message": "Hello, Service B!"})
    
    # Check if the response status is successful
    assert response.status_code == 200
    assert response.json() == {"status": "Message published successfully"}
