from abstract.AbstractSolution import AbstractSolution
from helpers.math.naturals import Naturals

class Euler14(AbstractSolution):
    def getSolution(self): return 837799

    def solve(self):
        nat = Naturals()

        high_count = 0
        candidate = 0

        for i in range(2, 10**6):
            count = nat.collatz_count(i)

            if count > high_count:
                high_count = count
                candidate = i

        return candidate
