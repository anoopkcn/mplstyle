from typing import Any, Callable, Dict

from cycler import cycler

user_templates: Dict[str, Dict[str, Any]] = {}
user_cycles: Dict[str, Callable[[], Any]] = {}


def register_template(name: str, template: Dict[str, Any]) -> None:
    """Register a custom template."""
    user_templates[name] = template


def register_cycle(name: str, cycle_function: Callable[[], Any]) -> None:
    """Register a custom cycle."""
    user_cycles[name] = cycle_function


def get_custom_template(name: str) -> Dict[str, Any]:
    """Get a custom template by name."""
    return user_templates.get(name, {})


def get_custom_cycle(name: str) -> Callable[[], Any]:
    """Get a custom cycle by name."""
    return user_cycles.get(name, lambda: cycler(color=["black"]))
