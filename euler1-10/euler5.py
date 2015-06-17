__author__ = 'Aleks'

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

'''
Strategy: First find a number that is divisible by all integers 2-20.
Then subtract 20 from it over and over, while checking that divisibility
still holds. The final number printed will be the lowest number.

This can probably be greatly optimized.
'''

number = 20

for i in range(3, 20):
    if not number % i == 0:
        number *= i
print(str(number))

for i in range(number, 20, -20):
    catch = True
    for j in range(3, 20):
        if not i % j == 0:
            catch = False
            break
    if catch:
        print(str(i))