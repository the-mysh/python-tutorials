# This version should work fine for all seen inputs from testSine.txt
import math
import numpy

# 1.

# We make two changes to mySin. The first is to convert x to a value
# y between 0 and 2*pi where sin(x) = sin(y). We can do this because
# sin is periodic. The second is to divide by the factorial using a
# loop rather than math.factorial to prevent OverflowError's from occuring.
def mySin(x, N):
    x = in_period(x, 2*math.pi)
    total = 0
    for n in range(N+1):
        y = (-1)**n * x**(2*n+1)
        # divide by (2*n+1)! in a loop
        for i in range(1,2*n+2):
            y /= i
        total += y

    return total

def in_period(x, period):
    # Repeatedly subtract period from x until x <= period
    while x > period:
        x -= period
    # Repeatedly add period from x > 0
    while x < 0:
        x += period
    # Note that only one of those loops will ever happen, since
    # subtracting the period in the first loop will never take x below
    # 0, and adding period in the second loop will never take it above period
    return x


# This is all repeated from q1.py

arr = numpy.loadtxt("testSine.txt")

def good_enough(x, N):
    try:
        result = mySin(x, N)
    except:
        return False
    return abs(result - math.sin(x)) < 1e-06


for i in range(len(arr)):
    x = arr[i, 0]
    N = int(arr[i, 1])
    if good_enough(x, N):
        print("Works fine for {} {}".format(x, N))
    else:
        print("Fails for {} {}".format(x, N))
