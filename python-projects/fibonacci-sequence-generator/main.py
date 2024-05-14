from collections import deque


def main():
    count = 0
    starter = deque((0, 1))
    while max(starter) < 50:
        if count == 0:
            yield starter[0]
            count += 1

        yield starter[1]

        starter.append(sum(starter))
        starter.popleft()


if __name__ == "__main__":
    for i in main():
        print(i)
