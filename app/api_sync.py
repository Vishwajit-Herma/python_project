import requests
from logger import logger

USERS_API = "https://jsonplaceholder.typicode.com/users"
POSTS_API = "https://jsonplaceholder.typicode.com/posts"


def fetch_users():
    logger.info("Fetching users synchronously")
    response = requests.get(USERS_API)
    response.raise_for_status()
    return response.json()


def fetch_posts():
    logger.info("Fetching posts synchronously")
    response = requests.get(POSTS_API)
    response.raise_for_status()
    return response.json()
