
def foo(numbers: list):
    """
    >>> foo([1, 2, 3, 0])
    [0, 3, 2, 1]
    >>> foo([])
    []
    >>> foo([2, 0])
    [0, 2]
    """

    def bar(step):
        if numbers[step] != 0:
            bar(step + 1)

        inverse_list.append(numbers[step])

    if len(numbers) == 0:
        return []

    inverse_list = []
    bar(0)

    return inverse_list
