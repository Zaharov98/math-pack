
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process


def _display_plot(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, 'o', dashes=[6, 2])
    plt.show()


def display_plot_async(x, y):
    """ Run pyplot window in another process """
    process = Process(target=_display_plot, args=(x, y))
    process.start()


def main():
    size = 10
    x = np.random.normal(loc=0, scale=1, size=size)
    y = np.random.normal(loc=0, scale=1, size=size)

    _display_plot(sorted(x), y)


if __name__ == '__main__':
    main()
