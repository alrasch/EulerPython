__author__ = 'aleksander'


'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from abstract.AbstractSolution import AbstractSolution
from helpers.math.divisibility import Divisibility

class Euler3(AbstractSolution):

    def getSolution(self):
        return 6857

    def solve(self):
        product = 600851475143
        largest_factor = 0

        '''
        Strategy: Check if the product is divisible by small numbers n.
        If product is divisible by n, and n is prime, reduce product by a factor of n.
        Repeat until product has been reduced to 1, then break. The last (i) of the for loop
        will be the largest prime factor of the product.
        '''
        div = Divisibility()
        for i in range(2, int((product+1)/2)+1):
            #Check for divisibility by (i)
            if product % i == 0 and div.is_prime(i):

                #Reduce product by a factor of (i)
                product /= i

                if i > largest_factor:
                    largest_factor = i

                #Check if all prime factors have been found
                if product == 1:
                    break

        return largest_factor
