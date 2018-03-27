__author__ = 'aleksander'

import math
import helpers.math.divisibility as div

def get_list_of_primes_up_to(x):
    primes = []
    for i in range(2, int(x)):
        if div.is_prime(i):
            primes.append(i)
    return primes


def get_nth_prime(n):
    primes = [2]

    odd = 3
    while len(primes) < n:
        if div.is_prime(odd):
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
