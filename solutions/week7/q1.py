## The simplest possible solution
def max3(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    elif b >= c: # here a < b
        return b
    else: # here a < b and b < c
        return c
