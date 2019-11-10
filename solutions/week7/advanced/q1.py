# To do this task, it first makes sense to have a function which
# returns a list of primes. (Tutorial 3, Advanced Question 4)

def primes(n):
    # Computes the prime numbers up to *and including* n, using the
    # trial division method.
    ps = []
    for i in range(2,n+1):
        # start by assuming i is prime
        is_prime = True
        # loop through all known primes
        for prime in ps:
            if i % prime == 0:
                # if any prime divides i, set is_prime to false
                is_prime = False
        # if after checking all primes none of them divided i, then
        # add it to our list of primes
        if is_prime:
            ps.append(i)
    return ps

# Given that function, we can now write a function which factors a
# positive integer. To do so, we will try to divide n by each prime as
# many times as possible.
def factor(n):
    factors = []
    for p in primes(n):
        # For every prime
        while n % p == 0:
            # Divide p from n as many times as possible
            n /= p
            # and add p to factors that many times
            factors.append(p)
    return factors
