#generated using ChatGPT. this is viewable if you use a GUI backend for Matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Define the bone infill function
def bone_infill(x, y, z, freq, amp):
    return np.sin(freq * np.pi * x) + np.sin(freq * np.pi * y) + np.sin(freq * np.pi * z) + amp

# Define the size of the grid
size = 50

# Create a grid of points
x, y, z = np.mgrid[-1:1:complex(0, size), -1:1:complex(0, size), -1:1:complex(0, size)]

# Set the frequency and amplitude of the bone infill
freq = 10
amp = 0.5

# Calculate the bone infill function at each point in the grid
f = bone_infill(x, y, z, freq, amp)

# Normalize the values to range from 0 to 1
f = (f - np.min(f)) / (np.max(f) - np.min(f))

# Threshold the values to create a binary array of 0's and 1's
threshold = 0.5
binary = (f > threshold)

# Plot the bone-like infill function as a 3D lattice structure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.voxels(binary, edgecolor="k")
plt.show()