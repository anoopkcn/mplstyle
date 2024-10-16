import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from plotreset import styles

st = styles.Style("academic")

x = np.linspace(-np.pi, np.pi, 100)

fig = plt.figure(figsize=(10, 4))

with mpl.rc_context(
    {"axes.grid": True, "xtick.minor.visible": True, "ytick.minor.visible": True}
):
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.plot(x, np.sin(x))

with mpl.rc_context({"text.usetex": False}):
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.plot(x, np.cos(x), color="tab:green")

with mpl.rc_context(
    {"axes.grid": True, "xtick.minor.visible": True, "ytick.minor.visible": True}
):
    panel = ax2.inset_axes((0.35, 0.2, 0.3, 0.3))
    panel.plot(x, np.sin(x), color="tab:orange")

plt.show()
