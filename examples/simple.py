import matplotlib.pyplot as plt
import numpy as np

from plotreset import Styles

style = Styles("academic")
plt.figure()
# plot gaussian distribution
style.font.size = 18  # change font size
x = np.linspace(-5, 5, 100)
y = 1 / (np.sqrt(2 * np.pi)) * np.exp(-(x**2) / 2)
plt.plot(x, y, label="Gaussian Distribution")
plt.savefig("examples/simple.svg")
# style.save_current_template("minimal", "examples/academic_latex.json", overwrite=True)
plt.show()
