import unittest
from helpers.math.divisibility import Divisibility

class DivisibilityTest(unittest.TestCase):
    def test_is_prime(self):
        div = Divisibility()
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 99991, 999983, 9999991, 99999989]

        for prime in primes:
            self.assertTrue(div.is_prime_2(prime))

    def test_is_not_prime(self):
        div = Divisibility()
        non_primes = [1, 4, 6, 100, 1000, 12349, 987653, 9876533, 99999991]

        for non_prime in non_primes:
            self.assertFalse(div.is_prime_2(non_prime))
