from threading import Thread
from multiprocessing import Process, Queue
from app.api_sync import fetch_users, fetch_posts
from app.logger import logger


# ---------------- THREADING ----------------
def fetch_users_thread(result):
    logger.info("Thread: fetching users")
    result["users"] = fetch_users()


def fetch_posts_thread(result):
    logger.info("Thread: fetching posts")
    result["posts"] = fetch_posts()


def fetch_data_with_threads():
    """
    Fetch users and posts concurrently using threads
    """
    shared_result = {}

    t1 = Thread(target=fetch_users_thread, args=(shared_result,))
    t2 = Thread(target=fetch_posts_thread, args=(shared_result,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    logger.info("Threading: fetched users and posts")
    return shared_result


# ---------------- MULTIPROCESSING ----------------
def count_items(data, queue, label):
    """
    CPU-bound task: count items
    """
    logger.info(f"Process: counting {label}")
    queue.put(len(data))


def process_data_with_multiprocessing(users, posts):
    """
    Process data in parallel using processes
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

    logger.info("Multiprocessing: processed data counts")

    return users_count, posts_count
