__author__ = 'Aleks'


'''
A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import helpers.string_helper as sh

class Euler4:
    def getSolution(self):
        return 906609

    def solve(self):
        highest = 0
        for x in range(999, 100, -1):
            for y in range(999, 100, -1):
                product = x * y
                string = str(product)
                if sh.is_palindrome(string) and int(string) > highest:
                    highest = int(string)
        return highest
