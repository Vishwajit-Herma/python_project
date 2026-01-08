import asyncio
from app.api_async_comments import fetch_comments
from app.storage_async import save_json_async


async def main():
    print("Async application started")

    comments = await fetch_comments()
    await save_json_async("comments_async.json", comments)

    print("Async application finished")


if __name__ == "__main__":
    asyncio.run(main())
