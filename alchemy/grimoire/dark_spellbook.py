"""Dark spellbook module demonstrating naive circular dependency."""
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return dark ingredients list."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Record dark spell using validator."""
    result: str = validate_ingredients(ingredients)
    if "VALID" in result and "INVALID" not in result:
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
