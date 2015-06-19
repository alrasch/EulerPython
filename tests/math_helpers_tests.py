import datetime

__author__ = 'aleksander'


import unittest
import helpers.math_helper as mh


class TestPrimeMethods(unittest.TestCase):

    def test_is_prime(self):

        start = datetime.datetime.now()

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

        end = datetime.datetime.now()
        timedelta = end-start

        print("is_prime, execution time: ", timedelta.microseconds, " µs")

    def test_get_nth_triangle_number(self):
        start = datetime.datetime.now()

        self.assertEqual(28, mh.get_nth_triangle_number(7))
        self.assertEqual(5050, mh.get_nth_triangle_number(100))

        end = datetime.datetime.now()
        timedelta = end-start

        print("get_nth_triangle_number, execution time: ", timedelta.microseconds, " µs")

    def test_get_all_divisors(self):
        start = datetime.datetime.now()
        self.assertEqual([1, 2, 4], mh.get_all_divisors(4))
        self.assertEqual([1, 2, 5, 10, 25, 50], mh.get_all_divisors(50))
        self.assertEqual([1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000], mh.get_all_divisors(1000))
        end = datetime.datetime.now()
        timedelta = end-start
        print("get_all_divisors, execution time: ", timedelta.seconds, " sec, ", timedelta.microseconds, "µs")