import sys


def main():
    free, cost = int(input()), int(input())

    print(free // cost, free % cost, file=sys.stdout)


if __name__ == '__main__':
    main()
