from resources.exceptions.inputexception import InputException


class Naturals:
    def validate_natural(self, input):
        if not isinstance(input, int):
            raise InputException("Input {} is not natural.".format(input))

    def factorial(self, n):
        if n == 1: return 1

        return n * self.factorial(n - 1)

    def collatz(self, n):
        if n % 2 == 0:
            return (n / 2)

        return (3 * n + 1)

    def collatz_count(self, n):
        steps = 0

        while n > 1:
            n = self.collatz(n)
            steps += 1

        return steps
