from datetime import datetime, timedelta


def naive_date():
    naive_datetime = datetime(2023, 7, 1, 12, 0, 0)
    print(naive_datetime)


def calc_with_naive_datetime():
    print('----------------------')
    print('Calc with naive datetime')
    naive_datetime = datetime(2023, 7, 1, 12, 0, 0)
    print('Before         ', naive_datetime)
    new_naive_datetime = naive_datetime + timedelta(hours=3)
    print('After          ', new_naive_datetime)


if __name__ == "__main__":
    naive_date()
    calc_with_naive_datetime()