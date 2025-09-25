import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

calibration = np.loadtxt("./Calibration_data.csv", delimiter=",", dtype=int)

cm = calibration[:, 0]
v = calibration[:, 1]
equation = Polynomial.fit(v, cm, 1)
def get_calibration_equation():
    return equation

def plot_calibration_equation():
    ax = plt.figure().add_subplot()
    t = np.linspace(350, 600, 100)
    ax.scatter(v, cm)
    ax.plot(t, equation(t))
    plt.show()
