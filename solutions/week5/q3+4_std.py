import sys
import math

# Question 3
# ----------
# Get a command line argument - number of numbers to be processed
n = int(sys.argv[1])

# Define a list to hold numbers given by the user one by one
all_numbers = []
for i in range(n):
    value = float(input("Enter a float: "))  # ask for another value; stdio is also fine for that
    all_numbers.append(value)                # put the value in the list

print(f"List of numbers: {all_numbers}")

# Calculate the sum of all numbers in the list
sum_of_the_numbers = 0
for a_number in all_numbers:
    sum_of_the_numbers += a_number
    print(f"Current number: {a_number}, sum: {sum_of_the_numbers}")

# Mean is the sum divided by the number of the elements (n)
mean_of_the_numbers = sum_of_the_numbers / n

print(f"Sum: {sum_of_the_numbers}, mean: {mean_of_the_numbers}")

# Standard deviation is:
# - square root
# - of the sum
# - of the squares
# - of their differences from the average (i.e. how far they are from the mean)
# (divided by n, but let's leave that bit for later)
# As usual, try to read that from the end: first the differences, then the squares, etc.

# Calculate the sum of squares of the differences
# The structure is the same as calculation of a plain sum
# Just the values we add are different - not the elements, but squares of the differences
sum_of_squares = 0
for a_number in all_numbers:
    a_square = (a_number - mean_of_the_numbers)**2
    sum_of_squares += a_square

# Square root of the sum
the_root = math.sqrt(sum_of_squares)

# The last bit now: to get standard deviation, divide by n
the_std = the_root / n

print(f"Standard deviation: {the_std:.3f}")  # display only 3 decimal digits

# Question 4
# ----------
# We want to detect numbers which are too far from the mean, i.e. they could be outliers
# e.g. for the following sequence: [3.5, 3.2, 10, 2.9, -2.5]:
# - the mean will be around 3
# - 3.5, 3.2, and 2.9 are close to the mean
# - 10 is quite far from the mean; same for -2.5, just the other direction
# How far is 'too far'? We'll take 1.5*std (standard deviation tells us about the spread of the data)
distance = 1.5 * the_std                # the maximum 'distance' from the mean we 'accept'
low = mean_of_the_numbers - distance    # the lower boundary - mean minus the max distance
up = mean_of_the_numbers + distance     # the upper boundary - mean plus the distance
print(f"\nBoundaries: {low:.3f}, {up:.3f}")

# If a number is too far from the mean, i.e. it is below the lower boundary or above the upper one - print it
print(f"\nOutliers:", end=' ')
for a_number in all_numbers:
    if a_number < low or a_number > up:  # or, not and - it can't be that both are simultaneously satisfied
        print(a_number, end=' ')
print("")

# You can also collect all numbers which are fine (within the range) and all outliers
the_good_ones = []
the_outliers = []
for a_number in all_numbers:
    if low <= a_number <= up:  # chained comparison - a_number being BOTH higher than 'low' and lower than 'up'
        the_good_ones.append(a_number)
    else:
        the_outliers.append(a_number)

print(f"\nNumbers close enough to the mean: {the_good_ones}; outliers: {the_outliers}")
