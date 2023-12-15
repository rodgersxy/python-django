import asyncio

async def example():
    print("Start")
    await asyncio.sleep(1)
    print("End")

asyncio.run(example())