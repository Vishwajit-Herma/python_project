import aiohttp
import asyncio
from app.logger import logger
from app.exceptions import APIError

COMMENTS_API = "https://jsonplaceholder.typicode.com/comments"


async def fetch_comments():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(COMMENTS_API) as response:
                response.raise_for_status()
                return await response.json()
    except Exception as e:
        logger.error(f"Async fetch comments failed: {e}")
        raise APIError("Unable to fetch comments")
