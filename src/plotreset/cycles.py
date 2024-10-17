from typing import Any, List

from cycler import Cycler, cycler

from plotreset import defaults

AVAILABLE_CYCLES = [
    "series_color",
    "series_linestyle",
    "series_linewidth",
    "series_marker",
    "series_markersize",
    "series_linestyle_color",
    "series_marker_color",
    "series_linestyle_marker_color",
    "series_fontsize",
    "series_linestyle_marker",
]


def _create_cycler(property: str, values: List[Any]) -> Cycler:
    return cycler(**{property: values})


def _combine_cyclers(*cyclers: Cycler) -> Cycler:
    if not cyclers:
        return cycler()
    return sum(cyclers, cycler())
    return sum(cyclers, cycler())


def series_linestyle() -> Cycler:
    return _create_cycler("linestyle", list(defaults.LINE_STYLES.values()))


def series_linewidth() -> Cycler:
    return _create_cycler("linewidth", list(defaults.LINE_WIDTHS.values()))


def series_color() -> Cycler:
    return _create_cycler("color", list(defaults.COLORS.values()))


def series_marker() -> Cycler:
    return _create_cycler("marker", list(defaults.MARKERS.values()))


def series_markersize() -> Cycler:
    return _create_cycler("markersize", list(defaults.MARKER_SIZES.values()))


def series_fontsize() -> Cycler:
    return _create_cycler("fontsize", list(defaults.FONT_SIZES.values()))


def _create_combined_cycler(
    prop1: str, prop2: str, values1: List[Any], values2: List[Any]
) -> Cycler:
    upper_limit = min(len(values1), len(values2))
    c1 = _create_cycler(prop1, values1[:upper_limit])
    c2 = _create_cycler(prop2, values2[:upper_limit])
    return _combine_cyclers(c1, c2)


def series_linestyle_color() -> Cycler:
    return _create_combined_cycler(
        "color",
        "linestyle",
        list(defaults.COLORS.values()),
        list(defaults.LINE_STYLES.values()),
    )


def series_marker_color() -> Cycler:
    return _create_combined_cycler(
        "color",
        "marker",
        list(defaults.COLORS.values()),
        list(defaults.MARKERS.values()),
    )


def series_linestyle_marker() -> Cycler:
    return _create_combined_cycler(
        "linestyle",
        "marker",
        list(defaults.LINE_STYLES.values()),
        list(defaults.MARKERS.values()),
    )


def series_linestyle_marker_color() -> Cycler:
    colors = list(defaults.COLORS.values())
    linestyles = list(defaults.LINE_STYLES.values())
    markers = list(defaults.MARKERS.values())
    upper_limit = min(len(colors), len(linestyles), len(markers))

    c1 = _create_cycler("color", colors[:upper_limit])
    c2 = _create_cycler("linestyle", linestyles[:upper_limit])
    c3 = _create_cycler("marker", markers[:upper_limit])

    return _combine_cyclers(c1, c2, c3)
