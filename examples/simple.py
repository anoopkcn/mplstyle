import matplotlib.pyplot as plt
import numpy as np

from plotreset import Styles

st = Styles("academic")
plt.figure()
# plot gaussian distribution
x = np.linspace(-5, 5, 100)
y = 1 / (np.sqrt(2 * np.pi)) * np.exp(-(x**2) / 2)
plt.plot(x, y, label="Gaussian Distribution")
plt.savefig("examples/simple.svg")
plt.show()
