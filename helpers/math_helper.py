__author__ = 'aleksander'


import math


# Primes
def is_prime(x):

    if x == 1:
        return False
    if x == 2:
        return True

    if not isinstance(x, int):
        print("Tried to check if a non-integer is prime. Of course it's not prime.")
        return False

    upper_limit = math.ceil(math.sqrt(x)) + 1

    if x % 2 == 0:
        return False

    for i in range(3, upper_limit, 2):
        if x % i == 0:
            return False

    return True


def get_list_of_primes_up_to(x):
    primes = []
    for i in range(2, int(x)):
        # if i % 10000 == 0:
        #     print("Progress: " + str(i))

        if is_prime(i):
            print(str(i))
            primes.append(i)
    return primes


def get_nth_prime(n):
    primes = [2]

    odd = 3
    while len(primes) < n:
        if is_prime(odd):
            primes.append(odd)
        odd += 2

    return primes[-1]


#Lists

def product_of_list(numbers):
    if not type(numbers) is list:
        print(product_of_list.__name__ + " requires a list. Other type found.")
        return False

    product = 1
    for x in numbers:
        product *= x
    return product


def sum_of_list(numbers):
    if not type(numbers) is list:
        print(sum_of_list.__name__ + " requires a list. Other type found.")
        return False

    sum_of_numbers = 0
    for x in numbers:
        sum_of_numbers += x
    return sum_of_numbers


#Triangle numbers

def get_nth_triangle_number(n):
    triangle_number = 0
    for i in range(1, n+1):
        triangle_number += i
    return triangle_number


#Divisibility and divisors

def get_all_divisors(n):
    if n == 1:
        return [1]
    divisors = [1, n]

    upper_limit = math.ceil(math.sqrt(n))

    for i in range(int(upper_limit), 1, -1):
        if n % i == 0:
            if i not in divisors:
                divisors.append(i)
                divisors.append(n/i)

    result = []
    for value in divisors:
        if value not in result:
            result.append(value)

    return sorted(result)


#Sums and products

def get_integer_sum(n):
    return get_nth_triangle_number(n)