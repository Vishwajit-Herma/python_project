import aiohttp
import asyncio
from logger import logger

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def fetch_all():
    logger.info("Fetching data asynchronously")
    async with aiohttp.ClientSession() as session:
        users, posts = await asyncio.gather(
            fetch(session, "https://jsonplaceholder.typicode.com/users"),
            fetch(session, "https://jsonplaceholder.typicode.com/posts")
        )
        return users, posts
