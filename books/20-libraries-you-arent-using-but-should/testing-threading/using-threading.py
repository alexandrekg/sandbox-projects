import threading
import time


def work():
    return sum(x for x in range(100))


if __name__ == "__main__":
    t0 = time.time()

    thread = threading.Thread(target=work)
    thread.start()
    thread.join()

    result = thread.result()
    print(result)

    t1 = time.time()
    result = t1 - t0
    print(result)
