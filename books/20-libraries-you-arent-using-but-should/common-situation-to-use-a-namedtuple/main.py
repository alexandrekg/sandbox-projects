def main():
    name = "Alex"
    birth_year = 1999
    current_year = 2023
    current_role = 'Developer'

    normal_tuple_response = _get_normal_tuple_response(name, birth_year, current_year, current_role)
    print(normal_tuple_response)
    named_tuple_response = _get_named_tuple_response(name, birth_year, current_year, current_role)
    print(named_tuple_response)


if __name__ == "__main__":
    main()
