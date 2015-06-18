__author__ = 'aleksander'

import math
import helpers.math_helper as mh


def solve9():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = math.sqrt(a**2 + b**2)
            if a+b+c == 1000:
                print(str(a) + " + " + str(b) + " + " + str(c) + " = " + str(a+b+c))
                return [a, b, c]

print(mh.product_of_list(solve9()))