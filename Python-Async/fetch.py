import aiohttp
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    result = await fetch_data(url)
    print(result)

asyncio.run(main())