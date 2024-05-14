def range_step(start, stop, step):
    a = start
    while a < stop:
        yield a
        a += step


if __name__ == "__main__":
    for i in range_step(0, 50, 5):
        print(i)
