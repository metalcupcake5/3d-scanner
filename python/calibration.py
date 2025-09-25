import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Load calibration measurements.
calibration = np.loadtxt("./Calibration_data.csv", delimiter=",", dtype=int)

# Create a line of best fit for the calibration data.
# The first column is centimeters, the second is recorded analog output.
cm = calibration[:, 0]
v = calibration[:, 1]
equation = Polynomial.fit(v, cm, 1)


# Function to return the conversion equation.
def get_calibration_equation():
    return equation


# Function to plot the calibration equation.
def plot_calibration_equation():
    ax = plt.figure().add_subplot()
    t = np.linspace(350, 600, 100)
    ax.scatter(v, cm, label="Measured Data")
    ax.plot(t, equation(t), label="Calibration Line")
    ax.set_xlabel("Analog Voltage Output")
    ax.set_ylabel("Distance (cm)")
    ax.set_title("Calibration Curve")
    ax.legend()
    plt.show()


# Function to plot the equation that the rubric asks for.
def plot_reverse_calibration():
    equation_2 = Polynomial.fit(cm, v, 1)
    ax = plt.figure().add_subplot()
    t = np.linspace(10, 35, 100)
    ax.scatter(cm, v, label="Measured Data")
    ax.plot(t, equation_2(t), label="Calibration Line")
    ax.set_ylabel("Analog Voltage Output")
    ax.set_xlabel("Distance (cm)")
    ax.set_title("Reversed Calibration Curve")
    ax.legend()
    plt.show()
