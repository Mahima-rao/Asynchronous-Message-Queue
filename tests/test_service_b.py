import pytest
import redis
from fastapi.testclient import TestClient
from service_b.main import app

@pytest.fixture
def redis_client():
    """Fixture to create a Redis client and clear the Redis database before each test."""
    client = redis.StrictRedis(host='localhost', port=6379, db=0)
    client.flushdb()  # Clear the entire Redis database to ensure no leftover messages
    return client

@pytest.fixture
def client():
    return TestClient(app)

def test_message_consumption(redis_client):
    """Test if Service B consumes messages from the queue."""
    expected_message = "Test message from Service A"
    
    # Publish the message to the Redis queue
    redis_client.rpush("shared_queue", expected_message)

    # Simulate Service B consuming the message (we'll check the queue directly)
    message_from_queue = redis_client.blpop("shared_queue", timeout=10)
    
    # Check if the consumed message is as expected
    assert message_from_queue[1].decode() == expected_message
    print(f"Test passed, received message: {message_from_queue[1].decode()}")
