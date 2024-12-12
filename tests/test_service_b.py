import pytest
import asyncio
from fastapi.testclient import TestClient
from service_b.main import app
from queue_lib.queue import AsyncMessageQueue

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

@pytest.mark.asyncio
async def test_service_b_subscription():
    queue = AsyncMessageQueue()

    # Simulate a message handler in Service B
    async def handler(message):
        assert message == "Test Message for Service B"

    # Publish a test message to the queue
    await queue.publish("Test Message for Service B")

    # Subscribe to the queue and process the message
    await asyncio.wait_for(queue.subscribe(handler), timeout=15)
