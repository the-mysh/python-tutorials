import matplotlib.pyplot as plt
import math

# a. Create a grid of 100 or more values between -2*pi and 2*pi
# Here, we will take evenly spaced values, which means that to cover
# the range in 100 steps, we should go up by 4*pi / 100 each time
steps = 100
lower = -2 * math.pi
upper = 2 * math.pi
step_size = (upper - lower) / steps

grid = []
for i in range(steps):
    # So the ith value in the list should be i steps above the lower limit
    grid.append(lower + i * step_size)

# b. Evaluate each of sin, cos, and tan, at each point in the grid
# We can reuse the same grid for each of the functions.

sins = []
for i in range(steps):
    sins.append(math.sin(grid[i]))

coss = []
for i in range(steps):
    coss.append(math.cos(grid[i]))

tans = []
for i in range(steps):
    tans.append(math.tan(grid[i]))

# c.
# See answers for q2 for more on what the plt functions do
plt.figure("Trig functions")
plt.plot(grid, sins)
plt.plot(grid, coss)
plt.plot(grid, tans)
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Plotting trig functions")
plt.ylim(-3, 3) # This restricts the range of the y-lim to be between -3 and 3
# This is important as otherwise matplotlib will try to fit every y
# value on the plot, and so the very large tan values we get near,
# e.g., pi/2, will dominate the graph and we won't really see sin or
# cos which are bounded between -1 and 1
plt.show()
