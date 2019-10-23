# Refer to q4_primes_with_function.py for more extensive description

import sys

# get the number from the command line
the_number = int(sys.argv[1])
print(f"The number: {the_number}")

# collect all prime numbers lower than the_number in a list
all_primes = []

# iterate over all integers less than the_number (all of them this time; starting from 2 - the lowest prime number)
for candidate in range(2, the_number):

    # assume that the number is prime
    prime = True

    # we could iterate over all numbers less than the candidate
    # but in fact it is enough to check whether the number is divisible by any prime number smaller than itself (why?)
    # and actually we are collecting all the lower prime numbers on the way in the all_primes list
    for divisor in all_primes:

        # another optimisation - there is no point in checking numbers higher than a half of the candidate
        # (the loop would break with 'prime' being True)
        if divisor > candidate//2+1:
            break

        # calculate the remainder
        remainder = candidate % divisor

        # display the calculation
        print(f"{candidate}%{divisor} = {remainder}")

        # break if any factor was found
        if remainder == 0:
            prime = False
            break

    if prime:
        all_primes.append(candidate)

# display the result
print(f"All primes lower than {the_number}: {all_primes}")
