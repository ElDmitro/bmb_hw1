import sys


def main():
    line = input().strip()

    rev_sents = list()
    for sent in line.split('.'):
        words = sent.strip().split()
        words = [word.lower() for word in words]
        rev_sents.append(' '.join(words[::-1]).capitalize())

    print('. '.join(rev_sents), file=sys.stdout)


if __name__ == '__main__':
    main()
