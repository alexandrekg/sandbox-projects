import sys


def main():
    my_name = sys.argv[1]
    script_name = sys.argv[0]

    print(f'{script_name} running by {my_name}')


main()

"""
[master][~/workspace/sandbox-projects/python-projects/getting-args-using-sys]$ python example-with-method.py Alexandre
example-with-method.py running by Alexandre
"""