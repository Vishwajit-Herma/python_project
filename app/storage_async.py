import json
import asyncio
from app.storage import DATA_DIR
from app.logger import logger
from app.exceptions import StorageError
import os


async def save_json_async(filename, data):
    path = os.path.join(DATA_DIR, filename)

    try:
        def _write_json(path, data):
            with open(path, "w") as f:
                json.dump(data, f, indent=4)

        await asyncio.to_thread(_write_json, path, data)
        logger.info(f"Async saved file: {path}")
    except Exception as e:
        logger.error(f"Async storage failed: {e}")
        raise StorageError(f"Could not store file: {filename}")
