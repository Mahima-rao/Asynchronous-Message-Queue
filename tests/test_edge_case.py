import pytest
from queue_lib.queue import AsyncMessageQueue
import asyncio

@pytest.mark.asyncio
async def test_empty_queue_subscription():
    queue = AsyncMessageQueue()

    # Simulate an empty queue (no messages are published yet)
    message_processed = []

    # Define the handler to process a message
    async def handler(message):
        message_processed.append(message)

    # Run the subscription, which should wait for a message
    asyncio.create_task(queue.subscribe(handler))

    # Now publish a message to the queue after a short delay
    await asyncio.sleep(1)
    await queue.publish("Message after delay")

    # Wait for the message to be processed
    await asyncio.sleep(1)
    assert message_processed[0] == "Message after delay"
