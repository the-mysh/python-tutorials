def factor(n):
    # We are assuming n is a positive integer.
    # We know then that either n = 1, or n has some prime divisor
    if n == 1:
        # Since 1 is not a prime, it has no prime divisors, so we
        # return an empty list
        return []
    else:
        p = find_prime_divisor(n)
        # So once we have found a prime divisor of n, the full list of
        # its prime divisors are the divisors of n / p and p
        ps = factor(n // p)
        return [p] + ps

def find_prime_divisor(n):
    for p in primes(n):
        if n % p == 0:
            return p
    return n # This line will never be reached. Why?

def primes(n):
    # See week 7 for an explanation
    ps = []
    for i in range(2,n+1):
        is_prime = True
        for prime in ps:
            if i % prime == 0:
                is_prime = False
        if is_prime:
            ps.append(i)
    return ps


print(factor(120)) # prints [2, 2, 2, 3, 5]
print(factor(30030)) # prints [2, 3, 5, 7, 11, 13]

# This code is quite inefficient because we rebuild primes(n) every
# time we recurse. This could be improved by using a nested function
# definition for the recursion. Then the code would more closely
# resemble our solution from week 7.
