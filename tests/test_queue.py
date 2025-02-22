import pytest
import redis
import time

@pytest.fixture
def redis_client():
    """Fixture to create a Redis client and clear the Redis database before each test."""
    client = redis.StrictRedis(host='localhost', port=6379, db=0)
    client.flushdb()  # Clear the entire Redis database to ensure no leftover messages
    return client

def test_publish_message(redis_client):
    """Test the publish functionality of the Redis queue."""
    message = "Hello from test!"
    
    # Publish the message to the Redis queue
    redis_client.rpush("shared_queue", message)

    # Add a short delay to ensure the message is added to the queue
    time.sleep(1)

    # Verify the message is in the queue
    message_from_queue = redis_client.blpop("shared_queue", timeout=10)
    assert message_from_queue is not None, "No message was retrieved from the queue"
    assert message_from_queue[1].decode() == message
    print("Test passed, message published.")
