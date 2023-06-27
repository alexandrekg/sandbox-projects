from colorama import init, Fore, Back, Style

# if we don't use autoreset, the second 'blah blah blah' string, will have the same color and background-color
# specified in the second string
# When the code is running on Windows, we still have to use init() for mapping ANSI colors
init(autoreset=True)

messages = [
    'blah blah blah',
    (Fore.LIGHTYELLOW_EX + Style.BRIGHT + Back.MAGENTA + 'Alert!!!'),
    'blah blah blah'
]


def main():
    for m in messages:
        print(m)


if __name__ == "__main__":
    main()
