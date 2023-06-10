
def main(arg):
    if 'not' in arg:
        response = _not_using_default_dict(arg)
    else:
        response = _using_default_dict(arg)

    print(response)
    return True


def _not_using_default_dict(arg):
    return arg


def _using_default_dict(arg):
    return True


if __name__ == '__main__':
    main('not default')
