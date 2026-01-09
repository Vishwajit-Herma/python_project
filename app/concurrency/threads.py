from threading import Thread
from app.api.sync import fetch_users, fetch_posts
from app.utils.logger import logger
from app.utils.exceptions import APIError

def fetch_users_thread(result):
    try:
        logger.info("Thread: fetching users")
        result["users"] = fetch_users()
    except Exception as e:
        logger.error(f"Thread failed while fetching users: {e}")
        result["users_error"] = e


def fetch_posts_thread(result): 
    try:
        logger.info("Thread: fetching posts")
        result["posts"] = fetch_posts()
    except Exception as e:
        logger.error(f"Thread failed while fetching posts: {e}")
        result["posts_error"] = e


def fetch_data_with_threads():
    """
    Fetch users and posts concurrently using threads.
    """
    shared_result = {}

    t1 = Thread(target=fetch_users_thread, args=(shared_result,))
    t2 = Thread(target=fetch_posts_thread, args=(shared_result,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    if "users_error" in shared_result or "posts_error" in shared_result:
        raise APIError("Threaded API fetching failed")

    logger.info("Threading: fetched users and posts successfully")
    return shared_result


