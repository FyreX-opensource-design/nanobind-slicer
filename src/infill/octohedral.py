#generated using chatGPT
import numpy as np
import matplotlib.pyplot as plt

# Define the octahedral infill function
def octahedral_infill(x, y, z, angle):
    a = angle * np.pi/180
    b = np.tan(a)
    return (x + y + z) - b*np.abs(x - y) - b*np.abs(y - z) - b*np.abs(z - x)

# Define the size of the grid
size = 50

# Create a grid of points
x, y, z = np.mgrid[-1:1:complex(0, size), -1:1:complex(0, size), -1:1:complex(0, size)]

# Set the angle of the octahedral infill
angle = 45

# Calculate the octahedral infill function at each point in the grid
f = octahedral_infill(x, y, z, angle)

# Normalize the values to range from 0 to 1
f = (f - np.min(f)) / (np.max(f) - np.min(f))

# Plot the octahedral infill function as a 3D surface
#again I suspect this part isn't working
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.plot_surface(x, y, z, facecolors=plt.cm.jet(f))
plt.show()