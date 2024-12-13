import pytest
from fastapi.testclient import TestClient
from service_a.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_publish_message(client):
    """Test the /publish/ endpoint in Service A."""
    data = {"message": "Test message from Service A"}
    
    # Send a POST request to the /publish/ endpoint
    response = client.post("/publish/", json=data)
    
    # Check if the status code is 200 and the message was published successfully
    assert response.status_code == 200
    assert response.json() == {"status": "Message published successfully"}
    print("Test passed, message published.")
