import threading
import time


class WorkThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._result = None

    def run(self):
        self._result = sum(x for x in range(100))

    def result(self):
        return self._result


if __name__ == "__main__":
    t0 = time.time()

    thread = WorkThread()
    thread.start()
    thread.join()

    result = thread.result()
    print(result)

    t1 = time.time()
    result = t1 - t0
    print(result)
