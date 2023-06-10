from collections import namedtuple


def main():
    name = "Alex"
    birth_year = 1999
    current_year = 2023
    current_role = 'Developer'

    normal_tuple_response = _get_normal_tuple_response(name, birth_year, current_year, current_role)
    print(normal_tuple_response)
    named_tuple_response = _get_named_tuple_response(name, birth_year, current_year, current_role)
    print(named_tuple_response)


def _get_normal_tuple_response(name, birth_year, current_year, current_role):
    age = _calc_age(birth_year, current_year)
    return name, age, current_role


def _get_named_tuple_response(name, birth_year, current_year, current_role):
    my_age = _calc_age(birth_year, current_year)
    tup = namedtuple('Person', 'name age role')
    return tup(name=name, age=my_age, role=current_role)


def _calc_age(birthday_year, current_year):
    return current_year - birthday_year


if __name__ == "__main__":
    main()
