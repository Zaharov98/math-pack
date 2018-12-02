
from itertools import chain


def main():
    file_name = 'data.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines_count = len(lines)

        words = list(chain.from_iterable([line.split() for line in lines]))
        words_count = len(words)

        letters_count = sum([len(word) for word in words])

    print('Lines: {0}\nWords: {1}\nLetters: {2}'.format(lines_count, words_count, letters_count))


if __name__ == '__main__':
    main()
