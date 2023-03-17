"""
This process uses an I/O-bound web query to demonstrate GIL interference in
multithreading.
"""

from threading import Thread
import time

import requests

def do_query(url : str) -> int:
    """ Do a query and get the response code """
    response = requests.get(url)
    return response.status_code

def show_code(url : str) -> None:
    """ Show a response code """
    print(f"CODE={do_query(url)}")

def query_no_threading(url : str, count : int) -> None:
    """ Query with no threading """
    start = time.time()
    for _trial in range(count):
        show_code(url)
    end = time.time()
    print(f"Non-threaded: {end - start:.4f} seconds")

def query_threading(url : str, count : int) -> None:
    """ Query with threading """
    threads = {}
    start = time.time()
    for trial in range(count):
        new_thread = Thread(target=show_code, args=[url])
        new_thread.start()
        threads[trial] = new_thread
    for query_thread in threads.values():
        query_thread.join()
    end = time.time()
    print(f"Threaded: {end - start:.4f} seconds")

if __name__ == '__main__':
    URL = 'http://www.google.com'
    COUNT = 5

    print("\nNo threads:")
    query_no_threading(URL, COUNT)

    print("\nThreads:")
    query_threading(URL, COUNT)
