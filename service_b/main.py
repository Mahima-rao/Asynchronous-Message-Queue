import logging
import asyncio
from fastapi import FastAPI
from queue_lib.queue import shared_queue

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

async def process_message(message: str):
    """Process a message from the Redis queue."""
    logging.debug(f"Service B: Processing message: {message}")
    await asyncio.sleep(1)  # Simulate processing delay
    logging.debug(f"Service B: Finished processing message: {message}")

async def message_consumer():
    """Consume messages from the Redis queue with retry logic."""
    logging.debug("Service B: Starting message consumer...")
    max_retries = 3  # Maximum number of retries for a message
    retry_delay = 2  # Delay (in seconds) between retries

    while True:
        try:
            # Blocking pop to retrieve a message from the Redis queue (asynchronously)
            message = await shared_queue.redis.blpop(shared_queue.queue_name, timeout=10)
            if message:
                logging.debug(f"Service B: Retrieved message: {message[1]}")

                retries = 0
                while retries < max_retries:
                    try:
                        await process_message(message[1].decode("utf-8"))
                        break  # Exit retry loop if successful
                    except Exception as e:
                        retries += 1
                        logging.error(
                            f"Service B: Error processing message. Retry {retries}/{max_retries}. Error: {e}"
                        )
                        await asyncio.sleep(retry_delay)

                if retries == max_retries:
                    logging.error(f"Service B: Failed to process message after {max_retries} retries: {message[1]}")

            else:
                logging.debug("Service B: No messages in queue.")

        except Exception as e:
            logging.error(f"Service B: Error while consuming messages: {e}")

@app.on_event("startup")
async def startup_event():
    """Start the message consumer as a background task."""
    logging.debug("Service B: Starting up...")
    asyncio.create_task(message_consumer())  # Start consuming messages in the background

@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event to clean up resources."""
    logging.debug("Service B: Shutting down...")
