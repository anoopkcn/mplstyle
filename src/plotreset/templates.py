# LATEX
import matplotlib as mpl
import matplotlib.font_manager as font_manager
from cycler import cycler

font_family = "sans-serif"
try:
    cmfont = font_manager.FontProperties(
        fname=mpl.get_data_path() + "/fonts/ttf/cmr10.ttf"
    )
    font_family = cmfont.get_name()
except FileNotFoundError:
    font_family = "sans-serif"

available = ["academic"]

academic = {
    "text.usetex": True,
    # "text.latex.preamble": "\usepackage\{amsmath\}",
    "mathtext.fontset": "cm",
    "mathtext.fallback": "cm",
    "mathtext.default": "regular",
    # FONT
    "font.size": 16,
    "font.family": font_family,
    # AXES
    # Documentation for cycler (https://matplotlib.org/cycler/),
    "axes.axisbelow": "line",
    "axes.unicode_minus": False,
    "axes.formatter.use_mathtext": True,
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
