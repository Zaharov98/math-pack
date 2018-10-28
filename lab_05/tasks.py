
def binary_search(items, elem, middle=None):
    """
    >>> binary_search([1, 2, 3, 4, 5], 4)
    3
    >>> binary_search([], 2)
    -1
    >>> binary_search([1, 2, 3], 1)
    0
    """
    if len(items) <= 0:
        return -1

    start, end = 0, len(items)
    while start <= end:
        middle = int((end + start) / 2)
        if items[middle] < elem:
            start = middle
        elif items[middle] > elem:
            end = middle
        elif items[middle] == elem:
            return middle

    return -1


def quadratic_eq_has_roots(a, b, c):
    """
    >>> quadratic_eq_has_roots(1, 0, 1)
    False
    >>> quadratic_eq_has_roots(1, 2, 1)
    True
    >>> quadratic_eq_has_roots(1, 1, 3)
    False
    """
    discriminant = b**2 - 4 * a * c
    return discriminant >= 0


def max_digit(number: float):
    """
    >>> max_digit(0.230052)
    5
    >>> max_digit(0.0)
    0
    >>> max_digit(-9.0000000019)
    9
    """
    digits = filter(lambda d: d.isdigit(), str(number))
    return max([int(numb) for numb in digits])


def is_polindrome(string: str):
    """
    >>> is_polindrome('123321')
    True
    >>> is_polindrome('111222')
    False
    >>> is_polindrome('')
    True
    """
    return string == string[::-1]


def replace_substring(string: str, old_subs: str, new_subs: str):
    """
    >>> replace_substring('1000222', '000', '!!!')
    '1!!!222'
    >>> replace_substring('12', '9', '4')
    '12'
    """
    return string.replace(old_subs, new_subs)


def max_word(string):
    """
    >>> max_word('hello world, yes!')
    5
    """
    return max((len(word.strip(',.?!')) for word in string.split()))
