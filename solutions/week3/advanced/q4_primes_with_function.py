import sys

# get the number from the command line
the_number = int(sys.argv[1])
print(f"The number: {the_number}")

# define a function which will check for you whether a number ('my_number') is prime


def is_prime(my_number):
    """Is my_number prime? In other words, is it divisible by any integer lower than itself and greater than 1?"""

    # let's assume the number is prime; we'll revise that
    prime = True

    # check all integers from 2 to my_number, not included
    # Or, actually, to half of my_number. No number will have a factor greater than half of itself.
    # For example, if my_number equals to 24, it only makes sense to check numbers up to 12
    for divisor in range(2, my_number//2+1):

        # calculate the remainder
        remainder = my_number % divisor

        # display the number, divisor and result (comment that out for faster computation)
        print(f"{my_number}%{divisor} = {remainder}")

        if remainder == 0:
            # if so, the divisor is a factor of my_number, so my_number is not prime
            prime = False
            break  # one such number is enough - we don't need to check further

    # the return part: give back a True for a prime number, False for a composite number
    if prime:
        return True
    else:
        return False


# if you want to see how the function itself works, use:
# n = 23  # use any number to be checked
# if is_prime(n):
#     print(f"{n} is prime")
# else:
#     print(f"{n} is not prime")

# collect all prime numbers lower than the_number in a list
all_primes = []

# iterate over all integers less than the_number (all of them this time; starting from 2 - the lowest prime number)
for candidate in range(2, the_number):
    if is_prime(candidate):
        all_primes.append(candidate)

# display the result
print(f"All primes lower than {the_number}: {all_primes}")
