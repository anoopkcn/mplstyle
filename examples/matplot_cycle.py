import numpy as np
from cycler import cycler
from matplotlib import pyplot as plt

from plotreset import defaults

fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True, figsize=(8, 4))
x = np.arange(10)

color_cycle = cycler(c=defaults.COLORS[:3])
ls_cycle = cycler(linestyle=defaults.LINE_STYLES[:3])
lw_cycle = cycler(linewidth=defaults.LINE_WIDTHS[:3])

sty_cycle = ls_cycle * (color_cycle + lw_cycle)

for i, sty in enumerate(sty_cycle):
    ax1.plot(x, x * (i + 1), **sty)

sty_cycle = (color_cycle + lw_cycle) * ls_cycle

for i, sty in enumerate(sty_cycle):
    ax2.plot(x, x * (i + 1), **sty)

plt.show()
