import logging
from fastapi import FastAPI
from pydantic import BaseModel
from queue_lib.queue import shared_queue  # Import the shared queue

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/service_a/publish/")
async def publish_message(data: Message):
    """Publish a message to the shared queue."""
    logging.debug(f"Service A: Received message to publish: {data.message}")
    # Log the queue size before adding the message
    logging.debug(f"Queue size before publishing: {shared_queue.queue.qsize()}")

    # Add message to the shared queue
    await shared_queue.publish(data.message)

    
    # Log the queue size after adding the message
    logging.debug(f"Queue size after publishing: {shared_queue.queue.qsize()}")

    # Log success
    logging.debug(f"Service A: Message '{data.message}' added to the queue.")

    return {"status": "Message published successfully"}
