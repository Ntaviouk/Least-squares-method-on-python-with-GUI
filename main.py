from copy import copy
import random
import numpy as np

from functions import gauss

from functions import draw

from models import Linear
from models import Feedback
from models import Hyperbolic
from models import Resoult
from models import Squared
from models import Rational


def main():
    random_generator = random.Random()

    r = Resoult()
    result = Resoult()
    models = [Linear(), Feedback(), Hyperbolic(), Squared(), Rational()]

    # Test_Example_1
    # r.x = [i for i in range(-21, 20, 2)]
    # r.y = [(5 + 8 * x ** 2) + random_generator.uniform(-20.95, 25.95) for x in r.x]

    # Test_Example_2
    # r.x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
    # 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    # r.y = [7, 4.1, 2.6, 1.5, 0.8, 0.3, -0.1, -0.4, -0.6, -0.8, -1,
    # -1.1, -1.3, -1.4, -1.5, -1.6, -1.6, -1.7, -1.8, -1.8, -1.9, -1.9, -2, -2, -2.1, -2.1, -2.1, -2.2, -2.2, -2.2,
    # -2.2, -2.3, -2.3, -2.3, -2.3, ]

    N = int(input("Введіть N: "))
    for i in range(N):
        r.x.append(int(input("x = ")))
    for i in range(N):
        r.y.append(int(input(f"y({r.x[i]}) = ")))

    for model in models:
        r.least_squares = model.least_squares(r.x, r.y)
        r.roots = gauss(np.array(r.least_squares))

        for i in r.x:
            r.calculated_y.append(model.func(r.roots[0], r.roots[1], float(i)))

        r.res = model.reslt(r.roots[0], r.roots[1])
        r.func = model.func
        r.sum_squares_mismatches()
        print(r.summ)

        if result.summ is None or result.summ > r.summ:
            result = copy(r)
            r.clear()

        r.clear()

    return result


if __name__ == "__main__":
    res = main()
    print(res.get_info())
    draw(res.func, res.roots, res.x, res.y, res.calculated_y, res.res)
