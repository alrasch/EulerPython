class AbstractSolution:
    def getSolution(self):
        raise NotImplementedError

    def solve(self, external_call = False):
        raise NotImplementedError
