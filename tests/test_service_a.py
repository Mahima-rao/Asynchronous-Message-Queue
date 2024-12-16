import pytest
from fastapi.testclient import TestClient
from service_a.main import app
import redis

@pytest.fixture
def redis_client():
    """Fixture to create a Redis client and clear the Redis database before each test."""
    client = redis.StrictRedis(host='localhost', port=6379, db=0)
    client.flushdb()  # Clear the entire Redis database to ensure no leftover messages
    return client

@pytest.fixture
def client(redis_client):  # Use the redis_client fixture that flushes the DB
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
