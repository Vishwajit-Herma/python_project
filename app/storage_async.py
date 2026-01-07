import json
import asyncio
from app.storage import DATA_DIR
from app.logger import logger
from app.exceptions import StorageError
import os


async def save_json_async(filename, data):
    path = os.path.join(DATA_DIR, filename)

    try:
        await asyncio.to_thread(
            lambda: json.dump(data, open(path, "w"), indent=4)
        )
        logger.info(f"Async saved file: {path}")
    except Exception as e:
        logger.error(f"Async storage failed: {e}")
        raise StorageError(f"Could not store file: {filename}")
