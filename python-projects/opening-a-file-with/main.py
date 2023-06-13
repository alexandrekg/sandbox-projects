def main():
    file_name = input('Please input the file name with the extension. Ex: data.txt  ')
    with open(file_name) as file:
        file_data = file.readlines()
        total_lines = len(file_data)
        total_words = len([word for row in file_data for word in row.split(" ")])
        total_characters = len(file_data)
        print("Line count: ", total_lines)
    return True


if __name__ == "__main__":
    main()
