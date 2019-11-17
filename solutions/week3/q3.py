import sys

m = int(sys.argv[1])
d = int(sys.argv[2])

if (m == 3) and (d >= 20):
    print(True)
elif (m > 3) and (m < 6):
    print(True)
elif (m == 6) and (d <= 20):
    print(True)
else:
    print(False)
