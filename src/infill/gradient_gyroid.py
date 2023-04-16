#generated using ChatGPT, works too (after 2 attempts)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# Define the gyroid infill function
def gyroid_infill(x, y, z, scale):
    sinx = np.sin(x*scale)
    siny = np.sin(y*scale)
    sinz = np.sin(z*scale)
    return (sinx*siny + siny*sinz + sinz*sinx)

# Define the size of the grid
size = 50

# Define the scale of the gyroid infill
scale = 4

# Create a grid of points
x, y, z = np.mgrid[-1:1:complex(0, size), -1:1:complex(0, size), -1:1:complex(0, size)]

# Calculate the gyroid infill function at each point in the grid
f = gyroid_infill(x, y, z, scale)

# Normalize the values to range from 0 to 1
f_norm = (f - np.min(f)) / (np.max(f) - np.min(f))

# Define the thickness scale factor for the fade effect
thickness_scale = 5

# Create a Line3DCollection object for the gyroid infill lines
lines = []
thicknesses = []
for i in range(size):
    for j in range(size):
        line = np.stack((x[:, i, j], y[:, i, j], z[:, i, j]), axis=-1)
        lines.append(line)
        thickness = thickness_scale * (1 - f_norm[i, j, 0])
        thicknesses.append(thickness)
for i in range(size):
    for j in range(size):
        line = np.stack((x[i, :, j], y[i, :, j], z[i, :, j]), axis=-1)
        lines.append(line)
        thickness = thickness_scale * (1 - f_norm[i, 0, j])
        thicknesses.append(thickness)
for i in range(size):
    for j in range(size):
        line = np.stack((x[i, j, :], y[i, j, :], z[i, j, :]), axis=-1)
        lines.append(line)
        thickness = thickness_scale * (1 - f_norm[0, i, j])
        thicknesses.append(thickness)
lc = Line3DCollection(lines, linewidths=thicknesses)

# Plot the gyroid infill as a 3D line collection
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.add_collection(lc)
plt.show()