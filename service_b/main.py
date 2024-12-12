from fastapi import FastAPI
import asyncio
import logging
from queue_lib.queue import shared_queue

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Define lifespan function
async def lifespan(app):
    logging.debug("Service B: Starting lifespan...")
    task = asyncio.create_task(shared_queue.subscribe(process_message))
    yield  # Lifespan stays active during server runtime
    logging.debug("Service B: Shutting down...")
    task.cancel()
    await task

# Initialize FastAPI app with lifespan
app = FastAPI(lifespan=lifespan)

async def process_message(message: str):
    """Process a message from the queue."""
    logging.debug(f"Service B: Processing message: {message}")
    # Simulate some processing time
    await asyncio.sleep(1)
    logging.debug(f"Service B: Message '{message}' processed.")
