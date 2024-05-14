def main():
    a, b = 0, 1
    while True:
        if b > 50:
            return False
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    for i in main():
        print(i)
