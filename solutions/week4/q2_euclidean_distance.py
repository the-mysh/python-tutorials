import math   # we'll be using sqrt function from math; imports should be defined at the top of the script


# let's assume the vectors are already defined
# they need to have the same lengths (i.e. the same number of elements)

my_vector1 = [20, 2, 11, 15, 2, 4, 12]
my_vector2 = [12, 5, -2, 77, 2, 23, 0]

# we need the length of the vectors (we assume it's the same; you can implement the verification if you want)
n = len(my_vector1)

# let's iterate over all elements of the two vectors
# we'll access elements by their position, i.e. index (call the variable whatever you want, could be i, x, unicorn, ...)
# we'll also be summing up values along the way, so we need an initial sum, which is 0 (see samples/for_and_while.py)
sum_of_squared_differences = 0

for position in range(n):
    element1 = my_vector1[position]
    element2 = my_vector2[position]
    print(f"Elements at position {position}: {element1}, {element2}")

    the_difference = element2 - element1  # does the order matter? why?
    print(f"Difference of the two elements: {the_difference}")

    the_difference_squared = the_difference**2
    print(f"The difference squared: {the_difference_squared}")

    # increment the sum
    sum_of_squared_differences += the_difference_squared
    print(f"Current sum of squared differences: {sum_of_squared_differences}")  # we're still in the loop here
    print('\n')

print(20*'-')
print(f"\nFinal sum of squares: {sum_of_squared_differences}")  # loop is finished now - back to zero indentation

sq_root_of_the_sum = math.sqrt(sum_of_squared_differences)
print(f"\nSquare root of the sum of squared differences, a.k.a. THE RESULT: {sq_root_of_the_sum}")
