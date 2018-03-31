from abstract.AbstractSolution import AbstractSolution
from helpers.math.naturals import Naturals

'''
This problem boils down to having to take 20 steps to the right
and 20 steps down. So you have to perform
RRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDD
but the order does not matter.

The problem can therefore be reduced to
    "How many permutations are there of 20 R's and 20 D's?"
    
From basic combinatorics, the answer to this is
    
    40! / (20! * 20!)
    
where ! signifies the factorial function.

I initially solved this problem by just entering that into
Wolphram|Alpha, but made this rudimentary implementation just
for the sake of completion.
'''

class Euler15(AbstractSolution):
    def getSolution(self): return 137846528820

    def solve(self):
        nat = Naturals()
        answer = nat.factorial(40) / (nat.factorial(20) * nat.factorial(20))
        return int(answer)
