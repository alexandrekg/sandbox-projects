import logging
from argparse import ArgumentParser

logger = logging.getLogger()


def blah():
    return 'blah'


if __name__ == "__main__":
    parser = ArgumentParser(description="My app which is mine")
    parser.add_argument('-ll', '--loglevel',
                        type=str,
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='Set the logging level')
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)
