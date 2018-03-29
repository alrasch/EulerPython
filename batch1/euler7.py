__author__ = 'aleksander'

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

'''
Strategy: Very straight-forward.
'''

import helpers.math_helper as mh
from abstract.AbstractSolution import AbstractSolution

class Euler7(AbstractSolution):
    def getSolution(self):
        return 104743

    def solve(self, external_call=None):
        return mh.get_nth_prime(10001)
