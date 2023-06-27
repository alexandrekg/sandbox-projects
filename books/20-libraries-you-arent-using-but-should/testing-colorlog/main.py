import colorlog

# specifying log level as DEBUG
logger = colorlog.getLogger()
logger.setLevel(colorlog.DEBUG)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)


def main():
    print('Hi')


if __name__ == "__main__":
    main()
