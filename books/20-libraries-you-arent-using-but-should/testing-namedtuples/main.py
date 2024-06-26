from collections import namedtuple


def main(name, age, mode):
    if 'named' in mode:
        result = _get_named_tuple(name, age)
    else:
        result = name, age
    print(result)
    return result


def _get_named_tuple(name, age):
    tup = namedtuple('Person', 'name age')
    return tup(name=name, age=age)


if __name__ == "__main__":
    name = 'Alexandre'
    age = '24'
    main(name, age, 'named')
