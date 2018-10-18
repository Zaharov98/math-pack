
import math


def distance(x1, y1, x2, y2):
    """
    :return: distance between two points (x1, y1) (x2, y2)

    >>> distance(0, 0, 3, 0)
    3.0
    >>> distance(1, 4, 3, 4)
    2.0
    """
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
