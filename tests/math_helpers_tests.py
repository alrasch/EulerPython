__author__ = 'aleksander'


import unittest
import helpers.math_helper as mh


class TestPrimeMethods(unittest.TestCase):

    def test_is_prime(self):

        true_cases = [2, 3, 11, 1709, 5381, 8273]
        false_cases = [1, 4, 3.14, [1, 2, 3]]

        for true_case in true_cases:
            self.assertTrue(mh.is_prime(true_case))
        for false_case in false_cases:
            self.assertFalse(mh.is_prime(false_case))