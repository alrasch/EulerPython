__author__ = 'aleksander'


'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

'''
Strategy: Straight-forward.
'''

from helpers.math.divisibility import Divisibility
from abstract.AbstractSolution import AbstractSolution

class Euler10(AbstractSolution):
    def getSolution(self):
        return 142913828922

    def solve(self):
        div = Divisibility()
        primes = div.get_primes_up_to(2000000)
        sum = 0
        for prime in primes: sum += prime
        return sum
