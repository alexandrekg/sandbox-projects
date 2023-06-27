from colorama import init, Fore, Back, Style

# if we don't use autoreset, the second 'blah blah blah' string, will have the same color and background-color
# specified in the second string
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
