#generated using ChatGPT, might be able to hook into the code somewhat

import numpy as np
import matplotlib.pyplot as plt

# Define the gyroid function
def gyroid(x, y, z, frequency):
    return np.sin(x*frequency)*np.cos(y*frequency) + np.sin(y*frequency)*np.cos(z*frequency) + np.sin(z*frequency)*np.cos(x*frequency)

# Define the size of the grid
size = 50

# Create a grid of points
x, y, z = np.mgrid[-1:1:complex(0, size), -1:1:complex(0, size), -1:1:complex(0, size)]

# Set the frequency of the gyroid function
frequency = 3

# Calculate the gyroid function at each point in the grid
f = gyroid(x, y, z, frequency)

# Plot the gyroid function as a 3D surface
#this part throws an error, don't use
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.plot_surface(x, y, z, facecolors=plt.cm.jet(f))
plt.show()