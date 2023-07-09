import array


def main():
    n = int(1e8)
    a = array.array('d', [0, 0]) * n

    for i in range(n):
        a[i] = i % 3

    print(a[:5])


if __name__ == "__main__":
    main()

"""
~/Documents/workspace/sandbox-projects/books/20-libraries-you-arent-using-but-should/testing-cython (develop) » time python slow-code.py                                                                                alexkg@alexkg-MS-7A39
array('d', [0.0, 1.0, 2.0, 0.0, 1.0])
python slow-code.py  6,48s user 0,47s system 100% cpu 6,953 total
"""