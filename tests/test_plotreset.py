import pytest
from cycler import Cycler, cycler

from plotreset import Styles, defaults, register_cycle, register_template


def test_styles_initialization():
    style = Styles()
    assert style.style_name == "default"

    style = Styles("ggplot")
    assert style.style_name == "ggplot"

    with pytest.raises(ValueError):
        Styles("nonexistent_style")


def test_defaults():
    assert isinstance(defaults.COLORS, dict)
    assert isinstance(defaults.LINE_STYLES, dict)
    assert isinstance(defaults.LINE_WIDTHS, dict)
    assert isinstance(defaults.MARKERS, dict)
    assert isinstance(defaults.MARKER_SIZES, dict)
    assert isinstance(defaults.FONT_SIZES, dict)


def test_custom_template():
    custom_template = {
        "font.size": 14,
        "axes.titlesize": 16,
        "axes.labelsize": 12,
    }
    register_template("custom_template", custom_template)

    style = Styles("custom_template")
    assert style.style_name == "custom_template"

    # Check if the custom template is applied
    assert style._get_template("custom_template") == custom_template


def test_custom_cycle():
    def custom_cycle_func():
        return cycler(color=["red", "green", "blue"], linestyle=["-", "--", "-."])

    register_cycle("custom_cycle", custom_cycle_func)

    style = Styles()
    custom_cycle = style.cycle("custom_cycle")

    assert isinstance(custom_cycle, Cycler)
    assert "color" in custom_cycle.keys
    assert "linestyle" in custom_cycle.keys
    assert list(custom_cycle) == [
        {"color": "red", "linestyle": "-"},
        {"color": "green", "linestyle": "--"},
        {"color": "blue", "linestyle": "-."},
    ]


def test_invalid_custom_template():
    with pytest.raises(ValueError):
        Styles("nonexistent_custom_template")


def test_invalid_custom_cycle():
    style = Styles()
    with pytest.raises(ValueError):
        style.cycle("nonexistent_custom_cycle")


if __name__ == "__main__":
    pytest.main()
