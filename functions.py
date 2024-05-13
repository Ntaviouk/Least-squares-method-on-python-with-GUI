import matplotlib.pyplot as plt
import numpy as np


def gauss(A):
    return np.linalg.solve(A[:, :-1], A[:, -1])


def sum_squares_mismatches(defined, calculated):
    summ = 0
    for i in range(len(defined)):
        summ += abs(abs(defined[i]) - abs(calculated[i])) ** 2
    return summ


def draw(func, roots, x, y, calculated_x, name):
    x_values = np.linspace(min(x) - 20, max(x) + 20, 400)
    y_values = [func(roots[0], roots[1], i) for i in x_values]
    plt.plot(x_values, y_values)
    plt.title(name)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    for i in range(len(x)):
        plt.scatter(x[i], y[i], color="green")

    plt.show()
