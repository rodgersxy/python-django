import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        item = f"item-{i}"
        await queue.put(item)
        print(f"Produced: {item}")

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed: {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await asyncio.gather(producer_task)
    await queue.join()
    consumer_task.cancel()

asyncio.run(main())
