# Reusing this function from q1.py. See that file for comments
def primes(n):
    # Computes the prime numbers up to *and including* n, using the
    # trial division method.
    ps = []
    for i in range(2,n+1):
        is_prime = True
        for prime in ps:
            if i % prime == 0:
                is_prime = False
        if is_prime:
            ps.append(i)
    return ps


def totient(n):
    count = 0
    ps = primes(n)
    # Loop over all numbers between 1 and n
    # Q. Why n rather than n-1? Change it and compare the answer to totient(1)
    for i in range(1, n+1):
        coprime = True
        for p in ps:
            # If any prime is a common divisor of i and n
            if i % p == 0 and n % p == 0:
                # then i and n are not coprime
                coprime = False
        if coprime:
            count += 1
    return count


# If you know about math.gcd, you can use that instead
import math
def totient_2(n):
    count = 0
    for i in range(n):
        if math.gcd(n,i) == 1:
            count += 1
    return count
