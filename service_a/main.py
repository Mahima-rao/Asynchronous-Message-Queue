from fastapi import FastAPI
from pydantic import BaseModel
from queue_lib.queue import shared_queue
import logging

logging.basicConfig(level=logging.DEBUG)

# Create the FastAPI app
app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/publish/")
async def publish_message(data: Message):
    """Publish a message to the shared Redis queue."""
    logging.debug(f"Service A: Publishing message '{data.message}'")
    await shared_queue.publish(data.message)
    return {"status": "Message published successfully"}
