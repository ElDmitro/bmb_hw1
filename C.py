import sys


def main():
    uniqs = dict()
    for value in input().strip().split():
        if value in uniqs:
            continue
        uniqs[int(value)] = 1


    print(*uniqs.keys(), file=sys.stdout)


if __name__ == '__main__':
    main()
