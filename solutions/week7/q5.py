import math


def sigmoid(x):
    return 1 / (1 - math.exp(-x))

# Alternatively, you can use math.e ** (- x)
