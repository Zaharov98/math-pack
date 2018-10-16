
def fibonacci():
    left, right = 0, 1
    while True:
        yield left
        left, right = right, left + right


def main():
    print('\tFibonacci')
    for _, fibonacci_number in zip(range(0, 100), fibonacci()):
        print(fibonacci_number)


if __name__ == '__main__':
    main()
