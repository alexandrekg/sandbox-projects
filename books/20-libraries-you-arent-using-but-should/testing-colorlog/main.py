import colorlog

# specifying log level as DEBUG
logger = colorlog.getLogger()
logger.setLevel(colorlog.DEBUG)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)


def main():
    logger.debug("Debug message")
    logger.info("Information message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")


if __name__ == "__main__":
    main()
