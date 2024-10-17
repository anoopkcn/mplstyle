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

available = ["academic", "reset"]

reset = {
    # Text settings
    "text.usetex": False,
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 12,
    # Axes settings
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.axisbelow": True,
    "axes.grid": True,
    "axes.prop_cycle": cycler(
        color=[
            "#1f77b4",
            "#ff7f0e",
            "#2ca02c",
            "#d62728",
            "#9467bd",
            "#8c564b",
            "#e377c2",
            "#7f7f7f",
            "#bcbd22",
            "#17becf",
        ]
    ),
    # Grid settings
    "grid.linestyle": "--",
    "grid.linewidth": 0.5,
    "grid.alpha": 0.5,
    # Legend settings
    "legend.fontsize": 10,
    "legend.frameon": False,
    "legend.numpoints": 1,
    "legend.scatterpoints": 1,
    # Tick settings
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.major.size": 4,
    "ytick.major.size": 4,
    "xtick.minor.visible": False,
    "ytick.minor.visible": False,
    # Figure settings
    "figure.figsize": [8.0, 6.0],
    "figure.dpi": 100,
    "figure.autolayout": True,
    # Saving figure settings
    "savefig.dpi": 300,
    "savefig.format": "png",
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
    # Histogram settings
    "hist.bins": 50,
}
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
