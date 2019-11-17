import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

if (0 <= a and a <= 1) and (0 <= b and b <= 1):
    print(True)
else:
    print(False)
