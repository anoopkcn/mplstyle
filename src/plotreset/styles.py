import matplotlib.pyplot as plt

from plotreset import cycles, templates


class Styles:
    def __init__(self, style_name: str = "default"):
        self.style_name = style_name
        self.style = None
        """
        Initialize a Style object with the specified style.

        Args:
            style_name (str): Name of the style to be applied. Defaults to "default".

        Raises:
            ValueError: If the provided style_name is not valid.
        """
        if style_name in plt.style.available:
            self.style = plt.style.use(style_name)
        elif style_name in templates.available:
            stylesheet = self._get_template(style_name)
            self.style = plt.style.use(stylesheet)
        else:
            raise ValueError(f"Invalid style name: {style_name}")

    def _get_template(self, template_name: str) -> str:
        """
        Get the template stylesheet for the given template name.

        Args:
            template_name (str): Name of the template.

        Returns:
            str: The stylesheet for the template.

        Raises:
            ValueError: If the provided template_name is not valid.
        """
        if template_name in templates.available:
            return getattr(templates, template_name)
        else:
            raise ValueError(f"Invalid template name: {template_name}")

    def cycle(self, cycle_name: str):
        if cycle_name in cycles.AVAILABLE_CYCLES:
            cycle_func = getattr(cycles, cycle_name)
            return cycle_func()
        else:
            raise ValueError(f"Invalid cycle name: {cycle_name}")
        """
        Get the specified cycle.

        Args:
            cycle_name (str): Name of the cycle to be used.

        Returns:
            cycler: The specified cycle.

        Raises:
            ValueError: If the provided cycle_name is not valid.
        """
        if cycle_name in cycles.AVAILABLE_CYCLES:
            return getattr(cycles, cycle_name)()
        else:
            raise ValueError(f"Invalid cycle name: {cycle_name}")
