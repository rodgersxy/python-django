import asyncio


example = lambda: asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(example())
    task2 = asyncio.create_task(example())
    
    await asyncio.gather(task1, task2)

asyncio.run(main())