"""
Implements a decorator to time a coroutine.
"""

import functools
import time
from typing import Any, Callable

def timed():
    """ Duration timer decorator """
    def wrapper(func: Callable) -> Callable:
        """ Wrap the timed function"""
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            """ Time a function """
            print(f"Start: {func}: args={args} kwargs={kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"Finish: {func}: time={total:.4f}")
        return wrapped
    return wrapper
