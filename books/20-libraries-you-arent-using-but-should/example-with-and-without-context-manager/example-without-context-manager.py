from time import perf_counter


def timing_func(func):
    def wrapper(*args, **kwargs):
        t0 = perf_counter()
        result = func(*args, **kwargs)
        t1 = perf_counter()
        print(f"Execution time: {t1 - t0} seconds")
        return result
    return wrapper


@timing_func
def my_function():
    # code to be timed
    print("Executing my function...")
    for i in range(1000000):
        pass


if __name__ == "__main__":
    my_function()
