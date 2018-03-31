from abstract.AbstractSolution import AbstractSolution

class Euler16(AbstractSolution):
    def getSolution(self): return 1366

    def solve(self):
        return sum([int(x) for x in str(2**1000)])
