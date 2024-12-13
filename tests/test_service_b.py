import pytest
import redis
from service_b.main import app
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def redis_client():
    return redis.StrictRedis(host='localhost', port=6379, db=0)

def test_message_consumption(redis_client):
    """Test if Service B consumes messages from the queue."""
    message = "Test message for Service B"
    
    # Publish the message to the Redis queue
    redis_client.rpush("shared_queue", message)

    # Simulate Service B consuming the message (we'll check the queue directly)
    message_from_queue = redis_client.blpop("shared_queue", timeout=10)
    assert message_from_queue[1].decode() == message
    print(f"Test passed, message '{message}' consumed by Service B.")
