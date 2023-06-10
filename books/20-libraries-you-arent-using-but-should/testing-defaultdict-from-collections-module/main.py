
def main(arg):
    response_without_default_dict = _not_using_default_dict(arg)
    print(response_without_default_dict)
    return True


def _not_using_default_dict(arg):
    return arg


if __name__ == '__main__':
    main('default')
