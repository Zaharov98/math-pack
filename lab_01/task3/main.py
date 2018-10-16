
import common.input


def get_factorial_loop(number: int):
    if not 0 <= number <= 100:
        raise ValueError

    factorial = 1
    for i in range(2, number + 1):
        factorial *= i

    return factorial


def main():
    number = common.input.input_number(int, 'Input int from 0 to 100: ')
    factorial = get_factorial_loop(number)

    print('Factorial: ', factorial)


if __name__ == '__main__':
    main()
