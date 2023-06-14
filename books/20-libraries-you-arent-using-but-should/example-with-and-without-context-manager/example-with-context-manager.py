from time import perf_counter
from contextlib import contextmanager


@contextmanager
def timing():
    t0 = perf_counter()
    yield
    t1 = perf_counter()
    print(f"Execution time: {t1 - t0} seconds")


def my_function():
    print("Executing my_function...")
    for i in range(1000000):
        pass


with timing():
    my_function()
