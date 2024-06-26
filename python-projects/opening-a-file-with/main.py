def main():
    file_name = input('Please input the file name with the extension. Ex: data.txt  ')
    with open(file_name) as file:
        file_data = file.readlines()
        total_lines = len(file_data)
        total_words = len([word for row in file_data for word in row.split(" ")])
        total_characters = len("".join(file_data).replace("\n", " "))
        print("Line count: ", total_lines)
        print("Word count: ", total_words)
        print("Character count: ", total_characters)


if __name__ == "__main__":
    main()
