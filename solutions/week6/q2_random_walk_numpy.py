import numpy as np
import matplotlib.pyplot as plt

# part a
n = int(1e4)  # number of numbers: 10 000

# create a list of random numbers, drawn according to normal (gaussian) distribution
random_array = np.random.randn(n)  # 'randn' - normal distribution;  'rand' would give uniform distribution
print(f"First 10 numbers of the list: {random_array[:10]}")  # print to see what's inside

# Calculate cumulative sums
cumsum_array = np.cumsum(random_array)

print(f"First 10 numbers of the cum-sum list: {cumsum_array[:10]}")

# part b: saving to txt file
np.savetxt('s-values.txt', cumsum_array)

# part c: cum-sum of cum-sums
variates_array = np.cumsum(cumsum_array)
np.savetxt('t-values.txt', variates_array)

# part d: display
plt.figure("Random walk")  # if the plot opens in a new window, the window name (top bar) will be 'Random walk'
plt.plot(cumsum_array, variates_array, linewidth=1., color='purple')
plt.grid(color='lightgray')
plt.xlabel("S values")
plt.ylabel("T values")
plt.title("Random walk: s and t values")  # title for the plot, displayed just above the plot 'box'
plt.show()  # without this line, the plot will not be displayed
