def recursive_func(level):
    print(f"Entering level {level}")
    if level > 0:
        recursive_func(level-1)
    print(f"Exiting level {level}")


def fibonacci_recursive(n, f1=1, f2=1):
    """Return n-th number from the Fibonacci sequence.

    Parameters
    ----------
    n   :   int
        which number should be returned
    f1  :   int
        currently last-but-one number in the sequence (the part of it calculated so far)
    f2  :   int
        currently last number in the sequence
    """

    print(f"f1={f1}, f2={f2}")  # current last number in the sequence

    if n == 0:
        return f2

    return fibonacci_recursive(n-1, f2, f1 + f2)  # new f1 is old f2, new f2 is f1+f2; we still have n-1 numbers to go

