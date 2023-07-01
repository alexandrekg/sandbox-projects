import arrow


def main():
    t0 = arrow.now()
    print(t0)

    t1 = arrow.utcnow()
    print(t1)

    difference = (t0 - t1).total_seconds()

    print('Total difference: %.2f seconds' % difference)


if __name__ == "__main__":
    main()
