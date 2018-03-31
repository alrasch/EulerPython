__author__ = 'Aleks'

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

'''
Strategy: All integers up to 20 can be factored into primes.
If we find the largest holder of each factor, we only need that number of each prime.
'''

from abstract.AbstractSolution import AbstractSolution

class Euler5(AbstractSolution):
    def getSolution(self):
        return 232792560

    def solve(self):
        return (2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)
