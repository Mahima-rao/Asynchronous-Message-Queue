import logging
from fastapi import FastAPI
from pydantic import BaseModel
from queue_lib.queue import AsyncMessageQueue  # Import the message queue abstraction

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

# Request body model
class Message(BaseModel):
    message: str

# Initialize the shared message queue
message_queue = AsyncMessageQueue()

@app.post("/publish/")
async def publish_message(data: Message):
    """Publish a message to the shared queue."""
    logging.debug(f"Received message: {data.message}")

    # Log the queue size before adding the message
    logging.debug(f"Queue size before publishing: {message_queue.queue.qsize()}")

    # Add message to the shared queue
    await message_queue.publish(data.message)

    # Log the queue size after adding the message
    logging.debug(f"Queue size after publishing: {message_queue.queue.qsize()}")
    logging.debug(f"Message '{data.message}' published to the queue.")

    return {"status": "Message published successfully"}