# Note, we do not expect you to be able to produce this program. It is
# provided solely as an example of how, with a little bit more
# thought, you can make a program that is a lot faster.

# One of the problems with the other program is that it tries a large
# amount of choices of (a, b, c, d) that can never be true, and some
# options are checked multiple times
# Rather than generating and checking, it is much faster if you only
# generate things that could be valid.
import sys
import math

n = int(sys.argv[1])

# The following solution uses python lists.

# First, given n, what is the largest number that we could possibly
# have as one of the cubes. Well, it is the cube root of n. (In fact
# this is slightly too big, but it will do for an approximation)
largest = int(math.pow(n, 1/3))
# math.pow lets us take the cube root, int will round it to the
# integer below

# We are going to keep a python list. In it, sum_of_two_cubes[i] is
# going to be the number of different ways i can be expressed as the
# sum of two cubes
sum_of_two_cubes = [0] * (2 * largest ** 3)

# Now, we are going to loop over all pairs of integers (a, b) with
# 0 <= a < b <= largest
for i in range(largest):
    # starting at i+1 means we always have i < j, so we have distinct numbers
    for j in range(i+1, largest):
        k = i ** 3 + j ** 3
        # Now we increment the number of ways k can be expressed as
        # the sum of two cubes
        sum_of_two_cubes[k] += 1

# Finally, we can loop over the list and print out all the numbers
# that can be expressed as the sum of two cubes in more than one way
for i in range(n+1):
    if sum_of_two_cubes[i] >= 2:
        print(i)

# The reason that this code is much faster than q3_slow.py is that it
# avoids checking any case more than once, and we never generate a
# "bad" example.

# One problem with the above code is that it creates a really large
# python list sum_of_two_cubes and most of the entries in that list
# never get updated. If you know how to use python dictionaries, you
# might try using one instead as this would waste less


# Compare the output of this with https://oeis.org/A001235
