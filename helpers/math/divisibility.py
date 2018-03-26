import math

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
