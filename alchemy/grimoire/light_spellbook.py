"""Light spellbook recording formulas using safe deferred imports."""


def light_spell_allowed_ingredients() -> list[str]:
    """Return the list of ingredients allowed for light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Validate and record a light spell, avoiding circular imports."""
    from .light_validator import validate_ingredients

    result: str = validate_ingredients(ingredients)
    if "VALID" in result and "INVALID" not in result:
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
