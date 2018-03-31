from resources.exceptions.inputexception import InputException


class Naturals:
    collatz_chain = {}

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
        if n == 1: return 0

        if n in self.collatz_chain: return self.collatz_chain[n]

        collatz = self.collatz(n)
        count = 1 + self.collatz_count(collatz)
        self.collatz_chain[n] = count
        return count
