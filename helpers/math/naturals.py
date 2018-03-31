from resources.exceptions.inputexception import InputException

class Naturals:
    def validate_natural(self, input):
        if not isinstance(input, int):
            raise InputException("Input {} is not natural.".format(input))

    def factorial(self, n):
        if n == 1: return 1

        return n * self.factorial(n-1)
