# To work out the base 2 logarithm of a number x, remember that we want
# to find the number n such that 2**n = x.
# In this case, the question restricts us to the *integer* n with
# 2 ** n <= x . The simplest way to find this number is just to start
# at 0 and count up until we go over

def lg2(x):
    n = 0
    while 2**n <= x:
        n = n + 1
    # Because we've gone over, i.e., 2**n > x,
    # we need to remember to subtract one.
    return n - 1
