from collections import Counter


def main():
    item_counter = Counter()
    with open('input.txt') as input_stream:
        for line in input_stream:
            for word in line.strip().split(','):
                item_counter[word] += 1

    with open('output.txt', 'w') as output_stream:
        output_stream.write(item_counter.most_common(1).pop()[0] + '\n')

if __name__ == '__main__':
    main()
