# This solution uses numpy functions to shorten the code from q1_without_numpy.py

import matplotlib.pyplot as plt
import numpy as np

# a. linspace will create 100 equally spaced values between -2*pi and 2*pi
grid = np.linspace(-2*np.pi, 2*np.pi, 100)

# b. Recall that the numpy versions of mathematical functions act on
# whole arrays at once
sins = np.sin(grid)
coss = np.cos(grid)
tans = np.tan(grid)

# c.
plt.figure("Trig functions")
plt.plot(grid, sins)
plt.plot(grid, coss)
plt.plot(grid, tans)
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Plotting trig functions")
plt.ylim(-3, 3)
plt.show()
