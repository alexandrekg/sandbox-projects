import pytz
from datetime import datetime


def main():
    timezone = pytz.timezone('America/New_York')
    aware_datetime = timezone.localize(datetime(2023, 7, 1, 12, 0, 0))
    print(aware_datetime)


def calc_with_timezone_example():
    timezone = pytz.timezone('America/New_York')
    aware_datetime = timezone.localize(datetime(2023, 7, 1, 12, 0, 0))
    print(aware_datetime)


if __name__ == "__main__":
    print('Aware object example')
    main()
    print('-----------------------')
    print('Calculating dates and times with aware objects')
    calc_with_timezone_example()
