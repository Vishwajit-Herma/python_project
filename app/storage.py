import json
import os
from app.logger import logger
from app.exceptions import StorageError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)


def save_json(filename, data):
    try:
        path = os.path.join(DATA_DIR, filename)
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"Saved file: {path}")
    except (OSError, TypeError) as e:
        logger.error(f"Failed to save {filename}: {e}")
        raise StorageError(f"Could not store file: {filename}")
