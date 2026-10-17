"""Potions module brewing remedies from fundamental elements."""

from elements import create_fire, create_water
from .elements import create_air, create_earth


def healing_potion() -> str:
    """Brew a healing potion using earth and air."""
    return (
        f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    """Brew a strength potion using fire and water."""
    return (
        f"Strength potion brewed with '{create_fire()}' and '{create_water()}'"
    )
