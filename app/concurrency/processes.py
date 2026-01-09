from multiprocessing import Process, Queue
from app.utils.logger import logger
from app.utils.exceptions import DataProcessingError

def count_items(data, queue, label):
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
