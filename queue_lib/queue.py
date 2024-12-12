import asyncio
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class AsyncMessageQueue:
    def __init__(self, max_size: int = 100):
        """Initialize the asynchronous in-memory queue."""
        self.queue = asyncio.Queue(max_size)

    async def publish(self, message: str):
        """Publish a message to the in-memory queue."""
        await self.queue.put(message)
        logging.debug(f"Message '{message}' added to the queue.")

    async def subscribe(self, handler):
        """Subscribe to the in-memory queue and process messages using the handler."""
        logging.debug("Starting subscription...")
        while True:
            try:
                # Get the next message from the queue
                message = await self.queue.get()
                logging.debug(f"Message '{message}' retrieved from the queue.")

                # Process the message using the provided handler
                await handler(message)

                # Mark the task as done
                self.queue.task_done()
                logging.debug(f"Message '{message}' processed successfully.")
            except asyncio.CancelledError:
                logging.debug("Subscription task cancelled.")
                break
            except Exception as e:
                logging.error(f"Error while processing message: {e}")

# Create a shared queue instance
shared_queue = AsyncMessageQueue()
