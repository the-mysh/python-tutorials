import sys

first = int(sys.argv[1])
second = int(sys.argv[2])

if first % second == 0 or second % first == 0:
    print(True)
else:
    print(False)
