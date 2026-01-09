import json
import os
from threading import Thread
from app.utils.logger import logger
from app.utils.exceptions import StorageError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)


def _write_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def save_json(filename, data):
    try:
        path = os.path.join(DATA_DIR, filename)

        thread = Thread(target=_write_json, args=(path, data))
        thread.start()
        thread.join()  

        logger.info(f"Threaded save completed: {path}")

    except (OSError, TypeError, RuntimeError) as e:
        logger.error(f"Threaded storage failed for {filename}: {e}")
        raise StorageError(f"Could not store file using threading: {filename}")
