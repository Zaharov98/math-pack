import math


class EventLoop:
    def __init__(self):
        self.x = None
        self.n = None
        self.m = None
        self.s = ''

    def start(self):
        """ Initialize user interaction loop """
        print('\n')
        self.x = self._input_number(float, 'Input number X from 1 to 9: ')

        if 1 < self.x <= 3:
            self.string_branch()
        elif 3 < self.x <= 6:
            self.power_branch()
        elif 6 < self.x <= 9:
            self.increment_branch()
        else:
            self._print_error()

    def string_branch(self):
        self.s = input('Input any string: ')
        self.n = self._input_number(int, 'Input number N: ')

        print(''.join([self.s for _ in range(0, self.n)]))

    def power_branch(self):
        self.m = self._input_number(int, 'Input power of X: ')
        print(math.pow(self.x, self.m))

    def increment_branch(self):
        for i in range(0, 10):
            self.x += 1
            print(self.x)

    def _input_number(self, number_type, prompt):
        while True:  # input without error
            try:
                x = number_type(input(prompt))
            except ValueError:
                self._print_error()
            except Exception as e:
                print(e)
            else:
                break
        return x

    def _print_error(self):
        print('\tInput Error!')