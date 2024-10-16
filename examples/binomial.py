import math

import matplotlib as mpl  # To use context manager of matplotlib
import matplotlib.pyplot as plt
import numpy as np
from plotreset import styles

st = styles.Style("academic")


def res(n, p, x):
    return math.comb(n, x) * p**x * (1 - p) ** (n - x)


n, p = 30 * 75, 1 / 900

x = np.array(range(0, 15))
p_x = np.array([res(n, p, i) for i in x])


color = ["tab:blue"] * len(x)
color[0] = "tab:orange"


with mpl.rc_context({"axes.grid": True, "axes.axisbelow": True}):
    """
    The default behavior of academic style is not to draw a grid on the axes.
    """
    plt.bar(x, p_x, color=color)
    plt.xticks(x)
    plt.ylabel("$\\mathrm{P(X)}$")
    plt.xlabel("$X$")
    plt.title("Probability of triggering the threshold")
    plt.annotate(
        "$P(X=0) = 0.082$", xy=(x.max() / 2.0, p_x.max() / 2), ha="left", va="center"
    )
    plt.annotate(
        "$P(X\\geq1) = 0.918$",
        xy=(x.max() / 2.0, p_x.max() / 2 - 0.03),
        ha="left",
        va="center",
    )
    plt.annotate(
        "$E(X) = 2.49$",
        xy=(x.max() / 2.0, p_x.max() / 2 - 0.06),
        ha="left",
        va="center",
    )
plt.show()  # This could be inside of outside the context
