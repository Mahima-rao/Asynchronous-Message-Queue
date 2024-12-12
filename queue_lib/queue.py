import asyncio
import logging
from typing import Any, Callable, Optional

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class AsyncMessageQueue:
    def __init__(self, max_size: int = 100):
        """Initialize the asynchronous in-memory queue."""
        self.queue = asyncio.Queue(max_size)

    async def publish(self, message: Any):
        """Publish a message to the in-memory queue."""
        await self.queue.put(message)
        logging.debug(f"Message '{message}' added to the queue.")

    async def subscribe(self, handler: Callable[[Any], None], retry_attempts: int = 3, retry_delay: int = 2):
        """Subscribe to the in-memory queue and process messages using the handler."""
        while True:
            message = await self.queue.get()
            attempt = 0
            success = False
            while attempt < retry_attempts and not success:
                try:
                    await handler(message)
                    logging.debug(f"Message '{message}' processed successfully.")
                    success = True
                except Exception as e:
                    attempt += 1
                    logging.error(f"Error processing message: {e}. Retrying {attempt}/{retry_attempts}...")
                    await asyncio.sleep(retry_delay)
                finally:
                    self.queue.task_done()

    async def consume(self) -> Any:
        """Consume a message from the queue."""
        return await self.queue.get()
