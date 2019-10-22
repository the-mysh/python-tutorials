"""Quick comparison between for and while loops in terms of the main usage cases."""

# let's say we have a vector of integers:
my_vector = [0, 2, 5, -1, -2, 4, 2, 6, 6, 9, 9, 10, 1, -8, 11]
print(f"values from the vector: {my_vector}")

# for loops are generally used if we know how many elements we want to process
# for example, calculate the sum of the first 10 elements
# imagine you collect tokens of different values and you stop collecting when you have 10

print("For loop: sum of first 10 elements")
sum_of_first_10 = 0  # initialise the sum to 0; we'll be adding elements one by one

for i in range(10):  # i is our loop variable; we will use it to access elements from the vector by indexing
    print(f"Element at position {i} equals to {my_vector[i]}")   # print the value
    sum_of_first_10 += my_vector[i]                              # increase the sum by the new value
    print(f"The current value of the sum is {sum_of_first_10}")  # print the current value

# print the final value
print(f"\nThe final value of the sum is {sum_of_first_10}")
# btw, check out Python 'f-strings' if you are curious about how the above print message formatting works
# Note: this works in Python 3 only
# (you are always free to use any different way, such as the '+' between message parts)

print(20*'=-' + '=' + '\n')
# ^ this is just a separator - a few 'minus' and 'equals' signs plus a new line sign ('\n')

# ==============================================================================================

# while loops are used when we don't know in advance how many elements we should process
# but we know another 'termination condition'
# for example, we want to sum up a few first elements of the vector until the sum is greater than 10
# imagine you collect tokens of different values and you stop collecting when the total value is more than 10

print("Sum of first few elements - greater than 10")
sum_greater_than_10 = 0              # initialise the sum as previously
i = 0                                # for a while loop, we need to take care about the loop variable separately
number_of_elements = len(my_vector)  # we also don't want indices to be greater than out number of elements (why?)

while sum_greater_than_10 <= 10:     # we're gonna stop when the sum is > 10, so we do it as long as it is <= 10
    print(f"Element at position {i} equals to {my_vector[i]}")       # print the value
    sum_greater_than_10 += my_vector[i]                              # increase the sum by the new value
    print(f"The current value of the sum is {sum_greater_than_10}")  # print the current value

    i += 1                                                           # increase i by 1

    # this is to make sure we don't go too far in the array (it could be that we never actually reach 10)
    # see what happens if you forget this part and use 100 instead of 10
    if i >= number_of_elements:
        print(f"Insufficient number of elements in the array!")
        break


# print the final value
print(f"\nThe final value of the sum is {sum_greater_than_10}")
# print how many numbers from the vector were taken into calculations
# it is i, not i+1 not i-1: we break at the next i, but also indexing starts from 0, not 1
print(f"Number of elements processed: {i}")
