import logging
from fastapi import FastAPI
import asyncio
from queue_lib.queue import AsyncMessageQueue  # Import the message queue abstraction

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

# Initialize the shared message queue
message_queue = AsyncMessageQueue()

async def process_message(message: str):
    """Process the message from the queue."""
    logging.debug(f"Service B: Processing message: {message}")
    # Simulate message processing (add your logic here)
    await asyncio.sleep(1)  # Simulate some async task, if necessary
    logging.debug(f"Service B: Message '{message}' processed successfully.")

@app.on_event("startup")
async def start_subscriber():
    """Start the subscriber when the application starts."""
    logging.debug("Service B: Startup event triggered.")

    # Start the subscription task (process messages in the background)
    task = asyncio.create_task(message_queue.subscribe(process_message))
    logging.debug("Service B: Background task created successfully.")

    # Ensuring that the task is awaited properly (this keeps the task running)
    await task  # Await the task to ensure that the background task runs correctly

