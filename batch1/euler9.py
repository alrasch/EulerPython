__author__ = 'aleksander'

import math
import helpers.math_helper as mh
from abstract.AbstractSolution import AbstractSolution

class Euler9(AbstractSolution):
    def getSolution(self):
        return 31875000

    def solve(self):
        for a in range(1, 1000):
            for b in range(1, 1000):
                c = math.sqrt(a**2 + b**2)
                if a+b+c == 1000:
                    return mh.product_of_list([a, b, c])
