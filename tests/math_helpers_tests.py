__author__ = 'aleksander'


import unittest
import helpers.math_helper as mh


class TestPrimeMethods(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(mh.is_prime(1))
        self.assertTrue(mh.is_prime(2))
        self.assertTrue(mh.is_prime(3))
        self.assertFalse(mh.is_prime(4))
        self.assertFalse(mh.is_prime(9))
        self.assertTrue(mh.is_prime(11))
        self.assertTrue(mh.is_prime(1709))
        self.assertTrue(mh.is_prime(5381))
        self.assertTrue(mh.is_prime(8273))

        self.assertFalse(mh.is_prime(3.14))
        self.assertFalse(mh.is_prime([1, 2, 3]))