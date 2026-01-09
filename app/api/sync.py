import requests
from app.utils.logger import logger
from app.utils.exceptions import APIError

USERS_API = "https://jsonplaceholder.typicode.com/users"
POSTS_API = "https://jsonplaceholder.typicode.com/posts"


def fetch_users():
    try:
        response = requests.get(USERS_API, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch users: {e}")
        raise APIError("Unable to fetch users data")


def fetch_posts():
    try:
        response = requests.get(POSTS_API, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch posts: {e}")
        raise APIError("Unable to fetch posts data")
