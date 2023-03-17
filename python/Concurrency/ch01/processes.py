""" Reports information about the main thread """

import multiprocessing as mp
import time

# pylint: disable=invalid-name

class HelloProcess(mp.Process):
    """ A Hello World Process """
    def run(self) -> None:
        """ Say hello """
        name = f"{self.name}({self.pid})"
        print(f"Hello from {name}!")
        time.sleep(5)
        print(f"{name} exiting")

def main() -> None:
    """ Run the parent process """
    hello_process = HelloProcess()
    hello_process.start()

    current = mp.current_process()
    name = f"{current.name}({current.pid})"
    count = len(mp.active_children())

    print(f"{name}: CHILDREN={count}")

    print(f"Waiting for {hello_process.name}({hello_process.pid}) to exit")
    hello_process.join()
    print(f"{name} exiting")

if __name__ == '__main__':
    main()
