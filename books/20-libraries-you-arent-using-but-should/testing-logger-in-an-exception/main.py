import logging
logger = logging.getLogger()


def main():
    try:
        1/0
    except:
        logger.exception("Something failed:")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
