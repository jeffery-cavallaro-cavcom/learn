"""
This process uses a compute-bound (inefficient, brute force) Fibonacci
algorithm to demonstrate GIL interference in multithreading.
"""

from threading import Thread
import time

def fib(number : int) -> int:
    """ Calculate the nth Fibonacci number """
    if number <= 1:
        answer = 0
    elif number == 2:
        answer = 1
    else:
        answer = fib(number - 1) + fib(number - 2)
    return answer

def show_fib(number : int) -> None:
    """ Calulate and show a Fibonacci number """
    print(f"Fib({number}) = {fib(number)}")

def fibs_no_threading(*numbers : list[int]) -> None:
    """ Calculate with no threading """
    start = time.time()
    for number in numbers:
        show_fib(number)
    end = time.time()
    print(f"Non-threaded: {end - start:.4f} seconds")

def fibs_threading(*numbers : list[int]) -> None:
    """ Calculate with threading """
    threads = {}
    start = time.time()
    for number in numbers:
        new_thread = Thread(target=show_fib, args=[number])
        new_thread.start()
        threads[number] = new_thread
    for fib_thread in threads.values():
        fib_thread.join()
    end = time.time()
    print(f"Threaded: {end - start:.4f} seconds")

if __name__ == '__main__':
    print("\nNo threads:")
    fibs_no_threading(40, 41)

    print("\nThreads:")
    fibs_threading(40, 41)
