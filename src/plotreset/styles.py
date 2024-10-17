import json
from typing import Any, Dict, Optional

import matplotlib.pyplot as plt
from cycler import cycler

from plotreset import custom, templates
from plotreset.utils import cycler_to_dict, load_custom_settings


class StyleProxy:
    def __init__(self, styles):
        self._styles = styles

    def __getattr__(self, name):
        return StyleCategory(self._styles, name)


class StyleCategory:
    def __init__(self, styles, category):
        self._styles = styles
        self._category = category

    def __getattr__(self, name):
        full_key = f"{self._category}.{name}"
        if full_key in self._styles.style:
            return self._styles.style[full_key]
        raise AttributeError(f"'{full_key}' not found in style")

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            full_key = f"{self._category}.{name}"
            self._styles.style[full_key] = value
            self._styles.apply_changes()


class TemplatePathError(Exception):
    """Exception raised when a path is not provided for template operations."""

    pass


class Styles:
    def __init__(self, template_name: str = "default", path: Optional[str] = None):
        """
        Initialize a Style object with the specified template.

        Args:
            template_name (str): Name of the template to be applied. Defaults to "default".
            path (Optional[str]): Path to a JSON file containing the custom template. Defaults to None.

        Raises:
            ValueError: If the provided template_name is not valid or if the file cannot be loaded.
        """
        self.style_name = template_name
        self.style: Dict[str, Any] = {}
        self.path = path
        self._proxy = None

        if path:
            self.apply_template(template_name, path)
        elif template_name == "default" or template_name in plt.style.available:
            self.style = dict(plt.rcParams)
            plt.style.use(template_name)
        elif (
            template_name in templates.available
            or template_name in custom.user_templates
        ):
            stylesheet = self._get_template(template_name)
            self.style = stylesheet
            plt.style.use(stylesheet)
        else:
            raise ValueError(f"Invalid template name: {template_name}")

        self.apply_changes()

    def __getattr__(self, name):
        if self._proxy is None:
            self._proxy = StyleProxy(self)
        return getattr(self._proxy, name)

    def apply_changes(self):
        """Apply the current style settings to plt.rcParams."""
        if self.style is not None:
            plt.rcParams.update(self.style)

    @staticmethod
    def _convert_axes_prop_cycle(template):
        if "axes.prop_cycle" in template and isinstance(
            template["axes.prop_cycle"], dict
        ):
            template["axes.prop_cycle"] = cycler(**template["axes.prop_cycle"])

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
            template = getattr(templates, template_name)
        elif template_name in custom.user_templates:
            template = custom.get_custom_template(template_name)
            if template is None:
                raise ValueError(
                    f"Custom template '{template_name}' is not properly defined"
                )
        else:
            raise ValueError(f"Invalid template name: {template_name}")

        self._convert_axes_prop_cycle(template)
        return template

    @staticmethod
    def load_template(name: str, path: str) -> Dict[str, Any]:
        """
        Load a specific template from a JSON file.

        Args:
            name (str): Name of the template to load.
            path (str): Path to the JSON file containing the templates.

        Returns:
            Dict[str, Any]: The loaded template.

        Raises:
            FileNotFoundError: If the specified file is not found.
            KeyError: If the specified template name is not found in the file.
        """
        try:
            with open(path, "r") as f:
                templates = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")

        if "templates" not in templates or name not in templates["templates"]:
            raise KeyError(f"Template '{name}' not found in {path}")

        template = templates["templates"][name]
        Styles._convert_axes_prop_cycle(template)
        return template

    def apply_template(self, name: str, path: str) -> None:
        """
        Load and apply a specific template.

        Args:
            name (str): Name of the template to load and apply.
            path (str): Path to the JSON file containing the templates.
        """
        template = self.load_template(name, path)
        self.style_name = name
        self.style = template
        self.path = path
        plt.style.use(template)
        print(f"Loaded and applied template '{name}' from {path}")

    @classmethod
    def load_custom_settings(cls, file_path: str) -> None:
        """Load custom templates from a JSON file."""
        templates = load_custom_settings(file_path)
        for name, template in templates.items():
            cls._convert_axes_prop_cycle(template)
            custom.register_template(name, template)

    def save_current_template(
        self,
        name: str,
        path: str,
        overwrite: bool = False,
    ) -> None:
        """
        Save the current template to a JSON file.

        Args:
            name (str): Name for the template. Required when saving a new template.
            path (Optional[str]): Path to save the JSON file. If None, uses the path from initialization.
            overwrite (bool): If True, overwrite existing template with the same name. Defaults to False.

        Raises:
            TemplatePathError: If no path is provided and no path was set during initialization.

        Returns:
            None
        """
        if self.style is None:
            print("No active style to save.")
            return

        if name is None:
            raise ValueError("A name must be provided when saving a template.")

        save_path = path if path is not None else self.path
        if save_path is None:
            raise TemplatePathError(
                "Error: File path is required when saving a template."
            )

        # Load existing templates
        try:
            with open(save_path, "r") as f:
                existing_templates = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_templates = {"templates": {}}

        if name in existing_templates["templates"] and not overwrite:
            print(
                f"Template '{name}' already exists. Use overwrite=True to replace it."
            )
            return

        template_dict = {name: self.style.copy()}

        # Convert Cycler to dict for JSON serialization
        if "axes.prop_cycle" in template_dict[name]:
            template_dict[name]["axes.prop_cycle"] = cycler_to_dict(
                template_dict[name]["axes.prop_cycle"]
            )

        # Add or update the template
        existing_templates["templates"].update(template_dict)

        # Save updated templates
        with open(save_path, "w") as f:
            json.dump(existing_templates, f, indent=2)

        # Update plt.rcParams with the current style
        plt.rcParams.update(self.style)

        action = (
            "updated"
            if overwrite and name in existing_templates["templates"]
            else "saved"
        )
        print(f"Template '{name}' {action} successfully in {save_path}.")
