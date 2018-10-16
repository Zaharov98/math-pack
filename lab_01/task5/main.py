
import math
import common.input


def get_fibonacci_bine(index: int):
    return (math.pow((1 + math.sqrt(5)) / 2, index) - math.pow((1 - math.sqrt(5)) / 2, index)) / math.sqrt(5)


def main():
    fibonacci_numb_index = common.input.input_number(int, 'Input fibonacci number index: ')
    if fibonacci_numb_index < 0:
        raise ValueError

    fibonacci_number = get_fibonacci_bine(fibonacci_numb_index)
    print(fibonacci_number)


if __name__ == '__main__':
    main()
