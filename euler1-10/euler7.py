__author__ = 'aleksander'

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

'''
Strategy: Very straight-forward.
'''

import helpers.math_helper as mh

print(mh.get_nth_prime(10001))
