
def main(name):
    my_dict = {'Joanny': 25, 'Leonard': 43, 'Giovanni': 15}
    print('My dict before using setdefault ...')
    my_dict.setdefault(name, 0)
    print('My dict after using setdefault: \n', my_dict)


if __name__ == "__main__":
    main('Alex')
