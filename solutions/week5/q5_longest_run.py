import sys

# use the command line arguments
# (e.g. python q5_longest_run.py 1 2 2 1 5 1 1 7 7 7 7 1 1)
# the first argument (position 0) is the file name; use the rest - from 1 onwards
numbers = sys.argv[1:]

# display the numbers
print(f"List of numbers to be processed: {numbers}")

# keep two variables - 'runs', i.e. lists of same numbers
# 1) current run - all subsequent past occurrences of the 'current' number
# put the first number from the entire list there
current_run = [numbers[0]]

# 2) best run, i.e. the longest ('until now') sequence of same numbers
# empty (although [numbers[0]] would work too
# Note: don't use 'best_run = current_run'! This would make both names (best_run and current_run) refer to the very same
# object, so if you modify one, the other will also change
best_run = []

# iterate over the numbers in the list
# start from the second one (at position 1 instead of 0)
# we're comparing a number to the previous one, so it doesn't make sense to compare the first number to anything
# (you can also modify the solution a bit to use 'range(len(numbers)-1)' instead
for i in range(1, len(numbers)):
    # check if the number is equal to the previous one
    if numbers[i] == numbers[i-1]:
        # if so, append it to the list
        current_run.append(numbers[i])
    else:
        # otherwise, reset the list - put the new number as the only element of the new current_run
        current_run = [numbers[i]]

    # remember the best result in best_run
    # if current_run ha more elements than the best_run we had until now, forget the old sequence and store the new one
    if len(current_run) > len(best_run):
        best_run = current_run[:]  # this copies all elements from current_run rather than referring to the same object

# Display the result
print(f"Longest run: {best_run}")

the_number = best_run[0]
run_length = len(best_run)
print(f"({run_length} consecutive {the_number}s)")

# tip: to better understand what is happening in the loop, add your own print statements on the way and read the output
