from fastapi import FastAPI
import logging
import asyncio
from queue_lib.queue import shared_queue  # This imports the shared Redis queue

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Service B: Application is starting.")

app = FastAPI()

async def process_message(message: str):
    """Process a message from the Redis queue."""
    logging.debug(f"Service B: Processing message: {message}")
    await asyncio.sleep(1)  # Simulate some processing time
    logging.debug(f"Service B: Finished processing message: {message}")

async def message_consumer():
    """Consume messages from the Redis queue asynchronously."""
    logging.debug("Service B: Starting message consumer...")
    while True:
        try:
            # Blocking pop to retrieve a message from the Redis queue (asynchronously)
            message = await shared_queue.redis.blpop(shared_queue.queue_name, timeout=10)
            if message:
                logging.debug(f"Service B: Retrieved message: {message[1]}")
                await process_message(message[1])  # Process the message asynchronously
            else:
                logging.debug("Service B: No messages in queue.")
        except Exception as e:
            logging.error(f"Service B: Error while consuming messages: {e}")

@app.on_event("startup")
async def startup_event():
    """Start the message consumer as a background task."""
    logging.debug("Service B: Starting up...")
    # Start the consumer task in the background
    asyncio.create_task(message_consumer())

@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event to clean up resources."""
    logging.debug("Service B: Shutting down...")
