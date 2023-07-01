import pytz
from datetime import datetime


def main():
    timezone = pytz.timezone('America/New_York')
    aware_datetime = timezone.localize()


if __name__ == "__main__":
    main()
