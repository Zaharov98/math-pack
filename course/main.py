
import sys
import math
import itertools
import functools
import numpy as np

lamb_positive = [[2, 3]]  # интенсивность входного потока положительных заявок
lamb_negative = [[3, 4]]  # интенсивность входного потока отрицательных заявок
mu = [1, 2]               # интенсивность обслуживания заявок

alp = [1, 1]              # начальное состояние сети


n = len(alp)
l = np.zeros(len(alp))
r = np.zeros(len(alp))
u = np.zeros(len(alp))


def get_active_vector(active) -> np.array:
    if active is u:
        return (n - 1), r
    elif active is r:
        return (n - 1), l

    return None, None


def get_state_probability(t: float, fault=0.001) -> float:
    active_vector = u
    active_index = n - 1

    previous_sum = sys.float_info.max
    current_sum = 0

    while True:
        seq_element = get_seq_item(t, active_vector, active_index)

        current_sum += seq_element
        if abs(current_sum - previous_sum) <= fault:
            active_index, active_vector = get_active_vector(active_vector)
            if active_vector is None:
                return get_a_coef(t) * current_sum

        active_vector[active_index] += 1
        previous_sum = current_sum


def get_a_coef(t: float) -> float:
    return math.exp(
        - sum((lamb_positive[0][i] + lamb_negative[0][i] + mu[i] for i in range(1, n)))
        * t
    )


def get_seq_item(t: float, active_vector: np.array, active_index: int) -> float:
    """ :returns t in special pow in multiplier from formula"""
    return math.pow(t, get_power()) * get_seq_item_multiplier()


def get_power() -> float:
    return sum(
        (l[i] + r[i] + u[i] + alp[i] for i in range(1, n))
    )


def get_seq_item_multiplier() -> float:
    return functools.reduce(
        lambda acc, item: acc * item,
        (get_multiplier(i) for i in range(1, n))
    )


def get_multiplier(i: int) -> float:
    return i


def main():
    get_state_probability(1)


if __name__ == '__main__':
    main()
