import random
import numpy as np
import matplotlib.pyplot as plt

# part a

n = int(1e4)  # number of numbers: 10 000

# prepare the list of random numbers
# we could start with an empty list and append elements as usual
# with big lists though, it might be better to have the size fixed
# the line below creates a list of n (10 000) zeros
random_list = n * [0.]

# put random numbers in the list - instead of the zeros
for i in range(n):
    random_list[i] = random.gauss(0, 1)  # the element at position i already exists (it is a 0) - just change the value

print(f"First 10 numbers of the list: {random_list[:10]}")  # print to see what's inside

# Calculate cumulative sums
cumsum_list = n*[0.]  # start as previously

# the first cumulative sum (at position 0) is just the first element from the original list
cumsum_list[0] = random_list[0]

# from the second element onwards, the sum at position i is the original i-th element (random_list[i])
# plus sum of all the previous elements
# which we have actually stored in the cum-sum list - at position i-1 (cumsum_list[i-1])
# we start from element of index 1 - we have already got the one at 0
for i in range(1, n):
    cumsum_list[i] = random_list[i] + cumsum_list[i-1]

print(f"First 10 numbers of the cum-sum list: {cumsum_list[:10]}")

# part b: saving to txt file
np.savetxt('s-values.txt', cumsum_list)

# part c: cum-sum of cum-sums
variates_list = n*[0.]
variates_list[0] = cumsum_list[0]

for i in range(1, n):
    variates_list[i] = cumsum_list[i] + variates_list[i-1]

np.savetxt('t-values.txt', variates_list)

# part d: display
plt.figure("Random walk")  # if the plot opens in a new window, the window name (top bar) will be 'Random walk'
plt.plot(cumsum_list, variates_list)
plt.grid(color='lightgray')
plt.xlabel("S values")
plt.ylabel("T values")
plt.title("Random walk: s and t values")  # title for the plot, displayed just above the plot 'box'
plt.show()  # without this line, the plot will not be displayed
