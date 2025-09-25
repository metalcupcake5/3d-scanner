import matplotlib.pyplot as plt
import numpy as np
from calibration import get_calibration_equation

ax = plt.figure().add_subplot(projection='3d')

with open("data_new_format.txt") as f:
    lines = f.readlines()

values = [int(x) for x in lines]
values = np.reshape(values, [66, 66])
values = get_calibration_equation()(values)

# horizontal angle
theta = np.divide(range(60, 125, 1), 180) * np.pi
# vertical angle
phi = np.divide(list(reversed(range(60, 125, 1))), 180) * np.pi

x = []
y = []
z = []

for p in range(len(phi)):
    for t in range(len(theta)):
        dist = values[p][t]
        if dist > 35:
            continue
        x.append(dist * np.cos(theta[t]) * np.sin(phi[p]))
        y.append(dist * np.sin(theta[t]) * np.sin(phi[p]))
        z.append(dist * np.cos(phi[p]))

ax.scatter(x, y, z)

ax.set_xlabel("X label")
ax.set_ylabel("Y label")
ax.set_zlabel("Z label")

plt.show()
