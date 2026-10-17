"""Transmutation recipes converting base elements into precious ones."""

from elements import create_fire
from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    """Execute recipe transmuting lead to gold."""
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}' and "
        f"'{strength_potion()}' mixed with '{create_fire()}'"
    )
