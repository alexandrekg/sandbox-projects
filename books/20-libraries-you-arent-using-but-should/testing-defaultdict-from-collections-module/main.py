from collections import defaultdict


def main(arg):
    if 'not' in arg:
        response = _not_using_default_dict(arg)
    else:
        response = _using_default_dict(arg)

    print(response)
    return True


def _not_using_default_dict(arg):
    d = {}
    return d[arg]


def _using_default_dict(arg):
    d = defaultdict(list)
    return d[arg]


if __name__ == '__main__':
    main('default')
