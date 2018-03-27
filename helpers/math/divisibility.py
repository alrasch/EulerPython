import math


class Divisibility:
    primes = [2, 3]

    def is_prime_2(self, n):
        if n == 1: return False
        if n in self.primes: return True
        max_factor = int(math.sqrt(n)) + 1

        for prime in self.primes:
            if n % prime == 0:
                return False

        while self.primes[-1] < max_factor:
            if n % self.primes[-1] == 0:
                return False
            self.generate_next_prime()

        return True


    def is_prime_current(self, n):
        for prime in self.primes:
            if n % prime == 0:
                return False
        return True

    def generate_next_prime(self):
        check = self.primes[-1]
        while True:
            check += 2
            if self.is_prime_current(check):
                self.primes.append(check)
                return

    def generate_primes_up_to(self, n):
        if self.primes[-1] >= n: return

        sieve = [True] * (n+1)
        for num in range(2, n+1):
            if sieve[num] == True:
                for c in range(num*2, n+1, num):
                    sieve[c] = False

        sieve[0] = False
        sieve[1] = False

        self.primes = [index for index, value in enumerate(sieve) if value == True]


    def get_primes_up_to(self, n):
        self.generate_primes_up_to(n)
        wanted_subset = []
        for prime in self.primes:
            if prime <= n: wanted_subset.append(prime)
        return wanted_subset

    def is_prime(self, x):
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

        for i in range(3, int(upper_limit), 2):
            if x % i == 0:
                return False

        return True
