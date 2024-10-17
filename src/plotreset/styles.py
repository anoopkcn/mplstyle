from typing import Any, Dict

import matplotlib.pyplot as plt
from cycler import Cycler

from plotreset import custom, cycles, templates


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
        if style_name == "default" or style_name in plt.style.available:
            self.style = plt.style.use(style_name)
        elif style_name in templates.available or style_name in custom.user_templates:
            stylesheet = self._get_template(style_name)
            self.style = plt.style.use(stylesheet)
        else:
            raise ValueError(f"Invalid style name: {style_name}")

    def _get_template(self, template_name: str) -> Dict[str, Any]:
        """
        Get the template stylesheet for the given template name.

        Args:
            template_name (str): Name of the template.

        Returns:
            Dict[str, Any]: The stylesheet for the template.

        Raises:
            ValueError: If the provided template_name is not valid.
        """
        if template_name in templates.available:
            return getattr(templates, template_name)
        elif template_name in custom.user_templates:
            custom_template = custom.get_custom_template(template_name)
            if custom_template is None:
                raise ValueError(
                    f"Custom template '{template_name}' is not properly defined"
                )
            return custom_template
        else:
            raise ValueError(f"Invalid template name: {template_name}")

    def cycle(self, cycle_name: str) -> Cycler:
        """
        Get the specified cycle.

        Args:
            cycle_name (str): Name of the cycle to be used.

        Returns:
            Cycler: The specified cycle.

        Raises:
            ValueError: If the provided cycle_name is not valid.
        """
        if cycle_name in cycles.AVAILABLE_CYCLES:
            cycle_func = getattr(cycles, cycle_name)
            return cycle_func()
        elif cycle_name in custom.user_cycles:
            custom_cycle = custom.get_custom_cycle(cycle_name)
            if custom_cycle is None:
                raise ValueError(f"Custom cycle '{cycle_name}' is not properly defined")
            return custom_cycle()
        else:
            raise ValueError(f"Invalid cycle name: {cycle_name}")
