import arrow


def main():
    t0 = arrow.now()
    print(t0)

    t1 = arrow.utcnow()
    print(t1)


if __name__ == "__main__":
    main()