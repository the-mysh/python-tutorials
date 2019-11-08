# Simplest possible solution, just check all four cases
def odd(a, b, c):
    if a and not b and not c:
        return True
    elif not a and b and not c:
        return True
    elif not a and not b and c:
        return True
    elif a and b and c:
        return True
    else:
        return False

## Alternatively, we can put them all in one condition
def odd_2(a, b, c):
    return (a and not b and not c) or (not a and b and not c) or (not a and not b and c) or (a and b and c):


# A third option is to note that we can treat boolean values as
# integers where True is 1, and False is 0.
def odd_3(a, b, c):
    # So the following line tells you how many of a, b, c are True
    sum = a + b + c
    # Then we can test for oddness using the modulo operator
    return (sum % 2) == 1
