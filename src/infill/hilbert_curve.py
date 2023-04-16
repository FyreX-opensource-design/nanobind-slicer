#generated using chatGPT. This might actually be complete, but that's yet to be tested

import numpy as np
import matplotlib.pyplot as plt

# Define the Hilbert curve function
def hilbert_curve(x, y, xi, xj, yi, yj, n):
    if n <= 0:
        X = x + (xi + yi)/2
        Y = y + (xj + yj)/2
        return X, Y
    else:
        x, y = hilbert_curve(x, y, yi/2, yj/2, xi/2, xj/2, n-1)
        x, y = hilbert_curve(x, y, xi/2, xj/2, yi/2, yj/2, n-1)
        x, y = hilbert_curve(x, y, xi/2, xj/2, yi/2, yj/2, n-1)
        x, y = hilbert_curve(x, y, -yi/2, -yj/2, -xi/2, -xj/2, n-1)
        return x, y

# Define the size of the grid
size = 512

# Set the order of the Hilbert curve
order = 6

# Generate the Hilbert curve
x, y = hilbert_curve(0, 0, 1, 0, 0, 1, order)

# Scale the curve to fit the grid
x = x * size/2 + size/2
y = y * size/2 + size/2

# Create a grid of points
xx, yy = np.meshgrid(range(size), range(size))

# Generate the Hilbert curve infill
infill = np.zeros((size, size))
for i in range(size):
    for j in range(size):
        if ((i+j)%2==0):
            if ((xx[i,j]<x[j]) or (yy[i,j]<y[j])):
                infill[i,j] = 1

# Plot the Hilbert curve infill
plt.imshow(infill, cmap='binary') #could use the binary date to map out the infill
plt.show()