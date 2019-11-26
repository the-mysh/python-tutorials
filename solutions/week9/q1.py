# For convenience sake, I'm going to include all results from
# Practical 9 in the one file.
import math
import numpy

# 1.
def mySin(x, N):
    total = 0
    # This is a straight translation of the formula into python code
    for n in range(N+1):
        total += ((-1)**n * x **(2*n+1)) / math.factorial(2*n+1)
    return total

# 2, 3, 4
arr = numpy.loadtxt("testSine.txt")

# In order to check if our function is good enough, we need to loop
# through arr, and check which inputs
# - do not crash, and
# - differ from math.sin(x) by more than one millionth

# To do so, I've written a function, good_enough for testing it on one
# value

def good_enough(x, N):
    # To see if the function errors, I am using pythons "exceptions".
    # These were not really covered in the course, but there are many
    # tutorials available online. But the basic use here should be clear
    try:
        # Try to compute result
        result = mySin(x, N)
    except OverflowError:
        # If that errors, return False
        return False

    # So if we got here, is the result close enough
    return abs(result - math.sin(x)) < 1e-06


for i in range(len(arr)):
    x = arr[i, 0]
    N = int(arr[i, 1])
    if good_enough(x, N):
        print("Works fine for {} {}".format(x, N))
    else:
        print("Fails for {} {}".format(x, N))
