""" Reports information about the main thread """

import os
import threading
import time

# pylint: disable=invalid-name

class HelloThread(threading.Thread):
    """ A Hello World Thread """
    def run(self) -> None:
        """ Say hello """
        print(f"Hello from {self.name}!")
        time.sleep(5)
        print(f"{self.name} terminating")

def main() -> None:
    """ Run the main thread """
    hello_thread = HelloThread()
    hello_thread.start()

    pid = os.getpid()
    current = threading.current_thread()
    count = threading.active_count()

    print(f"PID: {pid}: THREADS={count}, NAME={current.name}")

    print(f"Waiting for {hello_thread.name} to terminate")
    hello_thread.join()
    print(f"{current.name} terminating")

if __name__ == '__main__':
    main()
