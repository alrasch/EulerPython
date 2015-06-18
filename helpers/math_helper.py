__author__ = 'aleksander'


def is_prime(x):

    if x == 1:
        return False

    if not isinstance(x, int):
        print("Tried to check if a non-integer is prime. Of course it's not prime.")
        return False
    else:
        x = int(x)

    if x % 2 == 0:
        upper_limit = int(x/2)
    else:
        upper_limit = int((x+1)/2)

    upper_limit += 1

    for i in range(2, upper_limit):
        if x % i == 0:
            return False

    return True


def get_list_of_primes_up_to(x):
    primes = []
    for i in range(2, int(x)):
        if is_prime(i):
            primes.append(i)


def get_nth_prime(n):
    primes = [2]

    odd = 3
    while len(primes) < n:
        if is_prime(odd):
            primes.append(odd)
        odd += 2

    return primes[-1]