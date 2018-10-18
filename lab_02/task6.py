
def fib(index: int):
    """
    :return: fibonacci number with index 'index'
    >>> fib(3)
    2
    >>> fib(6)
    8
    >>> fib(0)
    0
    """
    if index < 0:
        raise ValueError

    if index == 0:
        return 0
    elif index == 1:
        return 1

    return fib(index - 1) + fib(index - 2)
