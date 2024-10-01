import matplotlib.pyplot as plt
import numpy as np


# Define the functions
def f1(x):
    return -(x**2) + x + 4


def f2(x):
    return -x + 1


def f3(x):
    return x


# Create an array of x values
x = np.linspace(-3, 5, 400)

# Calculate y values for each function
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)

# Set up the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label="y = -x^2 + x + 4", color="blue")
plt.plot(x, y2, label="y = -x + 1", color="red")
plt.plot(x, y3, label="y = x", color="green")

# Outline the axes
plt.axhline(0, color="black", linewidth=1.5, ls="-")  # y=0 (x-axis)
plt.axvline(0, color="black", linewidth=1.5, ls="-")  # x=0 (y-axis)

# Add labels and a legend
plt.title("Plot of the Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

# Set the limits for the y-axis
plt.ylim(-5, 5)

# Show the plot
plt.show()
