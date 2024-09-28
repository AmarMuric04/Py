import matplotlib.pyplot as plt
import numpy as np

# Define the x range
x = np.linspace(-5, 5, 400)

# Calculate the corresponding y values for each curve
y1_pos = np.sqrt(1 - x)  # Positive part of y^2 = 1 - x
y1_neg = -np.sqrt(1 - x)  # Negative part of y^2 = 1 - x
y2 = -x - 1  # Line equation
y3 = np.full_like(x, 4)  # Horizontal line y = 4

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each curve
plt.plot(x, y1_pos, label="$y^2 = 1 - x$", color="blue")
plt.plot(x, y1_neg, color="blue")  # Negative part of the parabola
plt.plot(x, y2, label="$y = -x - 1$", color="orange")
plt.plot(x, y3, label="$y = 4$", color="green")

# Set the limits for the plot
plt.xlim(-5, 5)
plt.ylim(-10, 10)

# Add labels and a legend
plt.title("Graphs of $y^2 = 1 - x$, $y = -x - 1$, and $y = 4$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="black", linewidth=0.5, ls="--")
plt.axvline(0, color="black", linewidth=0.5, ls="--")
plt.grid()
plt.legend()

# Show the plot
plt.show()
