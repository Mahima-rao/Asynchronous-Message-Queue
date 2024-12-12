import pytest
import asyncio
import sys
import os

# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from queue_lib.queue import AsyncMessageQueue

@pytest.mark.asyncio
async def test_publish_and_subscribe():
    # Create an instance of the message queue
    queue = AsyncMessageQueue()

    # Simple handler for processing messages
    async def handler(message):
        assert message == "Test Message"

    # Publish a message
    await queue.publish("Test Message")

    # Subscribe to the queue and process the message
    await queue.subscribe(handler)

@pytest.mark.asyncio
async def test_retries_on_failure():
    queue = AsyncMessageQueue()
    retry_attempts = 3
    retry_delay = 1
    failed_attempts = 0

    async def handler(message):
        nonlocal failed_attempts
        failed_attempts += 1
        if failed_attempts < retry_attempts:
            raise ValueError("Processing failed")
        assert message == "Test Retry Message"
        
    await queue.publish("Test Retry Message")
    await queue.subscribe(handler, retry_attempts=retry_attempts, retry_delay=retry_delay)
