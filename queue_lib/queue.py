import asyncio
import logging
from redis.asyncio import Redis

logging.basicConfig(level=logging.DEBUG)

class RedisMessageQueue:
    def __init__(self, redis_url="redis://localhost:6379", queue_name="shared_queue"):
        self.redis_url = redis_url
        self.queue_name = queue_name
        self.redis = Redis.from_url(redis_url)

    async def publish(self, message: str):
        """Publish a message to the Redis queue."""
        await self.redis.rpush(self.queue_name, message)
        logging.debug(f"Message '{message}' added to the Redis queue.")

    async def subscribe(self, handler):
        """Subscribe to the Redis queue and process messages."""
        logging.debug("Starting subscription to Redis queue...")
        while True:
            try:
                # Blocking pop to wait for new messages
                message = await self.redis.blpop(self.queue_name)
                if message:
                    await handler(message[1].decode("utf-8"))
            except asyncio.CancelledError:
                logging.debug("Subscription task cancelled.")
                break
            except Exception as e:
                logging.error(f"Error while processing message: {e}")

# Create a shared queue instance
shared_queue = RedisMessageQueue()
