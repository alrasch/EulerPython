__author__ = 'aleksander'


'''
Problem 2:
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''

from abstract.AbstractSolution import AbstractSolution

class Euler2(AbstractSolution):

    def getSolution(self):
        return 4613732

    def solve(self):
        fibs = [1, 1]

        nextfibref = 2
        nextfib = 0
        sum = 0

        while nextfib <= 4000000:
            nextfib = fibs[nextfibref-2] + fibs[nextfibref-1]
            if nextfib % 2 == 0:
                sum += nextfib
            fibs.append(nextfib)
            nextfibref += 1

        return sum
