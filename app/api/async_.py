import aiohttp
import asyncio
from app.utils.logger import logger
from app.utils.exceptions import APIError


async def fetch(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()
    except aiohttp.ClientResponseError as e:
        logger.error(f"HTTP error while fetching {url}: {e}")
        raise APIError(f"HTTP error while fetching data from {url}")
    except aiohttp.ClientError as e:
        logger.error(f"Client error while fetching {url}: {e}")
        raise APIError(f"Client error while fetching data from {url}")


async def fetch_all():
    logger.info("Fetching data asynchronously")
    try:
        async with aiohttp.ClientSession() as session:
            users_task = asyncio.create_task(
                fetch(session, "https://jsonplaceholder.typicode.com/users")
            )
            posts_task = asyncio.create_task(
                fetch(session, "https://jsonplaceholder.typicode.com/posts")
            )

            users = await users_task
            posts = await posts_task

            return users, posts

    except Exception as e:
        logger.error(f"Async fetch failed: {e}")
        raise APIError("Unable to fetch users and posts asynchronously")
