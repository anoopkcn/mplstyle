import matplotlib.pyplot as plt
import numpy as np

from plotreset import Styles

style = Styles("reset")
plt.figure(figsize=(6, 4))
x = np.linspace(-5, 5, 200)
y = 1 / (np.sqrt(2 * np.pi)) * np.exp(-(x**2) / 2)
y2 = 1 / (np.sqrt(2 * np.pi * 2)) * np.exp(-(x**2) / (2 * 0.5))
y3 = 1 / (np.sqrt(2 * np.pi * 2)) * np.exp(-(x**2) / (2 * 1.5))
plt.plot(x, y, label="Gaussian Distribution")
plt.plot(x, y2, label="Gaussian Distribution")
plt.plot(x, y3, label="Gaussian Distribution")
plt.savefig("examples/simple.svg")
plt.show()
