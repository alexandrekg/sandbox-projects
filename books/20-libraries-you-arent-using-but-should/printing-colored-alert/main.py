from colorama import init, Fore, Back, Style
init(autoreset=True)

messages = [
    'blah blah blah',
    (Fore.LIGHTYELLOW_EX + Style.BRIGHT + Back.MAGENTA + 'Alert!!!'),
    'blah blah blah'
]

def main():
    print('Hello World')


if __name__ == "__main__":
    main()
