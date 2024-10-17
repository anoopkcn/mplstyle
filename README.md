# plotreset
`matplotlib` plot styles and customizations. A sensible set of defaults for academic use. You can also extend the styles by adding more templates.

## Installation
**Activate your python environment then do:**
```bash
pip install plotreset
```
## Usage
Install the package
```python
from plotreset import Styles
```
Create an object. Note that when you create the object with a specific style template name, this template is applied instead of the matplotlib default

```python
st=Styles('academic')
```
Where `academic` is a `plotreset` template.  To revert back to `matplotlib` default template simply create the object without any arguments

```python
st=Styles()
```

### Example:
```python
st = Styles("academic")

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

plt.show()
```
<img src="https://raw.githubusercontent.com/anoopkcn/plotreset/refs/heads/main/examples/cycles.svg" alt="cycles" role="img">


Example script for binomial distribution plot:

```python
from plotreset import Styles

st = Styles("academic")

# Create example data
n = 30 * 75
p = 1 / 900
x = np.array(range(0, 15))

def res(n, p, x):
    return math.comb(n, x) * p**x * (1 - p) ** (n - x)

p_x = np.array([res(n, p, i) for i in x])

color = ["tab:blue"] * len(x)
color[0] = "tab:orange"

# The default behavior of academic style is not to draw a grid on the axes.
# We can change this behavior by using the `rc_context` method.

with mpl.rc_context({"axes.grid": True, "axes.axisbelow": True}):
    plt.bar(x, p_x, color=color)
    plt.xticks(x)
    plt.ylabel("$\\mathrm{P(X)}$")
    plt.xlabel("$\\mathrm{X}$")
    plt.annotate(
        "$\\mathrm{P(X=0) = 0.082}$",
        xy=(x.max() / 2.0, p_x.max() / 2),
        ha="left",
        va="center",
    )
    plt.annotate(
        "$\\mathrm{P(X\\geq1) = 0.918}$",
        xy=(x.max() / 2.0, p_x.max() / 2 - 0.03),
        ha="left",
        va="center",
    )
    plt.annotate(
        "$\\mathrm{E(X) = 2.49}$",
        xy=(x.max() / 2.0, p_x.max() / 2 - 0.06),
        ha="left",
        va="center",
    )
plt.show()
```
<img src="https://raw.githubusercontent.com/anoopkcn/plotreset/refs/heads/main/examples/binomial.svg" alt="binomial" role="img">

## Add more styles

You can add more style templates:


```python
import plotreset
my_template = {
    "axes.facecolor": "lightgray",
    "font.size": 14,
    # ... other style settings
}
plotreset.register_template("my_custom_style", my_template)
```

Use custom template:
```python
styles = Styles("my_custom_style")
```

You can also change the cycler templates:
```python
# Register a custom cycle
from cycler import cycler

def my_custom_cycle():
    return cycler(color=['r', 'g', 'b']) + cycler(linestyle=['-', '--', '-.'])

plotreset.register_cycle("my_custom_cycle", my_custom_cycle)
```

Use custom template and cycle
```python
styles = plotreset.Styles("my_custom_style")
plt.rcParams['axes.prop_cycle'] = styles.cycle("my_custom_cycle")
```

### `academic` template
```python

font_family = "cm" # or something else
academic = {
    "text.usetex": True,
    "mathtext.fontset": "cm",
    "mathtext.fallback": "cm",
    "mathtext.default": "regular",
    # FONT
    "font.size": 15,
    "font.family": font_family,
    # AXES
    "axes.axisbelow": "line",
    "axes.unicode_minus": False,
    "axes.formatter.use_mathtext": True,
     # Documentation for cycler (https://matplotlib.org/cycler/),
    "axes.prop_cycle": cycler(
        color=[
            "tab:red",
            "tab:blue",
            "tab:green",
            "tab:orange",
            "tab:purple",
            "tab:brown",
            "tab:pink",
            "tab:gray",
            "tab:olive",
            "tab:cyan",
            "k",
        ]
    ),
    # GRID
    "axes.grid": False,
    "grid.linewidth": 0.6,
    "grid.alpha": 0.5,
    "grid.linestyle": "--",
    # TICKS,
    "xtick.top": False,
    "xtick.direction": "in",
    "xtick.minor.visible": False,
    "xtick.major.size": 6.0,
    "xtick.minor.size": 4.0,
    "ytick.right": False,
    "ytick.direction": "in",
    "ytick.minor.visible": False,
    "ytick.major.size": 6.0,
    "ytick.minor.size": 4.0,
    # FIGURE,
    "figure.constrained_layout.use": True,
}

```
