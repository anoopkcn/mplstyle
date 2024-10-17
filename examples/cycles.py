import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from plotreset import Styles

st = Styles("minimal", path="examples/academic_latex.json")

c1 = st.cycle("series_color")
c2 = st.cycle("series_linestyle_color")
c3 = st.cycle("series_linestyle_marker_color")

x = np.linspace(0, 2 * np.pi, 50)
offsets = np.linspace(0, 2 * np.pi, 8, endpoint=False)
yy = np.transpose([np.sin(x + phi) for phi in offsets])

fig = plt.figure(figsize=(10, 4))
with mpl.rc_context({"axes.prop_cycle": c1}):
    ax1 = fig.add_subplot(3, 1, 1)
    ax1.plot(yy)
    ax1.set_title("changing_colors")
with mpl.rc_context({"axes.prop_cycle": c2}):
    ax2 = fig.add_subplot(3, 1, 2)
    ax2.plot(yy)
    ax2.set_title("changing linestyle and color")
with mpl.rc_context({"axes.prop_cycle": c3}):
    ax3 = fig.add_subplot(3, 1, 3)
    ax3.plot(yy)
    ax3.set_title("changing linestyle, color and marker")

# plt.savefig("cycles.svg")
# st.save_current_template("test", "examples/academic_latex.json")
plt.show()
