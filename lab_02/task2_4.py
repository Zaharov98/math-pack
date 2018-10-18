from functools import reduce


def power(number, p):
    """
    :return: number in power of p
    >>> power(2, 4)
    16
    >>> power(4, -1)
    0.25
    >>> power(3, 3)
    27
    >>> power(0, -5)
    0
    """
    if p == 0:
        return 1
    if number == 0:
        return 0

    result = reduce(lambda x, temp: x * temp, (number for _ in range(0, abs(p))))
    return result if p > 0 else 1 / result
