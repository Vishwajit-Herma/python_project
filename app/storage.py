import json
from logger import logger

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"Saved Data to {filename}")
