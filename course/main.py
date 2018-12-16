
import sys
import math
import functools
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import mpl_toolkits.axisartist as AA


lamb_positive = [[3, 4]]   # интенсивность входного потока положительных заявок
lamb_negative = [[1, 0.02]]   # интенсивность входного потока отрицательных заявок
p_positive = [[0.3, 0.22], [0.144, 0.98], [0.176, 0.6]]  # вероятность перехода положительных заявок
p_negative = [[1, 0.1], [0.4, 0.654], [0.45, 0.54]]  # вероятность перехода отрицательных заявок
mu = [5, 5]                # интенсивность обслуживания заявок

alp = [2, 4]               # начальное состояние сети

# lamb_positive = [[2]]
# lamb_negative = [[3]]
# p_positive = [[1, 1], [1, 1]]
# p_negative = [[1, 1], [1, 1]]
# mu = [2]
# alp = [1]


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
        seq_element = get_seq_item(t)

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


def get_seq_item(t: float) -> float:
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
    return numerator(i) / denominator(i)


def numerator(i: int):
    """ :returns Numerator from multiplication row"""
    return (
        math.pow(lamb_positive[0][i], l[-1])
        * math.pow(mu[i] * p_positive[i][0] + lamb_negative[0][i], l[i] + U(i) - R(i))
        * math.pow(mu[i], r[i] + u[i])
        * functools.reduce(
                lambda acc, item: acc * item,
                (p_positive[i][j] for j in range(1, n)))
        * functools.reduce(
                lambda acc, item: acc * item,
                (p_negative[i][j] for j in range(1, n)))
    )


def denominator(i: int):
    """ :returns Denominator from multiplication row"""
    return (
        math.factorial(l[i])
        * math.factorial(l[i] + U(i) - R(i))
        * math.factorial(r[i])
        * math.factorial(u[i])
    )


def U(i):
    return sum((r[j] if j != i else 0 for j in range(1, n)))


def R(i):
    return sum((u[j] if j != i else 0 for j in range(1, n)))


def display_plot(t, s):
    fig = plt.figure(1)
    ax = AA.Subplot(fig, 1, 1, 1)
    fig.add_subplot(ax)

    ax.axis["top", "right"].set_visible(False)
    ax.axis["bottom"].set_axisline_style("->", size=1.5)
    ax.axis["left"].set_axisline_style("->", size=1.5)

    f = interpolate.interp1d(t, s, kind='cubic')
    x_interp = np.arange(min(t), max(t), 0.01)
    ax.plot(x_interp, f(x_interp))
    plt.show()


def main():
    t_row = np.arange(0, 1, 0.1)
    s_row = [get_state_probability(t) for t in t_row]
    display_plot(t_row, s_row)


if __name__ == '__main__':
    main()
