import argparse


def main(a, b):
    return a + b


if __name__ == "__main__":
    # example: python argparse_example.py -a 3 -b 5
    parser = argparse.ArgumentParser(description="Add two numbers")
    parser.add_argument('-a', help="First value", type=float, default=0)
    parser.add_argument('-b', help="Second value", type=float, default=0)
    args = parser.parse_args()
    print(main(args.a, args.b))
