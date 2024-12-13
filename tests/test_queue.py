import asyncio
from queue_lib.queue import shared_queue

async def handler(message):
    print(f"Handler: Processing message '{message}'")

async def main():
    await shared_queue.publish("Test Message")
    task = asyncio.create_task(shared_queue.subscribe(handler))
    await asyncio.sleep(3)  # Give time for the subscription to process
    task.cancel()
    await task

asyncio.run(main())
