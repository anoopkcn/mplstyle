import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

from plotreset import Styles, defaults

style = Styles("reset")
c1 = cycler(color=defaults.COLORS[:4])
c2 = cycler(linestyle=defaults.LINE_STYLES[:4])
c3 = cycler(marker=defaults.MARKERS[:4])


x = np.linspace(0, 2 * np.pi, 50)
offsets = np.linspace(0, 2 * np.pi, 8, endpoint=False)
yy = np.transpose([np.sin(x + phi) for phi in offsets])

fig = plt.figure(figsize=(10, 4))
with mpl.rc_context({"axes.prop_cycle": c1}):
    ax1 = fig.add_subplot(3, 1, 1)
    ax1.plot(yy)
    ax1.set_title("changing_colors")

with mpl.rc_context({"axes.prop_cycle": c1 + c2}):
    ax2 = fig.add_subplot(3, 1, 2)
    ax2.plot(yy)
    ax2.set_title("changing linestyle and color")

with mpl.rc_context({"axes.prop_cycle": c1 + c2 + c3}):
    ax3 = fig.add_subplot(3, 1, 3)
    ax3.plot(yy)
    ax3.set_title("changing linestyle, color and marker")

# plt.savefig("cycles.svg")
# st.save_current_template("test", "examples/academic_latex.json")
plt.show()
