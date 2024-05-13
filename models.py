import math
from abc import ABC, abstractmethod
from functions import sum_squares_mismatches


class AbstractModel(ABC):
    @abstractmethod
    def least_squares(self, x, y):
        pass

    @abstractmethod
    def func(self, a0, a1, x):
        pass

    @abstractmethod
    def reslt(self, a0, a1):
        pass


class Linear(AbstractModel):
    def __init__(self):
        pass

    def least_squares(self, x, y):
        return [[len(x), sum(x), sum(y)], [sum(x), sum(i ** 2 for i in x), sum(i * j for i, j in zip(x, y))]]

    def func(self, a0, a1, x):
        return a0 + a1 * x

    def reslt(self, a0, a1):
        return f"y = {a0:.2f} + {a1:.2f} * x"


class Feedback(AbstractModel):
    def __init__(self):
        pass

    def least_squares(self, x, y):
        return [[len(x), sum(1 / i for i in x), sum(y)],
                [sum(1 / i for i in x), sum(1 / (i ** 2) for i in x), sum(j / i for i, j in zip(x, y))]]

    def func(self, a0, a1, x):
        return a0 + a1 / x

    def reslt(self, a0, a1):
        return f"y = {a0:.2f} + {a1:.2f} / x"


class Hyperbolic(AbstractModel):
    def __init__(self):
        pass

    def least_squares(self, x, y):
        return [[len(x), sum(x), sum(1 / i for i in y)],
                [sum(x), sum(i ** 2 for i in x), sum(i / j for i, j in zip(x, y))]]

    def func(self, a0, a1, x):
        return 1 / (a0 + a1 / x)

    def reslt(self, a0, a1):
        return f"y = 1 / {a0:.2f} + {a1:.2f} / x"


class Squared(AbstractModel):
    def __init__(self):
        pass

    def least_squares(self, x, y):
        return [[len(x), sum(i ** 2 for i in x), sum(y)],
                [sum(i ** 2 for i in x), sum(i ** 4 for i in x), sum(j * i ** 2 for i, j in zip(x, y))]]

    def func(self, a0, a1, x):
        return a0 + a1 * x ** 2

    def reslt(self, a0, a1):
        return f"y = {a0:.2f} + {a1:.2f} * x ^ 2"


class Rational(AbstractModel):
    def __init__(self):
        pass

    def least_squares(self, x, y):
        return [[len(x), sum(x), sum(i / j for i, j in zip(x, y))],
                [sum(x), sum(i ** 2 for i in x), sum((i ** 2) / j for i, j in zip(x, y))]]

    def func(self, a0, a1, x):
        return x / (a0 + a1 * x)

    def reslt(self, a0, a1):
        return f"y = x / {a0:.2f} + {a1:.2f} * x"


class Resoult():
    def __init__(self):
        self.x = []
        self.y = []
        self.calculated_y = []
        self.least_squares = None
        self.roots = None
        self.summ = None
        self.func = None
        self.res = None

    def sum_squares_mismatches(self):
        self.summ = 0
        for i in range(len(self.x)):
            self.summ += abs(abs(self.y[i]) - abs(self.calculated_y[i])) ** 2
            # self.summ += abs(abs(self.y[i]) - abs(self.func(self.roots[0], self.roots[1], self.calculated_x[i]))) ** 2

    def get_info(self):
        info = ""
        info += f"x: {self.x}\n"
        info += f"y: {self.y}\n"
        info += f"calculated_y: {self.calculated_y}\n"
        info += f"least_squares: {self.least_squares}\n"
        info += f"roots: {self.roots}\n"
        info += f"summ: {self.summ}\n"
        info += f"func: {self.func}\n"
        info += f"res: {self.res}\n"
        return info

    def clear(self):
        self.calculated_y = []
        self.least_squares = None
        self.roots = None
        self.summ = None
        self.func = None
        self.res = None
