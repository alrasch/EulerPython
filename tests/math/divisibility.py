
import unittest
import helpers.math.divisibility as div

class DivisibilityTest(unittest.TestCase):
    def test_is_prime(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

        for prime in primes:
            self.assertTrue(div.is_prime(prime))

    def test_is_not_prime(self):
        non_primes = [1, 4, 6, 100, 1000, 10000, 100000]

        for non_prime in non_primes:
            self.assertFalse(div.is_prime(non_prime))
