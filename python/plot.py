import matplotlib.pyplot as plt
import numpy as np
from calibration import get_calibration_equation

with open("data2_format.txt") as f:
    lines = f.readlines()

# reshape analog output to 2D matrix of distances
values = [int(x) for x in lines]
values = np.reshape(values, [17, 81])
values = get_calibration_equation()(values)

# horizontal angle
theta = np.divide(range(50, 131, 1), 180) * np.pi
# vertical angle
phi = np.divide(list(reversed(range(50, 135, 5))), 180) * np.pi


x = []
y = []
z = []
# Loop through each angle combination, calculating the Cartesian coordinates for
# x, y, and z.
for p in range(len(phi)):
    for t in range(len(theta)):
        dist = values[p][t]
        # if dist > 35:
        #     continue
        x.append(dist * np.cos(theta[t]) * np.sin(phi[p]))
        y.append(dist * np.sin(theta[t]) * np.sin(phi[p]))
        z.append(dist * np.cos(phi[p]))

# Use x, y, and z to create a 3D scatterplot.
ax = plt.figure().add_subplot(projection="3d")
ax.scatter(x, y, z)
ax.set_title("3D Scatterplot of Infrared Scan")
ax.set_xlabel("Horizontal Distance (cm)")
ax.set_ylabel("Depth (cm)")
ax.set_zlabel("Height from Sensor (cm)")
plt.show()
