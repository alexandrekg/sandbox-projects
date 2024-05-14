import parsedatetime as pdt


def main():
    cal = pdt.Calendar()
    examples = [
        "2016-07-16",
        "2016/07/16",
        "2016-7-16",
        "07-16-2016",
        "7-16-2016",
        "7-16-16",
        "7/16/16",
    ]

    print('{:30s}{:>30s}'.format('Input', 'Result'))
    print('=' * 60)
    for e in examples:
        dt, result = cal.parseDT(e)
        print('{:30s}{:>30s}'.format('"' + e + '"', dt.ctime()))


if __name__ == "__main__":
    main()
