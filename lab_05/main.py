

def main():
    file_name = 'data.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines_count = len(lines)

        letters_count = sum([len(line) for line in lines])

    print('Lines: {0}\nLetters: {1}'.format(lines_count, letters_count))


if __name__ == '__main__':
    main()
