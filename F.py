import sys


MONTHS = [
    'январь',
    'февраль',
    'март',
    'апрель',
    'май',
    'июнь',
    'июль',
    'август',
    'сентябрь',
    'октябрь',
    'ноябрь',
    'декабрь',
]


def main():
    day, month, year = input().strip().split('.')
    month_repr = MONTHS[int(month) - 1]

    print(
        f'{int(day):02d}', year, month_repr, month_repr[:3].upper(),
        sep='\n', file=sys.stdout
    )


if __name__ == '__main__':
    main()
