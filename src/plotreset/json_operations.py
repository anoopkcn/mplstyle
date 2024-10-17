# plotreset/src/plotreset/json_operations.py
import json
from typing import Any, Dict

from cycler import Cycler


def cycler_to_dict(cy):
    return {key: list(value) for key, value in cy.by_key().items()}


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Cycler):
            return cycler_to_dict(o)
        return super().default(o)


def load_custom_settings(file_path: str) -> Dict[str, Any]:
    """Load custom template from a JSON file."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data.get("templates", {})
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in file: {file_path}")


def save_template(template: Dict[str, Any], file_path: str) -> None:
    """Save template to a JSON file."""
    try:
        with open(file_path, "w") as file:
            json.dump({"templates": template}, file, indent=2, cls=CustomEncoder)
        print(f"Template saved to {file_path}")
    except Exception as e:
        print(f"Error saving template: {e}")
