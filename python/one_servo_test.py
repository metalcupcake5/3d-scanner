import matplotlib.pyplot as plt
import numpy as np
from calibration import get_calibration_equation

with open("data_new_format.txt") as f:
    lines = f.readlines()

values = [int(x) for x in lines]
values = np.reshape(values, [66, 66])
values = get_calibration_equation()(values)
values = values[33, ...]
print(values)

# horizontal angle
theta = np.divide(range(60, 125, 1), 180) * np.pi

x = []
y = []

for t in range(len(theta)):
    dist = values[t]
    if dist > 35:
        continue
    x.append(dist * np.cos(theta[t]))
    y.append(dist * np.sin(theta[t]))

# Create an array to plot of the correct distance.
correct_dist = np.ones(len(x)) * 30
# Plot the sensor output against the correct values.
plt.plot(x, y, "o", label="Sensor Output")
plt.title("2D Scatterplot of 1-Servo Scan")
plt.xlabel("Horizontal Distance (cm)")
plt.ylabel("Depth (cm)")
plt.plot(x, correct_dist, label="Correct Distance")
plt.xlabel("Horizontal Distance (cm)")
plt.ylabel("Depth (cm)")
plt.legend()
plt.show()

# Calculate the error.
error = np.divide(y - correct_dist, correct_dist)
# Plot the error in a scatterplot.
plt.plot(x, error * 100, "o")
plt.plot(x, np.zeros(len(x)), label="0% Error")
plt.title("1-Servo Error Scatterplot")
plt.xlabel("Horizontal Distance (cm)")
plt.ylabel("Error (%)")
plt.legend()
plt.show()
