import argparse


def main(a, b):
    return a + b


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add two numbers")
    parser.add_argument('-a', help="First value", type=float, default=0)
