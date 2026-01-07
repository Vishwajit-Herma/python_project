from threading import Thread
from multiprocessing import Process
from app.logger import logger

def task(name):
    logger.info(f"Executing task: {name}")


def run_threading():
    threads = [Thread(target=task, args=(f"Thread-{i}",)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def run_multiprocessing():
    processes = [Process(target=task, args=(f"Process-{i}",)) for i in range(2)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
