# To start off, you need to do a little bit of maths.
# Remember n! means factorial(n)
# Then ln(0!) = ln(1) = 0, and
# ln(n!) = ln(n*(n-1)!) = ln(n) + ln((n-1)!) for n > 0 using
# properties of logarithms.
# Since ln(n!) is defined in terms of ln((n-1)!) we can write a
# recursive program.
import math

def ln_fact(n):S
    if n == 0:
        return 0
    else:
        return math.log(n) + ln_fact(n-1)
