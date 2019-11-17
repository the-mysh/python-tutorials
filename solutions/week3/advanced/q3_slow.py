# The obvious, but really slow implementation.
# see q3_fast.py for a better way to do this

import sys

n = int(sys.argv[1])

for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                if (a != b) and (a != c) and (a != d) and (b != c) and (b != d) and (c != d) and (a ** 3 + b ** 3 == c ** 3 + d ** 3):
                   print(a ** 3 + b ** 3)
