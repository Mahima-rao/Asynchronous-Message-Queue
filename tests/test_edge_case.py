import pytest
import redis
import time

@pytest.fixture
def redis_client():
    return redis.StrictRedis(host='localhost', port=6379, db=0)

def test_empty_message(redis_client):
    """Test publishing an empty message."""
    message = ""
    
    # Publish the empty message to the Redis queue
    redis_client.rpush("shared_queue", message)

    # Add a short delay to ensure the message is added to the queue
    time.sleep(1)  # Small delay to allow the message to be available for consumption

    # Verify the empty message is in the queue
    message_from_queue = redis_client.blpop("shared_queue", timeout=10)
    assert message_from_queue is not None, "No message was retrieved from the queue"
    assert message_from_queue[1].decode() == message
    print("Test passed, empty message handled.")
