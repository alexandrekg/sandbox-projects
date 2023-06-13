def main():
    file_name = input('Please input the file name with the extension. Ex: data.txt  ')
    with open(file_name) as file:
        file_data = file.read()
        print(file_data)
    return True


if __name__ == "__main__":
    main()
