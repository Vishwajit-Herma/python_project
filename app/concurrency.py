from threading import Thread
from multiprocessing import Process, Queue
from app.api_sync import fetch_users, fetch_posts
from app.logger import logger
from app.exceptions import APIError, DataProcessingError


# ---------------- THREADING ----------------
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


# ---------------- MULTIPROCESSING ----------------
def count_items(data, queue, label):
    """
    Count items in a dataset inside a process.
    """
    try:
        logger.info(f"Process: counting {label}")
        queue.put(len(data))
    except Exception as e:
        logger.error(f"Process failed while counting {label}: {e}")
        queue.put(e)



def process_data_with_multiprocessing(users, posts):
    """
    Process data in parallel using multiprocessing.
    """
    queue = Queue()

    p1 = Process(target=count_items, args=(users, queue, "users"))
    p2 = Process(target=count_items, args=(posts, queue, "posts"))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    users_count = queue.get()
    posts_count = queue.get()

    if isinstance(users_count, Exception) or isinstance(posts_count, Exception):
        raise DataProcessingError("Multiprocessing failed during counting")

    logger.info("Multiprocessing: processed data counts successfully")
    return users_count, posts_count
