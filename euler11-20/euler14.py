from abstract.AbstractSolution import AbstractSolution
from helpers.math.naturals import Naturals

class Euler14(AbstractSolution):
    def getSolution(self): return 837799

    def solve(self):
        nat = Naturals()

        high_count = 0
        candidate = 0

        already_collatzed = [0] * (10**6 + 1)
        for i in range(10**6, 2, -1):
            if already_collatzed[i] != 0:
                count = already_collatzed[i]
            else:
                count = nat.collatz_count(i)
                already_collatzed[i] = count

            if count > high_count:
                high_count = count
                candidate = i
        return candidate
