__author__ = 'aleksander'


'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

'''
Strategy: Straight-forward.
'''


import helpers.math_helper as mh

primes = mh.get_list_of_primes_up_to(2000000)

sum = mh.sum_of_list(primes)

print("Sum: " + str(sum))