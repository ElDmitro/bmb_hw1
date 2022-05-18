import sys


ODD_FILLER = '?'


def main():
    name_letters = list(input())
    name_letters[1::2] = [ODD_FILLER] * (len(name_letters) // 2)
    print(''.join(name_letters), file=sys.stdout)


if __name__ == '__main__':
    main()
